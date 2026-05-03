#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Alpha Oracle Pro v14.0 — WebSocket 即時監控（常駐服務版）
══════════════════════════════════════════════════════════════════════
功能優化：
1. 秒級監控：訂閱 OKX Tickers 頻道，獲取最即時的市場價格。
2. 斷線容錯：整合 v14.0 的歷史 K 線掃描，斷線期間的插針也會被捕抓。
3. 自動保本/鎖利：同步執行 v14.0 的 TP1 移位止損與 TP2 鎖利邏輯。
4. 低延遲：針對活躍訊號進行定向檢查，避免無效的 API 請求。
══════════════════════════════════════════════════════════════════════
"""
import asyncio
import json
import os
import sys
import time
import logging
from datetime import datetime

try:
    import websockets
except ImportError:
    print("❌ 缺少依賴：請執行 'pip install websockets requests'")
    sys.exit(1)

# 匯入主程式邏輯
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import main as bot

# 日誌設定
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stdout,
)

OKX_WS_URL = "wss://ws.okx.com:8443/ws/v5/public"

# ═════════════════════════════════════════════════════════
# 核心 WebSocket 監控邏輯
# ═════════════════════════════════════════════════════════

async def subscribe_tickers(coins: list):
    """訂閱 OKX 即時價格，觸發訊號檢查"""
    while True:
        try:
            async with websockets.connect(OKX_WS_URL, ping_interval=25, ping_timeout=10) as ws:
                # 訂閱 Tickers
                args = [{"channel": "tickers", "instId": c} for c in coins]
                sub_msg = {"op": "subscribe", "args": args}
                await ws.send(json.dumps(sub_msg))
                logging.info(f"✅ WebSocket 成功訂閱 {len(coins)} 個幣種")

                async for raw in ws:
                    try:
                        msg = json.loads(raw)
                    except Exception:
                        continue
                        
                    if msg.get("event") == "subscribe":
                        continue
                        
                    data = msg.get("data") or []
                    for tick in data:
                        inst_id = tick.get("instId")
                        last_price = float(tick.get("last", 0))
                        if inst_id and last_price > 0:
                            await on_price_update(inst_id, last_price)
                            
        except Exception as e:
            logging.error(f"⚠️ WebSocket 斷線：{e}，10 秒後嘗試重連...")
            await asyncio.sleep(10)

# 控制處理頻率，避免過度讀寫硬碟
_last_check_time: dict = {}

async def on_price_update(inst_id: str, price: float):
    """當價格變動時，執行 v14.0 訊號追蹤邏輯"""
    
    # 頻率限制：每個幣種每 1 秒最多觸發一次磁碟檢查
    now = time.time()
    if now - _last_check_time.get(inst_id, 0) < 1.0:
        return
    _last_check_time[inst_id] = now

    # 初始化 Tracker (會讀取 active_signals.json)
    tracker = bot.SignalTracker()
    
    # 篩選出與當前幣種相關的活躍訊號
    active_ids = [sid for sid, s in tracker.signals.items() if s.get("instId") == inst_id]
    if not active_ids:
        return

    logging.info(f"⚡ {inst_id} 即時價: {price} | 監測中訊號: {len(active_ids)}")

    # 執行 v14.0 的 _check_one 邏輯 (包含插針捕抓與 TP/SL 移動)
    to_remove = []
    for sid in active_ids:
        sig = tracker.signals.get(sid)
        if not sig:
            continue
            
        try:
            # 這裡會觸發 bot._check_one，內含自動掃描歷史 K 線的功能
            if tracker._check_one(sid, sig):
                to_remove.append(sid)
        except Exception as e:
            logging.error(f"❌ 訊號處理錯誤 [{sid}]: {e}")

    # 若有訊號結算，更新檔案
    if to_remove:
        for sid in to_remove:
            tracker.signals.pop(sid, None)
        tracker._save()
        logging.info(f"🎯 訊號結算完成，移除數量: {len(to_remove)}")

# ═════════════════════════════════════════════════════════
# 背景任務：定期與主配置同步
# ═════════════════════════════════════════════════════════

async def config_sync_loop():
    """定期重新讀取配置，確保幣種清單是最新的"""
    while True:
        # 每小時執行一次全局訊號檢查，防止任何極端情況下的遺漏
        try:
            tracker = bot.SignalTracker()
            tracker.check_all()
            logging.info("🔄 定期全局檢查 (Cleanup) 完成")
        except Exception as e:
            logging.error(f"❌ 定期檢查失敗: {e}")
            
        await asyncio.sleep(3600)

async def run_oracle_ws():
    # 讀取配置
    cfg = bot.load_config()
    coins = cfg.get("coins", bot.ALL_COINS)
    
    logging.info("🚀 Alpha Oracle Pro v14.0 WebSocket 服務啟動")
    logging.info(f"📍 監控幣種: {', '.join(coins)}")
    
    # 同時跑 WebSocket 監控與定期同步
    await asyncio.gather(
        subscribe_tickers(coins),
        config_sync_loop()
    )

if __name__ == "__main__":
    if not bot.TG_TOKEN or not bot.CHAT_ID:
        logging.critical("❌ 環境變數缺失：請設定 TG_TOKEN 與 CHAT_ID")
        sys.exit(1)
        
    try:
        asyncio.run(run_oracle_ws())
    except KeyboardInterrupt:
        logging.info("👋 服務已手動停止")
