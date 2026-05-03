import asyncio
import json
import logging
import websockets
import main as bot  # 引用你的 main.py

# 設定 OKX WebSocket 位址[cite: 3]
OKX_WS_URL = "wss://ws.okx.com:8443/ws/v5/public"

async def on_price_update(instId, price):
    """每當價格更新，就調用你 main.py 裡的追蹤邏輯"""
    tracker = bot.SignalTracker() 
    # 找到所有與該幣種相關的活耀訊號[cite: 3]
    related = [k for k, s in tracker.signals.items() if s.get("instId") == instId]
    
    if not related:
        return

    to_remove = []
    for sid in related:
        sig = tracker.signals[sid]
        # 直接執行你寫在 main.py 裡的 v14.0 檢查邏輯[cite: 3]
        if tracker._check_one(sid, sig):
            to_remove.append(sid)
            logging.info(f"🎯 訊號 {sid} 已結清，價格: {price}")

    if to_remove:
        for sid in to_remove:
            tracker.signals.pop(sid, None)
        tracker._save()[cite: 3]

# ... (其餘 WebSocket 訂閱邏輯保持不變) ...
