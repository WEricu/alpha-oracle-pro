#!/usr/bin/env python3
"""
service.py — Alpha Oracle Pro Koyeb/Railway Service Mode v2
掩描排程 + Telegram callback 秒級輪詢
"""
import hashlib
import os
import sys
import time
import threading
import logging
import base64
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler

# ── 日誌 ──
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

# ── 環境變數 ──
GH_TOKEN          = os.environ.get("GITHUB_TOKEN", "")
GH_REPO           = os.environ.get("GH_REPO", "WEricu/alpha-oracle-pro")
GH_BRANCH         = "main"
SCAN_INTERVAL     = int(os.environ.get("SCAN_INTERVAL", 600))
CALLBACK_INTERVAL = int(os.environ.get("CALLBACK_INTERVAL", 5))
PORT              = int(os.environ.get("PORT", 8000))

# ── GitHub API 狀態同步 ──
_gh_shas: dict = {}
_gh_content_hashes: dict = {}
_gh_lock = threading.Lock()

STATE_FILES = [
    "active_signals.json",
    "system_state.json",
    "tg_update_offset.json",
    "signal_cooldown.json",
    "trade_history.json",
    "learning_state.json",
]


def _gh_headers():
    return {"Authorization": f"token {GH_TOKEN}", "Accept": "application/vnd.github+json"}


def gh_load_all():
    if not GH_TOKEN:
        logging.warning("GITHUB_TOKEN 未設定，跳過狀態同步")
        return
    for fname in STATE_FILES:
        try:
            r = requests.get(
                f"https://api.github.com/repos/{GH_REPO}/contents/{fname}",
                headers=_gh_headers(),
                params={"ref": GH_BRANCH},
                timeout=10,
            )
            if r.status_code == 200:
                d = r.json()
                _gh_shas[fname] = d["sha"]
                content_bytes = base64.b64decode(d["content"])
                with open(fname, "wb") as f:
                    f.write(content_bytes)
                _gh_content_hashes[fname] = hashlib.md5(content_bytes).hexdigest()
                logging.info(f"gh_load: {fname} OK")
            elif r.status_code == 404:
                logging.info(f"gh_load: {fname} not found on GitHub, using local default")
            else:
                logging.warning(f"gh_load: {fname} HTTP {r.status_code}")
        except Exception as e:
            logging.warning(f"gh_load {fname}: {e}")


def gh_save_file(fname: str):
    if not GH_TOKEN or not os.path.exists(fname):
        return
    with _gh_lock:
        try:
            with open(fname, "rb") as f:
                raw = f.read()
            new_hash = hashlib.md5(raw).hexdigest()
            if _gh_content_hashes.get(fname) == new_hash:
                return
            body = {
                "message": f"service: sync [skip ci] {fname}",
                "content": base64.b64encode(raw).decode(),
                "branch": GH_BRANCH,
            }
            if fname in _gh_shas:
                body["sha"] = _gh_shas[fname]
            r = requests.put(
                f"https://api.github.com/repos/{GH_REPO}/contents/{fname}",
                headers=_gh_headers(),
                json=body,
                timeout=15,
            )
            if r.status_code in (200, 201):
                _gh_shas[fname] = r.json()["content"]["sha"]
                _gh_content_hashes[fname] = new_hash
                logging.info(f"gh_save: {fname} OK")
            elif r.status_code == 409:
                info = requests.get(
                    f"https://api.github.com/repos/{GH_REPO}/contents/{fname}",
                    headers=_gh_headers(),
                    params={"ref": GH_BRANCH},
                    timeout=10,
                ).json()
                _gh_shas[fname] = info["sha"]
                body["sha"] = info["sha"]
                r2 = requests.put(
                    f"https://api.github.com/repos/{GH_REPO}/contents/{fname}",
                    headers=_gh_headers(), json=body, timeout=15,
                )
                if r2.status_code in (200, 201):
                    _gh_shas[fname] = r2.json()["content"]["sha"]
                    _gh_content_hashes[fname] = new_hash
                    logging.info(f"gh_save (retry): {fname} OK")
            else:
                logging.warning(f"gh_save: {fname} HTTP {r.status_code}")
        except Exception as e:
            logging.warning(f"gh_save {fname}: {e}")


def gh_sync_all():
    for fname in STATE_FILES:
        gh_save_file(fname)


import main as _main

tracker = None


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        sig_count = len(tracker.signals) if tracker else 0
        body = (
            f"Alpha Oracle Pro OK\n"
            f"Time: {_main.tw_ts()}\n"
            f"Signals: {sig_count}"
        ).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass


def health_server():
    HTTPServer(("", PORT), HealthHandler).serve_forever()


def callback_loop():
    logging.info(f"Callback loop started, interval {CALLBACK_INTERVAL}s")
    while True:
        try:
            _main.process_pending_approvals(tracker)
        except Exception as e:
            logging.error(f"callback_loop: {e}")
        time.sleep(CALLBACK_INTERVAL)


def scan_loop():
    logging.info(f"Scan loop started, interval {SCAN_INTERVAL // 60} min")
    while True:
        try:
            _main.run_scan(tracker)
        except Exception as e:
            logging.error(f"scan_loop: {e}")
            import traceback; traceback.print_exc()
        try:
            gh_sync_all()
        except Exception as e:
            logging.warning(f"gh_sync: {e}")
        time.sleep(SCAN_INTERVAL)


if __name__ == "__main__":
    logging.info("Alpha Oracle Pro — Service Mode starting")
    gh_load_all()
    tracker = _main.SignalTracker(_main.ACTIVE_SIGNALS_FILE)
    logging.info(f"SignalTracker ready, signals={len(tracker.signals)}")
    threading.Thread(target=health_server, daemon=True).start()
    threading.Thread(target=callback_loop, daemon=True).start()
    scan_loop()
