import json
import os
import time

# 檔案定義（對齊 GitHub Action 與 WebSocket 溝通路徑）
ACTIVE_SIGNALS_FILE = "active_signals.json"[cite: 3]

class SignalTracker:
    def __init__(self):
        self.signals = self._load()

    def _load(self):
        if os.path.exists(ACTIVE_SIGNALS_FILE):
            with open(ACTIVE_SIGNALS_FILE, "r") as f:
                try:
                    return json.load(f)
                except:
                    return {}
        return {}

    def _save(self):
        with open(ACTIVE_SIGNALS_FILE, "w") as f:
            json.dump(self.signals, f, indent=2)[cite: 3]

    def add_signal(self, sid, data):
        """當 main.py 發現新機會時，調用此函數存檔"""
        self.signals[sid] = data
        self._save()

    def _check_one(self, sid, sig):
        """
        這裡是 v14.0 的核心監控邏輯
        包含：TP1 移保本、TP2 鎖利、TP3 結清
        """
        # ... (此處填入你原本的價格檢查邏輯) ...
        # 如果觸發結清，回傳 True
        return False

# 修改原本的 generate_signal 流程
def process_signals():
    tracker = SignalTracker()
    # 假設你的主邏輯產出了 new_sig
    # tracker.add_signal(new_sig_id, new_sig_data)
