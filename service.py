h#!/usr/bin/env python3
"""
service.py — Alpha Oracle Pro Koyeb Service Mode
即時掃描 + Telegram callback 秒回應
"""
import os, sys, time, threading, logging, json, base64, requests
from http.server import HTTPServer, BaseHTTPRequestHandler

# ── 日誌 ──
logging.basicConfig(
    level=logging.INFO,h
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
_gh_lock = threading.Lock()

STATE_FILES = [
    "active_signals.json",
    "system_state.json",
    "tg_offset.json",
    "cooldowns.json",
    "trade_history.json",
    "learning_data.json",
]

def _gh_headers():
    return {"Authorization": f"token {GH_TOKEN}", "Accept": "application/vnd.github+json"}

def gh_load_all():
    if not GH_TOKEN:
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
                content = base64.b64decode(d["content"]).decode()
                with open(fname, "w", encoding="utf-8") as f:
                    f.write(content)
                logging.info(f"載入 {fname}")
            elif r.status_code == 404:
                logging.info(f"{fname} 不存在，使用預設值")
        except Exception as e:
            logging.warning(f"gh_load {fname}: {e}")

def gh_save_file(fname: str):
    if not GH_TOKEN or not os.path.exists(fname):
        return
    with _gh_lock:
        try:
            with open(fname, "rb") as f:
                raw = f.read()
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
        except Exception as e:
            logging.warning(f"gh_save {fname}: {e}")

def gh_sync_all():
    for fname in STATE_FILES:
        gh_save_file(fname)

import main as _main

tracker = _main.SignalTracker(_main.ACTIVE_SIGNALS_FILE)

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = (
            f"Alpha Oracle Pro OK\n"
            f"Time: {_main.tw_ts()}\n"
            f"Signals: {len(tracker.signals)}"
        ).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *a): pass

def health_server():
    logging.info(f"Health server on :{PORT}")
    HTTPServer(("0.0.0.0", PORT), HealthHandler).serve_forever()

def callback_loop():
    logging.info(f"Callback loop every {CALLBACK_INTERVAL}s")
    while True:
        try:
            _main.process_pending_approvals(tracker)
        except Exception as e:
            logging.error(f"callback_loop: {e}")
        time.sleep(CALLBACK_INTERVAL)

def scan_loop():
    logging.info(f"Scan loop every {SCAN_INTERVAL // 60}min")
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
    logging.info("Alpha Oracle Pro — Koyeb Service Mode")
    gh_load_all()

    tracker = _main.SignalTracker(_main.ACTIVE_SIGNALS_FILE)
    threading.Thread(target=health_server, daemon=True).start()
    threading.Thread(target=callback_loop, daemon=True).start()
    scan_loop()
