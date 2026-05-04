#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Alpha Oracle Pro v14.7 â ç²¾æºå¹æ ¼åµæ¸¬ + é²æ´çï¼ç¹é«ä¸­æï¼
ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
â¨ v14.7 ä¿®å¾© / æ°å¢ï¼
  ðª å³æå¹åä½µé² K ç·ï¼OKX ticker tick æ¯ K ç·å¿«ï¼èåå¾æå¾æ´æ©
  ð¡ï¸ æåæ´æ° 15 åé throttleï¼1 åé cron ä¸åæ¯åéæ´ç
     â³ ä¿®å¾© v14.6 ä¹å¾ TP/SL éæ¨éç¥è¢«æåæ´æ°æ´å°ä¸é¢å»çä¸å°ç bug
  ð send_tg å éè©¦ï¼429 ééç­ retry_after / 5xx ç¨ exponential backoff
     â³ è¨æ¯ééçå¾ ~95% â ~99.9%

â¨ v14.6ï¼
  â¡ ä¸»æææ¹ 1 åé cronï¼åä½µ Pro + Monitor æå®ä¸ jobï¼
  ð¡ï¸ æ©æéåºï¼å¨é¨å¹£é½å·å» / æåæè·³éé APIï¼åªè·ç£æ§ï¼5 ç§æå®ï¼
  ð¡ï¸ å´æ ¼æ¯æ¥é¢¨æ§ä¸ç´ç·ï¼
     â  åææåæ¸ä¸éï¼é è¨­ 2 åï¼
     â¡ ç¶æ¥ç´¯è¨ PnL < -5% åæ­¢éæ°å®å°éå¤©
     â¢ ä¸å¤©æå¤ 6 ç­è¨è

â¨ v14.5ï¼
  ðµ è³é / æ§æ¡¿ / æçè©¦ç®ï¼ä¾ $100 è³éã$20 é¢¨éªèªåç®æ§æ¡¿èå TP ç¾åæç
  ð è¦ç¤è¨æ¯ä¿è­ééï¼è³æä¸è¶³ / ä¾å¤æä¹é fallbackï¼ä¸åéé»å¤±æ
  ð§± OB å¤±æéå ´ç¾å¨ä¹æéè¦ç¤åæ

â¨ v14.4ï¼
  ðª VWAP éå æ¬åå¹ï¼èå¾è©åå  Â±3ï¼ä¸é¡¯ç¤ºçµ¦ç¨æ¶ï¼é¿åè¨æ¯å¤ªäºï¼
  ð¡ï¸ é è¨­ééãè©åç´°é é¡¯ç¤ºãï¼é²å ´éç¥æ´ä¹¾æ·¨ï¼show_score_breakdown=Falseï¼
  ð§ ä¿®å¾© TP é åº bugï¼å dynamic TP æ ¡æ­£æè® TP3 â¤ TP2ï¼DOGE/NEAR æ¡ä¾ï¼
  ð¯ æ¹æé è¨­ãåºå® R:Rã(1.5R/3R/5R)ï¼å¯é æãæ°¸é å®èª¿éå¢
     â³ æ³ç¨åæ TP æ¹ config: fixed_rr_mode=falseï¼å·²ä¿®å¥½ collapse bugï¼

â¨ v14.3ï¼
  ð©º å¥åº·ç£æ§ï¼24h æ²é TG / é£ 5 æ¬¡å¤±æ â èªåç¼è­¦å ±ï¼6h ä¸éè¤ï¼
  ð¬ ææ¨å¯©æ¥ï¼/auditï¼ï¼ç¥ç´ vs ä¸è¬ãMTF é å¢ vs ä¸­æ§ãéè½ãå¸æ³ãæ¹å
     â³ ç¨å¯¦éåçé©è­æ¯åææ¨æ¯å¦ççææï¼ââ ï¸â ä¸ç´å¤è®ï¼
  ð¦ å·¥ä½æµåä½µï¼alpha_oracle.yml ä¸æªå Pro + Monitor å©å Job

â¨ v14.2ï¼é²éæºè½ 5 é ï¼ï¼
  ð è¨èæ¹åçµ±è¨ + èªåååé«åçæ¹åï¼/direction å½ä»¤ï¼
  ð¯ ç¥ç´è¨èç¹å¥æ¨è¨ï¼95+ åç¨ ð¯ð¯ð¯ éç®æ¨é¡
  ðª EMA å¤é±ææåï¼20/50/200 å®ç¾æå +5ãé 200 -5
  ð¥ éç±ä¿è­·ï¼æå¹£é£ 3 åå¾æ«åä¸è¼ªé¿åéåº¦ä¾è³´
  ð§± OB å¤±æéå ´ï¼é²å ´ä¾æçè¨å®å¡æ¶ç¤è¢«ç ´ â ä¸»åæåéå ´

â¨ v14.1ï¼é«åçç²¾é¸ + é¢¨æ§å¼·åï¼ï¼
  ð é²å ´éç¥é¡¯ç¤ºãçºä»éº¼ N åãåæ¸ç´°é æè§£
  ð¼ åä½å¤§å°å»ºè­°ï¼ä¾åæ¸æ¨è¦ 0.5x / 1.0x / 1.5x
  â¸ï¸ èªåæ«åçå¹£ï¼éå» 7 å¤©åç < 30% èªåæ«å 24h
  âï¸ R:R æä½éæª»ï¼TP1 < 1.5R èªåæçµï¼é¿ååæ TP æ ¡éé ­ï¼
  âï¸ é£æå·éæï¼é£ 2 æå¾ 30 åéä¸éæ°å®

â¨ v14.0ï¼å°æ¥­äº¤æå¡é¤æï¼ï¼
  ð å¤ææ¡å±æ¯ï¼1H + 4H Supertrend ç¢ºèªï¼æé« +15 åï¼åå -10ï¼
  ð éè½ç¢ºèªï¼æå¾ K é vs å 20 æåéï¼æé« +8 åï¼æ²é -10 ç´æ¥æ·æ±°ï¼
  ð å¸å ´çæè­å¥ï¼ADX è¶¨å¢/éçª/éæ¸¡ï¼éçªå¸éæª»èªå +5
  ð¯ åæ TPï¼åºå® R å TP è½å¨å¼· S/R åæ¹æèªåæ ¡æ­£
  ð° æ°èäºä»¶éæ¿¾ï¼NFP / CPI èªåè¦å + èªè¨äºä»¶æ¸å®
  ð é²å ´ææ©ï¼åµæ¸¬åæ¸¬å½±ç· K å  +3 å
  ð§¬ KNN å­¸ç¿ï¼æ¯ç­è¨èåéåï¼æ¾æç¸ä¼¼ 10 ç­æ­·å²äº¤æçåç
  ð æ¥å ± / æå ±ï¼/daily è /monthly å½ä»¤ï¼å«åå¹£ç¨®ç¸¾æãé£åé£æ
  ð backtest.pyï¼ç¨ç«åæ¸¬è³æ¬ï¼è®æ­·å² K ç·éè·ç­ç¥ï¼
  ð¡ websocket_monitor.pyï¼å¸¸é§ WS ç£æ§ï¼é¨ç½² Railway/Fly.ioï¼

â¨ v13.1 æ¢æï¼
  â¡ monitor æ¨¡å¼ + é«é » cron workflowï¼30 ç§ä¸æ¬¡ï¼
  â¡ monitor æ¨¡å¼ï¼è¼éãåªè¿½æ¢æè¨èï¼ä¸çææ°è¨è
     â³ ç¨æ³ï¼python main.py monitor [polls] [interval]
     â³ æ­é alpha-oracle-monitor.yml æ¯ 3 åé cron + ä¸æ¬¡ 3 è¼ª = ~30 ç§æª¢æ¥ä¸æ¬¡
     â³ TP/SL éç¥å»¶é²å¾ 15 åéå£å° ~30 ç§
  ð æ°æª alpha-oracle-monitor.ymlï¼é«é »ç£æ§å°ç¨ workflow

â¨ v13.0ï¼æèªææé·ï¼ï¼
  ð è¦ç¤åæï¼SL / BE / LOCK å¾èªååæãçºä»éº¼çµç®ãä¸¦é Telegram
     â³ 6 å¤§æ­¸å ï¼è¶¨å¢åè½ / RSI å´©ç¤ / æµåæ§æè© / æ³¢åæ¿å¢ / åååè½ / OB è·ç ´
     â³ éãä¸æ¬¡è©²æéº¼å¤æ·ã+ åé¡è¨­å®æ­·å²åç
  ð§  å­¸ç¿æ©å¶ï¼æ¯ç­äº¤æçµç®å¾æ´æ°æ¡¶ï¼åæ¸/RSI/è³éè²»ç/ææ®µ/å¹£ç¨®ï¼
     â³ è©åæèªåå¥ç¨èª¿æ´ï¼é«åççµå +1~+2ãä½åççµå -2~-3ï¼ä¸é Â±10
     â³ /learning å½ä»¤æ¥çæ©å¨äººå­¸äºä»éº¼
  ð 12 ç¨®å¹£å¥ï¼BTC/ETH/SOL/BNB/XRP/DOGE/ADA/AVAX/LINK/DOT/TON/NEAR
     â³ å¯å¨ config.json ç coins èªè¨

â¨ v12.2 æ¢æï¼
  ð æ­·å² K ç·è£æï¼æ last_checked_ts ä¹å¾ææ K ç·ä¾åºèç
  ð åå¹£ç¨®æªå¹³åå´æ ¼æ
  ð¦ fetch_candles_fullï¼æ¯è¼ªå±ç¨ 30 ç§å¿«å

â¨ v12.1ï¼å¹³åç²¾åº¦ï¼ï¼
  ðª¡ æéè§¸ç¼ï¼K ç·é«ä½é»è§¸å°å¹³åå¹å³è¦çºå¹³å
  ð TP/SL é åºèçï¼TP1 â TP2 â TP3 â SLï¼SL ç¨æ´æ°å¾çå¼ï¼
  ð BE ä¿æ¬é¡¯ç¤ºï¼å°é TP1 å¾è¥ SL è§¸ç¼ï¼ç¨ç«é¡¯ç¤ºãð ä¿æ¬åºå ´ã`0R`
  ð LOCK éå©é¡¯ç¤ºï¼å°é TP2 å¾è¥ SL è§¸ç¼ï¼ç¨ç«é¡¯ç¤ºãð éå©åºå ´ã`+1.5R`
  ðª¡ éç¥æ¨è¨æéè§¸ç¼ä¾æºï¼K ç·æéè§¸åç®æ¨å¹ï¼

â¨ v12.0 æ°å¢ï¼é«åªåç´é¢¨æ§ï¼ï¼
  ð TradingView ç¬¬äºå¹æ ¼ä¾æº â OKX/TV åé¢è¶éé¾å¼èªåè·³é
  ð é£çºè§æçæ·ï¼é£ 3 ææ«å 4hãé£ 5 æç¡¬çæ· 24h
  ð ééµææ®µéæ¿¾ï¼è³éè²»ççµç® / ç¾è¡éç¤ç­é«æ³¢åææ®µèªåé¿é
  ð config.json ç±æ´æ°èé©è­ï¼ç¡ééæ°é¨ç½²å³å¯èª¿æ´åæ¸
  ð ç³»çµ±çææä¹åï¼system_state.jsonï¼ï¼çæ·çæè·¨ Actions ä¸æ¼
  ð åå¹£ç¨®æªå¹³åä¸éè¤éå

â¨ v11.0 æ¢æéé»ï¼
  â ä¿®å¾©ææ Markdown éæ¥åçèªæ³é¯èª¤
  â å®æ´ SMCï¼OBï¼/ ICTï¼FVGãæµåæ§æè©ï¼/ SNR / å¹æ ¼è¡çº / ç¤å£åè½
  â è©å 100 åå¶ï¼è¶¨å¢30+RSI25+OB20+FVG15+SNR5+PA5+æµåæ§5+åè½5ï¼
  â æ­¢çåç 1.5R / 3.0R / 5.0R
  â æéå°ç£ UTC+8 / è¨èå·å»æä¹å / TPÂ·SL ç·å±¤åè¦
ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
"""
import requests
import os
import json
import logging
import time
import sys
import uuid
from datetime import datetime, timezone, timedelta


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# ð¹ð¼ å°ç£æéå·¥å·
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
TW_TZ = timezone(timedelta(hours=8))


def tw_now() -> datetime:
    """ç²åå°ç£æé datetime ç©ä»¶"""
    return datetime.now(TW_TZ)


def tw_ts() -> str:
    """å°ç£æéæéæ³å­ä¸²ï¼çµ¦éç¥é¡¯ç¤ºç¨ï¼"""
    return tw_now().strftime("%Y-%m-%d %H:%M:%S å°ç£æé")


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# ð§ ç°å¢è®æ¸å®å¨è§£æ
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def _get_env(key: str, default: str = "") -> str:
    val = os.getenv(key)
    return val.strip() if val and val.strip() else default


def _get_env_int(key: str, default: int) -> int:
    val = os.getenv(key)
    try:
        return int(val.strip()) if val and val.strip() else default
    except Exception:
        return default


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 1. åºç¤éç½®
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    stream=sys.stdout,
)

TG_TOKEN = _get_env("TG_TOKEN")
CHAT_ID = _get_env("CHAT_ID")

ALL_COINS = [
    "BTC-USDT-SWAP", "ETH-USDT-SWAP", "SOL-USDT-SWAP",
    "BNB-USDT-SWAP", "XRP-USDT-SWAP", "DOGE-USDT-SWAP",
    "ADA-USDT-SWAP", "AVAX-USDT-SWAP", "LINK-USDT-SWAP",
    "DOT-USDT-SWAP", "TON-USDT-SWAP", "NEAR-USDT-SWAP",
]
MAX_SIGNALS = _get_env_int("MAX_SIGNALS", 3)
SCORE_THRESHOLD = _get_env_int("SETUP_SCORE_THRESHOLD", 68)

SIGNAL_EXPIRE_HOURS = 24
COOLDOWN_HOURS = 2

ACTIVE_SIGNALS_FILE = "active_signals.json"
TRADE_HISTORY_FILE = "trade_history.json"
COOLDOWN_FILE = "signal_cooldown.json"
CONFIG_FILE = "config.json"
SYSTEM_STATE_FILE = "system_state.json"
LEARNING_FILE = "learning_state.json"

# è¨æ¶é«å¿«åï¼åä¸è¼ªå·è¡å§å±ç¨ï¼è·¨è¼ªä¸æä¹ï¼
_price_cache: dict = {}

# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 1.5 é è¨­éç½®ï¼config.json ä¸å­å¨æç fallbackï¼
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
DEFAULT_CONFIG: dict = {
    "coins": ALL_COINS,                # å¯å¨ config.json èªè¨
    "max_signals": 3,
    "score_threshold": 68,
    "cooldown_hours": 2,
    "signal_expire_hours": 24,
    "atr_max_pct": 0.04,
    "post_mortem": {
        "enabled": True,
        "loss_only": False,            # False = SL/BE/LOCK é½åè¦ç¤ï¼True = åª SL
    },
    "learning": {
        "enabled": True,
        "knn_enabled": True,           # é²é KNN å­¸ç¿ï¼æ¾æç¸ä¼¼æ­·å²äº¤æï¼
        "min_samples": 5,
        "max_score_adjust": 10,
    },
    "news_blackouts": [
        # ç¨æ¶å¯èªè¨äºä»¶ï¼ä¾å¦ï¼
        # {"start": "2026-05-07T20:30:00+08:00", "end": "2026-05-07T22:30:00+08:00", "reason": "FOMC æè­°"}
    ],
    "auto_news_blackout": {
        "nfp": True,                   # æ¯æç¬¬ä¸é±äº 21:25â22:30 (TW)
        "cpi": True,                   # æ¯æ 10â16 æ¥ 21:25â22:30 (TW)
    },
    # ââ v14.1 æ°å¢ï¼é«åçç¯©é¸ + é¢¨æ§å¼·å ââ
    "show_score_breakdown": False,     # é²å ´éç¥é¡¯ç¤ºåæ¸ç´°é æè§£ï¼é è¨­ééï¼å¤ªéäºï¼
    "fixed_rr_mode": True,             # åºå® 1.5R/3R/5Rï¼é è¨­ï¼ï¼ééæ¹ç¨åæ TP æ ¡æ­£
    # ðµ åä½ / æ§æ¡¿ / æçè©¦ç®
    "capital_management": {
        "enabled": True,
        "capital_per_trade_usd": 100,  # æ¨æºå®ç­è³é
        "max_loss_usd": 20,            # æå¤§å¯æ¥åè§æï¼å«æçºè²»çç·©è¡ï¼
        "max_leverage": 50,            # ä¸éæ§æ¡¿ï¼é¿åæ¥µç­ SL ç®åºè¶é«æ§æ¡¿ï¼
        "min_leverage": 2,             # ä¸éï¼é¿åæ¥µé  SL ç®åº 0.x æ§æ¡¿ï¼
    },
    # ð¡ï¸ v14.6 å´æ ¼é¢¨æ§ï¼æ¯æ¥ä¸é + åææåæ¸
    "daily_limits": {
        "enabled": True,
        "max_concurrent_positions": 2,  # åææå¤ N ååä½
        "daily_loss_limit_pct": 5.0,    # ç¶æ¥ç´¯è¨ PnL < -N% åæ­¢éæ°å®
        "max_daily_signals": 6,         # ä¸å¤©æå¤é N ç­æ°è¨è
    },
    "coin_auto_pause": {               # èªåæ«åçå¹£
        "enabled": True,
        "days": 7,                     # éå» N å¤©
        "min_trades": 5,               # è³å° N ç­æå¤å®
        "max_winrate": 0.30,           # åçä½æ¼æ­¤å¼å°±æ«å
        "pause_hours": 24,
    },
    "position_sizing": {               # åä½å¤§å°å»ºè­°
        "enabled": True,
        "tiers": [
            {"min_score": 95, "multiplier": 1.5, "label": "ð¥ å¼·è¨èå å¤§å"},
            {"min_score": 85, "multiplier": 1.0, "label": "æ¨æºå"},
            {"min_score": 80, "multiplier": 0.5, "label": "è¬¹æå°å"},
            {"min_score": 0,  "multiplier": 0.5, "label": "æ¨æºå"},
        ],
    },
    "min_rr_ratio": 1.5,               # TP1 è³å°è¦æ 1.5R ææ¥ï¼å¦åæçµ
    "cooling_off": {                   # é£æå·éæ
        "enabled": True,
        "loss_threshold": 2,           # é£ N æå¾ååå·é
        "period_minutes": 30,          # å·é N åé
    },
    # ââ v14.2 æ°å¢ï¼æ¹ååå¥½ / ç¥ç´è¨è / EMA / éç± / OB å¤±æ ââ
    "direction_bias": {                # èªååå¥½é«åçæ¹å
        "enabled": True,
        "min_diff_pct": 15,            # LONG/SHORT åçå·® â¥ N% æåååå¥½
        "min_samples": 10,             # è³å°å N ç­æä¿¡
        "bonus": 3,                    # é å¢æ¹åå å
        "penalty": 3,                  # éå¢æ¹åæ£å
    },
    "god_signal": {                    # ç¥ç´è¨èç¹å¥æ¨è¨
        "enabled": True,
        "min_score": 95,
    },
    "ema_alignment": {                 # å¤ææ¡ EMA æå
        "enabled": True,
        "periods": [20, 50, 200],
        "perfect_bonus": 5,            # å®ç¾æåå å
        "partial_bonus": 3,            # é¨åæåå å
        "against_penalty": 5,          # é EMA200 æ£å
    },
    "overheating": {                   # éåº¦éä¸­ä¿è­·
        "enabled": True,
        "win_streak_threshold": 3,     # é£ N åå¾ååä¿è­·
        "cooldown_hours": 4,
    },
    "ob_invalidation": {               # OB / FVG å¤±æéå ´
        "enabled": True,
        "break_buffer_pct": 0.2,       # æ¶ç¤è·ç ´ OB éç·£ N% â è¦çºå¤±æ
    },           # ATR/Price è¶éæ­¤å¼è¦çºéçªéå¤§
    "price_verification": {
        "enabled": True,
        "max_deviation_pct": 0.5,  # OKX è TradingView åé¢ > 0.5% è·³é
        "block_on_unverified": False,  # TV æä¸å°ææ¯å¦ä¸å¾è·³éï¼False=æ¾è¡ï¼
    },
    "circuit_breaker": {
        "enabled": True,
        "soft_threshold": 3,       # é£ 3 æ â è»çæ·
        "soft_pause_hours": 4,
        "hard_threshold": 5,       # é£ 5 æ â ç¡¬çæ·
        "hard_pause_hours": 24,
    },
    # å°ç£æéææ®µï¼HH:MMï¼ï¼çµææéçºãä¸å«ã
    "blackout_windows_tw": [
        {"start": "07:50", "end": "08:10", "reason": "è³éè²»ççµç®ï¼00 UTCï¼"},
        {"start": "15:50", "end": "16:10", "reason": "è³éè²»ççµç®ï¼08 UTCï¼"},
        {"start": "23:50", "end": "00:10", "reason": "è³éè²»ççµç®ï¼16 UTCï¼"},
        {"start": "21:25", "end": "21:45", "reason": "ç¾è¡éç¤æ³¢å"},
        {"start": "02:00", "end": "02:30", "reason": "FOMC å¬å¸ææ®µ"},
    ],
}


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 2. éç¥ç³»çµ±
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def send_tg(
    msg: str,
    parse_mode: str = "Markdown",
    reply_markup: dict | None = None,
    reply_to_message_id: int | None = None,
    max_retries: int = 3,
) -> int | None:
    """ð¤ ç¼é Telegram éç¥ â åå³ message_idï¼å¤±æå Noneï¼

    v14.7 å å¥éè©¦ï¼429 (rate limit) ç­ retry_afterï¼5xx ç¨ exponential backoff
    """
    if not TG_TOKEN or not CHAT_ID:
        logging.warning("â ï¸ TG_TOKEN æ CHAT_ID æªè¨­å®ï¼ç¥éç¼é")
        return None

    payload = {
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": parse_mode,
        "disable_web_page_preview": True,
    }
    if reply_markup:
        payload["reply_markup"] = json.dumps(reply_markup)
    if reply_to_message_id:
        payload["reply_to_message_id"] = reply_to_message_id
        payload["allow_sending_without_reply"] = True

    last_err = ""
    for attempt in range(max_retries):
        try:
            r = requests.post(
                f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
                json=payload,
                timeout=8,
            )
            if r.status_code == 200:
                # ð©º å¥åº·ç£æ§ï¼ç´éæå¾ä¸æ¬¡æåé TG çæé
                try:
                    _state = _load_json(SYSTEM_STATE_FILE, {})
                    _state["last_tg_sent"] = time.time()
                    _save_json(SYSTEM_STATE_FILE, _state)
                except Exception:
                    pass
                return r.json().get("result", {}).get("message_id")

            # 429 = ééï¼æ Telegram çµ¦ç retry_after ç­
            if r.status_code == 429:
                try:
                    wait = float(r.json().get("parameters", {}).get("retry_after", 2))
                except Exception:
                    wait = 2.0
                wait = min(wait + 0.5, 15)
                logging.warning(f"â³ TG 429 ééï¼ç­ {wait:.1f}s éè©¦")
                time.sleep(wait)
                last_err = "429 rate limit"
                continue

            # 5xx = ä¼ºæå¨é¯ï¼exponential backoff
            if r.status_code >= 500:
                wait = 2 ** attempt
                logging.warning(f"â³ TG {r.status_code} ä¼ºæå¨é¯ï¼{wait}s å¾éè©¦")
                time.sleep(wait)
                last_err = f"server {r.status_code}"
                continue

            # 4xx å¶ä»é¯ä¸éè©¦ï¼éå¸¸æ¯ payload åé¡ï¼
            logging.error(f"â TG API {r.status_code}: {r.text[:200]}")
            return None

        except Exception as e:
            last_err = str(e)
            wait = 2 ** attempt
            logging.warning(
                f"â³ TG ç¼éå¤±æï¼åè©¦ {attempt + 1}/{max_retries}ï¼ï¼{e}ï¼{wait}s å¾éè©¦"
            )
            time.sleep(wait)

    logging.error(f"â TG ç¼éå¤±æï¼{max_retries} æ¬¡éè©¦å¾ä»å¤±æï¼ï¼{last_err}")
    return None


def _order_keyboard(order_id: str) -> dict:
    """ð çæè¨å®æ¥è©¢æéï¼LINE é¢¨æ ¼ï¼"""
    return {
        "inline_keyboard": [
            [
                {
                    "text": f"ð æ¥è©¢è¨å® {order_id[-8:]}",
                    "callback_data": f"order_{order_id}",
                }
            ]
        ]
    }


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 2.5 v14.1 åä½å»ºè­° + åæ¸ç´°é æ ¼å¼å
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def suggest_position_size(score: int, cfg: dict | None = None) -> tuple[float, str]:
    """ð° æ ¹æåæ¸æ¨è¦åä½åæ¸"""
    if cfg is None:
        cfg = load_config()
    ps_cfg = cfg.get("position_sizing", {})
    if not ps_cfg.get("enabled", True):
        return 1.0, "æ¨æºå"
    tiers = ps_cfg.get("tiers", DEFAULT_CONFIG["position_sizing"]["tiers"])
    for tier in tiers:
        if score >= tier.get("min_score", 0):
            return tier.get("multiplier", 1.0), tier.get("label", "æ¨æºå")
    return 1.0, "æ¨æºå"


def calc_position_sizing(
    entry: float,
    sl: float,
    tp1: float,
    tp2: float,
    tp3: float,
    side: str,
    pos_multiplier: float = 1.0,
    cfg: dict | None = None,
) -> dict | None:
    """ðµ æ ¹æè³é / é¢¨éªä¸éç®æ§æ¡¿ãåä½ãå TP ç¾åæç

    éè¼¯ï¼
      effective_capital = base_capital Ã pos_multiplier
      effective_max_loss = base_max_loss Ã pos_multiplier  ï¼é¢¨éªæ¯ä¾ä¸è®ï¼
      leverage = (effective_max_loss / effective_capital) Ã· SLè·é¢
              = max_loss / capital Ã· SLè·é¢ï¼è multiplier ç¡éï¼
      position_value = effective_capital Ã leverage
    """
    if cfg is None:
        cfg = load_config()
    cm = cfg.get("capital_management", {})
    if not cm.get("enabled", True):
        return None

    base_cap = cm.get("capital_per_trade_usd", 100)
    base_max_loss = cm.get("max_loss_usd", 20)
    max_lev = cm.get("max_leverage", 50)
    min_lev = cm.get("min_leverage", 2)

    sl_dist_pct = abs(entry - sl) / entry
    if sl_dist_pct <= 0:
        return None

    # é¢¨éªæ¯ = æå¤± / è³éï¼ä¸æè¢« multiplier æ¹è®ï¼
    risk_ratio = base_max_loss / base_cap
    required_lev = risk_ratio / sl_dist_pct
    leverage = max(min_lev, min(max_lev, round(required_lev)))

    # ä¾ multiplier ç¸®æ¾å¯¦éè³éèå®¹å¿æå¤±
    capital = base_cap * pos_multiplier
    max_loss = base_max_loss * pos_multiplier

    position_value = capital * leverage
    contracts = position_value / entry

    def _pnl(target_price):
        if side == "LONG":
            return position_value * (target_price - entry) / entry
        return position_value * (entry - target_price) / entry

    return {
        "capital_usd": round(capital, 2),
        "max_loss_usd": round(max_loss, 2),
        "leverage": int(leverage),
        "position_value_usd": round(position_value, 2),
        "contracts": round(contracts, 4),
        "sl_loss_usd": round(abs(_pnl(sl)), 2),
        "tp1_profit_usd": round(_pnl(tp1), 2),
        "tp2_profit_usd": round(_pnl(tp2), 2),
        "tp3_profit_usd": round(_pnl(tp3), 2),
        "pos_multiplier": pos_multiplier,
    }


def _format_score_breakdown(detail: dict | None) -> str:
    """ð å¼·åçè©åç´°é """
    if not detail:
        return ""
    out = ["", "ð *è©åæç´°ï¼*"]
    trend_v=detail.get("trend",0); rsi_val=detail.get("rsi_value",0); rsi_v=detail.get("rsi",0)
    if trend_v==30: out.append("  ð è¶¨å¢ï¼`30/30` â Supertrend é å¢ï¼ä¸»æ¹åç¢ºèª")
    elif trend_v==15: out.append("  ð è¶¨å¢ï¼`15/30` â Supertrend ä¸­æ§")
    else: out.append("  ð è¶¨å¢ï¼`0/30` â ï¸ Supertrend éå¢")
    if rsi_v==25:
        lbl="è¶è³£åå" if rsi_val<50 else "è¶è²·åè½"
        out.append(f"  ð RSIï¼`25/25` â RSI {rsi_val:.1f}ï¼{lbl}")
    elif rsi_v==15: out.append(f"  ð RSIï¼`15/25` â RSI {rsi_val:.1f}ï¼ä¸­æ§åé")
    else: out.append(f"  ð RSIï¼`0/25` â RSI {rsi_val:.1f}ï¼ä¸å¨çæ³å")
    ob_v=detail.get("ob",0); ob_low=detail.get("ob_low"); ob_high=detail.get("ob_high")
    if ob_v==20 and ob_low and ob_high: out.append(f"  ð§± OBï¼`20/20` â æ©æ§è¨å®å¡ `{ob_low:.4f}â{ob_high:.4f}`")
    elif ob_v==20: out.append("  ð§± OBï¼`20/20` â è¨å®å¡ç¢ºèª")
    else: out.append("  ð§± OBï¼`0/20` â ç¡ææè¨å®å¡")
    fvg_v=detail.get("fvg",0); fvg_low=detail.get("fvg_low"); fvg_high=detail.get("fvg_high")
    if fvg_v==15 and fvg_low and fvg_high: out.append(f"  â¡ FVGï¼`15/15` â å¬åç¼ºå£ `{fvg_low:.4f}â{fvg_high:.4f}`")
    elif fvg_v==15: out.append("  â¡ FVGï¼`15/15` â FVG å±æ¯")
    else: out.append("  â¡ FVGï¼`0/15` â ç¡ FVG")
    extras=[]
    if detail.get("snr"): extras.append("SNR â")
    if detail.get("pa"): extras.append("Kç·åæ â")
    if detail.get("liq"): extras.append("æµåæ§æè© â")
    if detail.get("mom"): extras.append("åè½ â")
    out.append("  ð éå ï¼"+(" | ".join(extras) if extras else "åæªè§¸ç¼"))
    if "mtf" in detail:
        mtf_v=detail["mtf"]; mtf_d=detail.get("mtf_desc",""); sign="+" if mtf_v>=0 else ""
        color="ð¢ å®ç¾" if mtf_v>=13 else "ð¡ é¨å" if mtf_v>=5 else "ð´ éæ¡" if mtf_v<0 else "âª å¾®å¼±"
        out.append(f"  ð MTF ({mtf_d})ï¼`{sign}{mtf_v}` {color}")
    if "volume" in detail:
        vol_v=detail["volume"]; vol_r=detail.get("volume_ratio",0); sign="+" if vol_v>=0 else ""
        out.append(f"  ð éè½ï¼`{sign}{vol_v}` â {vol_r}Ãåé")
    regime=detail.get("regime"); adx=detail.get("adx")
    if regime and adx:
        rm={"trend":"è¶¨å¢è¡æ","range":"éçªè¡æ","transitional":"éæ¸¡æ"}
        out.append(f"  ð å¸å ´ï¼{rm.get(regime,regime)}ï¼ADX `{adx:.1f}`ï¼")
    return "\n".join(out)


def _fmt_analysis_narrative(detail: dict | None, side: str, score: int) -> str:
    """ð çºä»éº¼é²å ´ â ç½è©±æåææ®µè½ï¼æ°¸é é¡¯ç¤ºï¼"""
    if not detail:
        return ""
    reasons=[]; warnings=[]
    rsi_val=detail.get("rsi_value",50); trend_v=detail.get("trend",0)
    if trend_v==30: reasons.append("Supertrend 15m é å¢ç¢ºèªï¼ä¸»æ¹åæç¢º")
    elif trend_v==15: warnings.append("Supertrend ä¸­æ§ï¼ç¡æç¢ºè¶¨å¢æ¹å")
    else: warnings.append("â ï¸ Supertrend éå¢ï¼å±¬éå¸æä½")
    rsi_v=detail.get("rsi",0)
    if rsi_v==25:
        if side=="LONG": reasons.append(f"RSI {rsi_val:.0f} å¾è¶è³£åååï¼å¤æ¹åè½åè½æ­£")
        else: reasons.append(f"RSI {rsi_val:.0f} å¾è¶è²·ååè½ï¼ç©ºæ¹åè½ä¸»å°")
    elif rsi_v==15: reasons.append(f"RSI {rsi_val:.0f} ä¸­æ§åéï¼æ¹åå¯è¡ä½éæä½³é»")
    else:
        if rsi_val>=70: warnings.append(f"â ï¸ RSI {rsi_val:.0f} è¶è²·ï¼è¿½å¤é¢¨éªé«")
        elif rsi_val<30: warnings.append(f"â ï¸ RSI {rsi_val:.0f} è¶è³£ä½åè½æªè½å")
    smc=[]
    if detail.get("ob",0)==20:
        ol=detail.get("ob_low"); oh=detail.get("ob_high")
        smc.append(f"OBæ©æ§å¡ {ol:.4f}â{oh:.4f}" if ol and oh else "OBæ©æ§è¨å®å¡ç¢ºèª")
    if detail.get("fvg",0)==15:
        fl=detail.get("fvg_low"); fh=detail.get("fvg_high")
        smc.append(f"FVGç¼ºå£ {fl:.4f}â{fh:.4f}" if fl and fh else "FVGå¬åç¼ºå£å±æ¯")
    if detail.get("liq"): smc.append("æµåæ§æè©å®æ")
    if smc: reasons.append("SMCï¼"+"ã".join(smc))
    if "mtf" in detail:
        mtf_v=detail["mtf"]; mtf_d=detail.get("mtf_desc","")
        if mtf_v>=13: reasons.append(f"ä¸ææ¡ï¼{mtf_d}ï¼å®ç¾å±æ¯ï¼å¤§æ¹åä¸è´")
        elif mtf_v>=5: reasons.append(f"MTF é¨åå±æ¯ï¼{mtf_d}ï¼ï¼å¤§æ¡æ¶æ¯æ")
        elif mtf_v<0: warnings.append(f"â ï¸ MTF éæ¡ï¼{mtf_d}ï¼ï¼å¤§é±ææ¹åç¸å")
    vol_v=detail.get("volume",0); vol_r=detail.get("volume_ratio",0)
    if vol_v>0 and vol_r>=1.5: reasons.append(f"éè½ {vol_r:.1f}Ãåéæ¾å¤§ï¼è³éæµå¥ä½è­")
    elif vol_v<0: warnings.append(f"éè½ {vol_r:.1f}Ãåå¼±ï¼æ³¨æåçªç ´")
    if detail.get("pa"): reasons.append("Kç·åæç¢ºèªï¼éå­/åå¬/éåï¼")
    regime=detail.get("regime"); adx=detail.get("adx",0)
    if regime=="range": warnings.append(f"å¸å ´éçªï¼ADX {adx:.0f}ï¼ï¼æ³¨æåçªç ´")
    elif regime=="trend": reasons.append(f"ADX {adx:.0f} è¶¨å¢è¡æï¼è·å¢åçè¼é«")
    if not reasons and not warnings: return ""
    out=["\nð *çºä»éº¼é²å ´ï¼*"]
    for r in reasons[:5]: out.append(f"  â {r}")
    for w in warnings[:3]: out.append(f"  ð© {w}")
    return "\n".join(out)


def _fmt_entry(
    coin: str,
    side: str,
    order_id: str,
    price: float,
    entry: float,
    sl: float,
    tp1: float,
    tp2: float,
    tp3: float,
    score: int,
    funding_rate: float | None = None,
    detail: dict | None = None,
) -> str:
    """ð é²å ´éç¥ï¼å«åæ¸ç´°é  + åä½å»ºè­°ï¼"""
    direction = "åå¤" if side == "LONG" else "åç©º"
    emoji = "ð¢" if side == "LONG" else "ð´"

    # ð¯ ç¥ç´è¨èç¹å¥æ¨è¨
    cfg_god = load_config().get("god_signal", {})
    god_threshold = cfg_god.get("min_score", 95)
    is_god = cfg_god.get("enabled", True) and score >= god_threshold

    if is_god:
        grade = "ð¯ð¯ð¯ *ç¥ç´è¨è* ð¯ð¯ð¯"
    elif score >= 85:
        grade = "ð¥ A+ æ¥µå¼·"
    elif score >= 70:
        grade = "â­ A å¼·å"
    else:
        grade = "â B+ åæ ¼"

    tp1_pct = (tp1 - entry) / entry * 100 * (1 if side == "LONG" else -1)
    tp2_pct = (tp2 - entry) / entry * 100 * (1 if side == "LONG" else -1)
    tp3_pct = (tp3 - entry) / entry * 100 * (1 if side == "LONG" else -1)
    sl_pct = (sl - entry) / entry * 100  # å¸¶æ­£è² è

    funding_line = ""
    if funding_rate is not None:
        funding_line = f"ð° è³éè²»çï¼`{funding_rate * 100:+.4f}%`\n"

    # åä½å»ºè­°
    cfg = load_config()
    pos_mult, pos_label = suggest_position_size(score, cfg)
    pos_line = f"ð¼ å»ºè­°åä½ï¼`{pos_mult}x` ({pos_label})\n"

    # ðµ åä½ / æ§æ¡¿ / æçè©¦ç®
    sizing = calc_position_sizing(entry, sl, tp1, tp2, tp3, side, pos_mult, cfg)
    sizing_block = ""
    if sizing:
        sizing_block = (
            f"\n"
            f"ðµ *è³éè©¦ç®ï¼è³é `${sizing['capital_usd']}` / é¢¨éª `${sizing['max_loss_usd']}`ï¼*\n"
            f"  æ§æ¡¿ï¼`{sizing['leverage']}x`\n"
            f"  åç®åä½ï¼`${sizing['position_value_usd']:,.0f}`\n"
            f"  æ¸éï¼`{sizing['contracts']:,.4f} {coin}`\n"
            f"  ð æ­¢ææå¤±ï¼`-${sizing['sl_loss_usd']:.2f}`\n"
            f"  ð¥ TP1 ç²å©ï¼`+${sizing['tp1_profit_usd']:.2f}`\n"
            f"  ð¥ TP2 ç²å©ï¼`+${sizing['tp2_profit_usd']:.2f}`\n"
            f"  ð TP3 ç²å©ï¼`+${sizing['tp3_profit_usd']:.2f}`\n"
        )

    # R:R é¡¯ç¤ºï¼TP1 å¯¦éåæ¸ï¼
    risk = abs(entry - sl)
    tp1_r = abs(tp1 - entry) / risk if risk > 0 else 0
    tp2_r = abs(tp2 - entry) / risk if risk > 0 else 0
    tp3_r = abs(tp3 - entry) / risk if risk > 0 else 0

    # â åæè§£èªªæ®µè½ï¼æ°¸é é¡¯ç¤ºï¼
    # ★ 限價成交標記
    _entry_diff_pct = (entry - price) / price * 100
    if abs(_entry_diff_pct) > 0.05:
        _fill_arrow = "📉" if side == "LONG" else "📈"
        limit_note = f"{_fill_arrow} *限價成交* \u2014 較掛單時市價 `{_entry_diff_pct:+.2f}%`\n"
    else:
        limit_note = ""

    narrative_block = _fmt_analysis_narrative(detail, side, score)

    # åæ¸ç´°é ï¼é è¨­ééï¼
    breakdown = ""
    if cfg.get("show_score_breakdown", False):
        breakdown = _format_score_breakdown(detail)

    return (
        f"{emoji} *{coin} é²å ´æé* {grade}\n"
        f"ââââââââââââââ\n"
        f"ð è¨å®ç·¨èï¼`{order_id}`\n"
        f"â° æéï¼{tw_ts()}\n"
        f"æ¹åï¼{direction}\n"
        f"é²å ´å¹ï¼`{entry:.4f}`\n"
        f"ç¶åå¹ï¼`{price:.4f}`\n"
        f"è©åï¼*{score} å*\n"
        f"{pos_line}"
        f"{funding_line}"
        f"{sizing_block}"
        f"{limit_note}"
        f"{narrative_block}\n"
        f"{breakdown}\n"
        f"\n"
        f"ð¯ æ­¢çç®æ¨ï¼\n"
        f"  TP1 `{tp1:.4f}` ({tp1_pct:+.2f}% / `{tp1_r:.1f}R`)\n"
        f"  TP2 `{tp2:.4f}` ({tp2_pct:+.2f}% / `{tp2_r:.1f}R`)\n"
        f"  TP3 `{tp3:.4f}` ({tp3_pct:+.2f}% / `{tp3_r:.1f}R`)\n"
        f"\n"
        f"ð æ­¢æï¼`{sl:.4f}` ({sl_pct:+.2f}%)\n"
        f"\n"
        f"ð¡ å°é TP1 èªåä¿æ¬ï¼å°é TP2 èªåéå©è³ TP1"
    )


def _fmt_tp(
    coin: str,
    side: str,
    order_id: str,
    tp_level: str,
    price: float,
    pnl_pct: float,
    r_mult: float,
    wick_triggered: bool = False,
) -> str:
    """ð¯ æ­¢çéç¥"""
    direction = "åå¤" if side == "LONG" else "åç©º"
    advice = (
        "å»ºè­°å¹³å â éå®ç²å©"
        if tp_level == "TP1"
        else "å»ºè­°åå¹³å â è½è¢çºå®"
        if tp_level == "TP2"
        else "å»ºè­°å¨é¨å¹³åï¼å®ç¾æ¶å² ð"
    )
    wick_note = "\nðª¡ _æéè§¸ç¼ï¼K ç·æéè§¸åç®æ¨å¹ï¼_" if wick_triggered else ""
    return (
        f"ð¯ *{coin} {tp_level} éæ¨ï¼*\n"
        f"ââââââââââââââ\n"
        f"ð è¨å®ç·¨èï¼`{order_id}`\n"
        f"â° æéï¼{tw_ts()}\n"
        f"æ¹åï¼{direction}\n"
        f"è§¸ç¼å¹ï¼`{price:.4f}`{wick_note}\n"
        f"ç²å©ï¼`{pnl_pct:+.2f}%` (`{r_mult:+.1f}R`)\n"
        f"\n"
        f"â å·²éæ {tp_level}\n"
        f"\n"
        f"ð¡ {advice}"
    )


def _fmt_sl(
    coin: str,
    side: str,
    order_id: str,
    price: float,
    pnl_pct: float,
    mode: str = "LOSS",
    r_value: float = -1.0,
    wick_triggered: bool = False,
) -> str:
    """ð å¹³åéç¥ï¼ä¸æ¨¡å¼ï¼LOSS æ­¢æ / BE ä¿æ¬ / LOCK éå©ï¼"""
    direction = "åå¤" if side == "LONG" else "åç©º"
    if mode == "BE":
        label = "ð ä¿æ¬åºå ´"
        r_tag = "`0.0R`"
        advice = (
            "â¨ TP1 å·²éæï¼æ­¢æä¸ç§»è³é²å ´å¹\n"
            "æ¬ç­ç¡æåºå ´ï¼è³éå®æ´ä¿ç\n"
            "ð¡ ç­å¾ä¸ä¸åé«åçè¨è ðª"
        )
    elif mode == "LOCK":
        label = "ð éå©åºå ´"
        r_tag = f"`+{r_value:.1f}R`"
        advice = (
            "ð TP2 å·²éæï¼æ­¢æä¸ç§»è³ TP1\n"
            "è¶¨å¢åé ­æéä½ TP1 çç²å©åªééå ´\n"
            "ð¡ é¢¨æ§å®ç¾å·è¡ï¼ç¹¼çºä¿æ â¨"
        )
    else:
        label = "â æ­¢æé¢å ´"
        r_tag = "`-1.0R`"
        advice = "ð¡ éµå®é¢¨æ§ï¼å¿å ç¢¼æ¤å¹³ãä¸ä¸ç­è¨èææ´å¥½ ð"

    wick_note = "\nðª¡ _æéè§¸ç¼ï¼K ç·æéè§¸åå¹³åå¹ï¼_" if wick_triggered else ""
    return (
        f"{label} *{coin}*\n"
        f"ââââââââââââââ\n"
        f"ð è¨å®ç·¨èï¼`{order_id}`\n"
        f"â° æéï¼{tw_ts()}\n"
        f"æ¹åï¼{direction}\n"
        f"è§¸ç¼å¹ï¼`{price:.4f}`{wick_note}\n"
        f"çµæï¼`{pnl_pct:+.2f}%` {r_tag}\n"
        f"\n"
        f"{advice}"
    )


def _fmt_position(sig: dict, current_price: float) -> str:
    """ð æåé²åº¦æ´æ°"""
    coin = sig["instId"].split("-")[0]
    side = sig["side"]
    direction = "åå¤" if side == "LONG" else "åç©º"
    entry = sig["entry"]
    pnl = (
        (current_price - entry) / entry * 100
        if side == "LONG"
        else (entry - current_price) / entry * 100
    )
    pnl_emoji = "ð¢" if pnl >= 0 else "ð´"

    if sig.get("hit_tp3"):
        progress = "ð TP3 â"
    elif sig.get("hit_tp2"):
        progress = "ð¥â â ð¥â â â³ TP3"
    elif sig.get("hit_tp1"):
        progress = "ð¥â â â³ TP2"
    else:
        progress = "â³ ç­å¾ TP1"

    return (
        f"ð *{coin} æåæ´æ°*\n"
        f"ââââââââââââââ\n"
        f"ð è¨å®ç·¨èï¼`{sig.get('order_id', 'N/A')}`\n"
        f"â° æéï¼{tw_ts()}\n"
        f"æ¹åï¼{direction}\n"
        f"ç¶åï¼`{current_price:.4f}` {pnl_emoji}{pnl:+.2f}%\n"
        f"é²å ´ï¼`{entry:.4f}`\n"
        f"\n"
        f"ð¯ æ­¢çé²åº¦ï¼{progress}\n"
        f"  TP1 `{sig['tp1']:.4f}`{'â' if sig.get('hit_tp1') else ''}\n"
        f"  TP2 `{sig['tp2']:.4f}`{'â' if sig.get('hit_tp2') else ''}\n"
        f"  TP3 `{sig['tp3']:.4f}`{'â' if sig.get('hit_tp3') else ''}\n"
        f"\n"
        f"ð æ­¢æï¼`{sig['sl']:.4f}`"
    )


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 4. æ¸ææå
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def fetch_price(instId: str) -> float:
    """ð å³æå¹æ ¼ï¼5 ç§è¨æ¶é«å¿«åï¼"""
    now = time.time()
    if instId in _price_cache:
        price, t = _price_cache[instId]
        if now - t < 5:
            return price
    try:
        res = requests.get(
            f"https://www.okx.com/api/v5/market/ticker?instId={instId}",
            timeout=5,
        ).json()
        if res.get("code") == "0" and res.get("data"):
            price = float(res["data"][0]["last"])
            if price > 0:
                _price_cache[instId] = (price, now)
                return price
    except Exception as e:
        logging.warning(f"â ï¸ åå¾ {instId} å¹æ ¼å¤±æï¼{e}")
    return _price_cache.get(instId, (0.0, 0))[0]


def fetch_candles(instId: str, tf: str = "15m", limit: int = 100) -> list | None:
    """ð K ç·ï¼å·²æ¶ç·ï¼"""
    try:
        res = requests.get(
            f"https://www.okx.com/api/v5/market/candles?instId={instId}&bar={tf}&limit={limit}",
            timeout=6,
        ).json()
        if res.get("code") != "0":
            return None
        data = res.get("data", [])
        if len(data) < 30:
            return None
        # OKX ç¬¬ 9 æ¬ï¼index 8ï¼çº confirmï¼ååå·²æ¶ç·ï¼OKX é è¨­ç±æ°å°èï¼åè½æç±èå°æ°
        confirmed = [r for r in data if r[8] == "1"][::-1]
        return [
            {
                "ts": r[0],
                "o": float(r[1]),
                "h": float(r[2]),
                "l": float(r[3]),
                "c": float(r[4]),
                "v": float(r[5]),
            }
            for r in confirmed
        ]
    except Exception as e:
        logging.warning(f"â ï¸ åå¾ {instId} K ç·å¤±æï¼{e}")
        return None


_candle_full_cache: dict = {}


def fetch_candles_full(instId: str, tf: str = "15m", limit: int = 100) -> list:
    """ðª¡ ææè¿ N æ ¹ K ç·ï¼å«æªæ¶ç·ï¼ä¸¦ææéååºæåºï¼æ¯è¼ªææå±ç¨ 30 ç§å¿«å

    åå³æ¯ç­å«ï¼ts(ms æ´æ¸)ão/h/l/c/vãconfirmed(bool)
    ç¨æ¼ _check_one çãæ­·å²æéè£æãï¼
      - è¨èèª last_checked_ts ä¹å¾çææ K ç·é½æè¢«æé
      - å³ä½¿ cron æ¼è·ãè¨èéäº 3 å°æææª¢æ¥ï¼éå»ä»»ä½æéé½ä¸ææ¼
    """
    now = time.time()
    if instId in _candle_full_cache:
        candles, t = _candle_full_cache[instId]
        if now - t < 30:
            return candles
    try:
        res = requests.get(
            f"https://www.okx.com/api/v5/market/candles?instId={instId}&bar={tf}&limit={limit}",
            timeout=8,
        ).json()
        if res.get("code") != "0":
            return _candle_full_cache.get(instId, ([], 0))[0]
        data = res.get("data", [])
        candles = [
            {
                "ts": int(r[0]),
                "o": float(r[1]),
                "h": float(r[2]),
                "l": float(r[3]),
                "c": float(r[4]),
                "v": float(r[5]),
                "confirmed": r[8] == "1",
            }
            for r in data
        ]
        candles.sort(key=lambda x: x["ts"])
        _candle_full_cache[instId] = (candles, now)
        return candles
    except Exception as e:
        logging.warning(f"â ï¸ åå¾ {instId} å®æ´ K ç·å¤±æï¼{e}")
        return _candle_full_cache.get(instId, ([], 0))[0]


def fetch_recent_range(instId: str, bars: int = 2, tf: str = "15m") -> tuple[float, float] | None:
    """ðª¡ ææè¿ N æ ¹ K ç·ï¼å«æªæ¶ç·ï¼çæä½ / æé« â (low, high)

    ç¨éï¼åµæ¸¬æéï¼é¿åãå¿«éæ³å° SL/TP åç¸®åå»ãééè¿½è¹¤ã
    è fetch_candles ä¸åï¼éè£¡ä¸éæ¿¾ confirmï¼ææ­£å¨å½¢æç K ç·ä¹ç®é²å»ã
    """
    try:
        res = requests.get(
            f"https://www.okx.com/api/v5/market/candles?instId={instId}&bar={tf}&limit={bars}",
            timeout=5,
        ).json()
        if res.get("code") != "0":
            return None
        data = res.get("data", [])
        if not data:
            return None
        lows = [float(r[3]) for r in data]
        highs = [float(r[2]) for r in data]
        return min(lows), max(highs)
    except Exception as e:
        logging.warning(f"â ï¸ åå¾ {instId} æè¿åéå¤±æï¼{e}")
        return None


def fetch_funding_rate(instId: str) -> float | None:
    """ð° OKX è³éè²»çï¼æ°¸çºåç´ï¼"""
    try:
        res = requests.get(
            f"https://www.okx.com/api/v5/public/funding-rate?instId={instId}",
            timeout=5,
        ).json()
        if res.get("code") == "0" and res.get("data"):
            return float(res["data"][0]["fundingRate"])
    except Exception as e:
        logging.warning(f"â ï¸ åå¾ {instId} è³éè²»çå¤±æï¼{e}")
    return None


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 4.5 TradingView ç¬¬äºå¹æ ¼ä¾æºï¼é¢¨æ§ï¼
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
_tv_cache: dict = {}


def fetch_price_tv(instId: str) -> float | None:
    """ð¡ å¾ TradingView æåå³æå¹æ ¼ï¼OKX æ°¸çºåç´ï¼

    åå³ None ä»£è¡¨æä¸å°ï¼ç¶²è·¯ / å¥ä»¶æªå®è£ / ç¬¦èé¯èª¤ï¼
    """
    now = time.time()
    if instId in _tv_cache:
        price, t = _tv_cache[instId]
        if now - t < 10:
            return price

    try:
        # å¥ä»¶å¯è½æªå®è£ï¼ç´èªæ³æª¢æ¥ææ¬å°æ¸¬è©¦ï¼
        from tradingview_ta import TA_Handler, Interval  # type: ignore
    except ImportError:
        logging.warning("â ï¸ æªå®è£ tradingview_taï¼è·³é TV é©è­")
        return None

    try:
        # BTC-USDT-SWAP â BTCUSDT.Pï¼OKX æ°¸çºåç´å¨ TradingView çå½åï¼
        symbol = instId.replace("-USDT-SWAP", "USDT.P").replace("-", "")
        handler = TA_Handler(
            symbol=symbol,
            exchange="OKX",
            screener="crypto",
            interval=Interval.INTERVAL_1_MINUTE,
            timeout=8,
        )
        analysis = handler.get_analysis()
        price = float(analysis.indicators.get("close", 0) or 0)
        if price > 0:
            _tv_cache[instId] = (price, now)
            return price
    except Exception as e:
        logging.warning(f"â ï¸ TradingView åå¾ {instId} å¤±æï¼{e}")
    return None


def verify_price(
    instId: str,
    okx_price: float,
    max_dev_pct: float = 0.5,
    block_on_unverified: bool = False,
) -> tuple[bool, float | None, float]:
    """âï¸ éä¾æºå¹æ ¼é©è­ â (æ¯å¦éé, TV å¹æ ¼, åé¢ç¾åæ¯)

    block_on_unverified:
      True  â TV æä¸å°ä¹æè¨èï¼ä¿å®ï¼
      False â TV æä¸å°ç¶ä½ééï¼é¿åå®é»å¤±æææææè¨èï¼
    """
    tv_price = fetch_price_tv(instId)
    if tv_price is None:
        return (not block_on_unverified, None, 0.0)
    diff_pct = abs(okx_price - tv_price) / okx_price * 100
    if diff_pct > max_dev_pct:
        logging.warning(
            f"ð¨ {instId} å¹æ ¼ä¸ä¸è´ï¼OKX={okx_price:.4f} TV={tv_price:.4f} "
            f"diff={diff_pct:.3f}% > {max_dev_pct}%"
        )
        return (False, tv_price, diff_pct)
    logging.info(
        f"â {instId} å¹æ ¼é©è­ééï¼OKX={okx_price:.4f} TV={tv_price:.4f} "
        f"diff={diff_pct:.3f}%"
    )
    return (True, tv_price, diff_pct)


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 5. åºç¤æè¡ææ¨
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def calc_atr(df: list, period: int = 14) -> float:
    """ATRï¼ç°¡ååå¼çæ¬ï¼"""
    if len(df) < period + 1:
        return 0.001
    trs = []
    for i in range(1, len(df)):
        hl = df[i]["h"] - df[i]["l"]
        hc = abs(df[i]["h"] - df[i - 1]["c"])
        lc = abs(df[i]["l"] - df[i - 1]["c"])
        trs.append(max(hl, hc, lc))
    if len(trs) < period:
        return 0.001
    atr = sum(trs[-period:]) / period
    return atr if atr > 0 else 0.001


def calc_supertrend(df: list, period: int = 10, mult: float = 3.0) -> int:
    """è¶¨å¢æ¹åï¼1=å¤é ­ / -1=ç©ºé ­ / 0=éçªï¼ç°¡åçæ¬ï¼"""
    if len(df) < period + 2:
        return 0
    atr = calc_atr(df, period)
    mid = sum(r["c"] for r in df[-20:]) / 20
    cur = df[-1]["c"]
    band = atr * 0.5
    if cur > mid + band:
        return 1
    if cur < mid - band:
        return -1
    return 0


def calc_rsi(df: list, period: int = 14) -> float:
    """RSIï¼Wilder ç°¡åçï¼"""
    if len(df) < period + 1:
        return 50.0
    gains, losses = [], []
    for i in range(1, len(df)):
        ch = df[i]["c"] - df[i - 1]["c"]
        gains.append(ch if ch > 0 else 0)
        losses.append(-ch if ch < 0 else 0)
    if len(gains) < period:
        return 50.0
    avg_g = sum(gains[-period:]) / period
    avg_l = sum(losses[-period:]) / period
    if avg_l == 0:
        return 100.0
    rs = avg_g / avg_l
    return 100 - (100 / (1 + rs))


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 6. SMC / ICT / SNR / å¹æ ¼è¡çº / æµåæ§ / åè½
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def find_order_block(df: list, side: str, lookback: int = 30) -> dict | None:
    """ð§± è¨å®å¡ï¼OBï¼

    çæ¼² OBï¼æè¿çé°ç·å¾ç·æ¥é½ç·çªç ´å¶é«é»ã
    çè· OBï¼æè¿çé½ç·å¾ç·æ¥é°ç·è·ç ´å¶ä½é»ã
    """
    n = len(df)
    if n < lookback + 5:
        return None
    start = max(0, n - lookback)
    if side == "LONG":
        for i in range(n - 4, start, -1):
            if df[i]["c"] < df[i]["o"]:  # é°ç·
                for j in range(i + 1, min(i + 4, n)):
                    if df[j]["c"] > df[i]["h"]:
                        return {"low": df[i]["l"], "high": df[i]["h"]}
    else:
        for i in range(n - 4, start, -1):
            if df[i]["c"] > df[i]["o"]:  # é½ç·
                for j in range(i + 1, min(i + 4, n)):
                    if df[j]["c"] < df[i]["l"]:
                        return {"low": df[i]["l"], "high": df[i]["h"]}
    return None


def find_fvg(df: list, side: str, lookback: int = 30) -> dict | None:
    """â¡ å¬åå¹å¼ç¼ºå£ï¼FVGï¼

    çæ¼² FVGï¼K[i].low > K[i-2].highã
    çè· FVGï¼K[i].high < K[i-2].lowã
    """
    n = len(df)
    if n < 4:
        return None
    start = max(2, n - lookback)
    for i in range(n - 1, start, -1):
        if side == "LONG":
            if df[i]["l"] > df[i - 2]["h"]:
                return {"low": df[i - 2]["h"], "high": df[i]["l"]}
        else:
            if df[i]["h"] < df[i - 2]["l"]:
                return {"low": df[i]["h"], "high": df[i - 2]["l"]}
    return None


def calc_snr(df: list, lookback: int = 100) -> tuple[float, float]:
    """ð åææ¯æ / é»åï¼è¿ N æ ¹æ¥µå¼ï¼"""
    seg = df[-lookback:] if len(df) >= lookback else df
    high = max(r["h"] for r in seg)
    low = min(r["l"] for r in seg)
    return low, high


def detect_price_action(df: list, side: str) -> bool:
    """ð åµæ¸¬ Pin Bar æåæ²å½¢æï¼æ¹åéèäº¤ææ¹åä¸è´"""
    if len(df) < 2:
        return False
    last, prev = df[-1], df[-2]
    body = abs(last["c"] - last["o"])
    upper = last["h"] - max(last["c"], last["o"])
    lower = min(last["c"], last["o"]) - last["l"]

    # Pin Barï¼å½±ç· â¥ 2 åå¯¦é«ï¼
    if body > 0:
        if side == "LONG" and lower > body * 2 and lower > upper:
            return True
        if side == "SHORT" and upper > body * 2 and upper > lower:
            return True

    # åæ²å½¢æ
    if side == "LONG":
        if (
            prev["c"] < prev["o"]
            and last["c"] > last["o"]
            and last["c"] > prev["o"]
            and last["o"] < prev["c"]
        ):
            return True
    else:
        if (
            prev["c"] > prev["o"]
            and last["c"] < last["o"]
            and last["c"] < prev["o"]
            and last["o"] > prev["c"]
        ):
            return True
    return False


def detect_liquidity_sweep(df: list, side: str, lookback: int = 20) -> bool:
    """ð§ æµåæ§æè©

    å¤é ­æè©ï¼æå¾ä¸æ ¹åµ N ææ°ä½å¾å¿«éæ¶åï¼æ¶ç¤åå°åéä¸­ä½ä»¥ä¸ï¼ã
    ç©ºé ­æè©ï¼æå¾ä¸æ ¹åµ N ææ°é«å¾å¿«éåè½ã
    """
    if len(df) < lookback + 1:
        return False
    seg = df[-(lookback + 1) : -1]
    last = df[-1]
    prev_low = min(r["l"] for r in seg)
    prev_high = max(r["h"] for r in seg)
    mid = (prev_low + prev_high) / 2

    if side == "LONG":
        return last["l"] < prev_low and last["c"] > mid
    return last["h"] > prev_high and last["c"] < mid


def calc_momentum_ratio(df: list, side: str, n: int = 5) -> bool:
    """ð ç¤å£åè½ï¼æè¿ N æ ¹ K ç·å¤ç©ºæ¯ä¾"""
    seg = df[-n:]
    bull = sum(1 for r in seg if r["c"] > r["o"])
    ratio = bull / max(1, len(seg))
    return ratio >= 0.6 if side == "LONG" else ratio <= 0.4


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 6.4 v14.2 EMA å¤é±ææå
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def calc_ema(df: list, period: int) -> float:
    """EMA è¨ç®ï¼ç¨®å­ç¨ SMAï¼"""
    if len(df) < period:
        return df[-1]["c"] if df else 0.0
    closes = [c["c"] for c in df]
    multiplier = 2.0 / (period + 1)
    ema = sum(closes[:period]) / period
    for c in closes[period:]:
        ema = c * multiplier + ema * (1 - multiplier)
    return ema


def calc_ema_alignment(df: list, side: str, cfg: dict | None = None) -> tuple[int, str]:
    """ðª EMA å¤é±ææåè©å â (åæ¸ -5~+5, æè¿°)

    å¤é ­å®ç¾æåï¼å¹æ ¼ > EMA20 > EMA50 > EMA200
    ç©ºé ­å®ç¾æåï¼å¹æ ¼ < EMA20 < EMA50 < EMA200
    """
    if cfg is None:
        cfg = load_config()
    ec = cfg.get("ema_alignment", {})
    if not ec.get("enabled", True):
        return 0, ""
    periods = ec.get("periods", [20, 50, 200])
    if len(df) < max(periods) + 5:
        return 0, "EMA è³æä¸è¶³"

    p_short, p_mid, p_long = periods[0], periods[1], periods[2]
    ema_s = calc_ema(df, p_short)
    ema_m = calc_ema(df, p_mid)
    ema_l = calc_ema(df, p_long)
    price = df[-1]["c"]

    if side == "LONG":
        if price > ema_s > ema_m > ema_l:
            return ec.get("perfect_bonus", 5), f"å¤é ­å®ç¾æåï¼å¹>{p_short}>{p_mid}>{p_long}ï¼"
        if price > ema_s > ema_m:
            return ec.get("partial_bonus", 3), "ç­ä¸­æå¤é ­"
        if price < ema_l:
            return -ec.get("against_penalty", 5), "å¨ EMA200 ä¹ä¸ï¼éå¤§è¶¨å¢"
    else:
        if price < ema_s < ema_m < ema_l:
            return ec.get("perfect_bonus", 5), f"ç©ºé ­å®ç¾æåï¼å¹<{p_short}<{p_mid}<{p_long}ï¼"
        if price < ema_s < ema_m:
            return ec.get("partial_bonus", 3), "ç­ä¸­æç©ºé ­"
        if price > ema_l:
            return -ec.get("against_penalty", 5), "å¨ EMA200 ä¹ä¸ï¼éå¤§è¶¨å¢"
    return 0, "EMA æªæç¢ºæå"


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 6.5 v14 æ°ææ¨ï¼ADX / å¤ææ¡ / éè½ / å¸å ´çæ / é²å ´ææ©
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def calc_adx(df: list, period: int = 14) -> float:
    """ð ADX è¶¨å¢å¼·åº¦ï¼>25 å¼·è¶¨å¢ã<18 éçªãä¸­ééæ¸¡"""
    if len(df) < period * 2 + 1:
        return 0.0
    plus_dm, minus_dm, trs = [], [], []
    for i in range(1, len(df)):
        up = df[i]["h"] - df[i - 1]["h"]
        dn = df[i - 1]["l"] - df[i]["l"]
        plus_dm.append(up if (up > dn and up > 0) else 0)
        minus_dm.append(dn if (dn > up and dn > 0) else 0)
        tr = max(
            df[i]["h"] - df[i]["l"],
            abs(df[i]["h"] - df[i - 1]["c"]),
            abs(df[i]["l"] - df[i - 1]["c"]),
        )
        trs.append(tr)
    if len(trs) < period:
        return 0.0
    atr = sum(trs[-period:]) / period
    if atr == 0:
        return 0.0
    plus_di = 100 * sum(plus_dm[-period:]) / period / atr
    minus_di = 100 * sum(minus_dm[-period:]) / period / atr
    s = plus_di + minus_di
    if s == 0:
        return 0.0
    return 100 * abs(plus_di - minus_di) / s


def detect_market_regime(df: list) -> dict:
    """ð å¤æ·å¸å ´çæï¼trend / range / transitional + æ¯å¦é«æ³¢å"""
    adx = calc_adx(df)
    atr = calc_atr(df)
    price = df[-1]["c"] if df else 1
    atr_pct = atr / price * 100 if price else 0
    if adx > 25:
        regime = "trend"
    elif adx < 18:
        regime = "range"
    else:
        regime = "transitional"
    return {
        "regime": regime,
        "adx": round(adx, 1),
        "atr_pct": round(atr_pct, 3),
        "volatile": atr_pct > 2.5,
    }


_mtf_cache: dict = {}


def fetch_mtf_trend(instId: str) -> dict:
    """ð æ 1H è 4H ç K ç·å¤æ·å¤§è¶¨å¢ï¼30 ç§å¿«åï¼"""
    now = time.time()
    if instId in _mtf_cache:
        data, t = _mtf_cache[instId]
        if now - t < 30:
            return data
    out = {}
    for tf in ("1H", "4H"):
        df = fetch_candles(instId, tf=tf, limit=50)
        if df:
            st = calc_supertrend(df)
            out[tf] = {
                "supertrend": st,
                "trend": "up" if st == 1 else "down" if st == -1 else "side",
                "rsi": round(calc_rsi(df), 1),
            }
        else:
            out[tf] = {"supertrend": 0, "trend": "side", "rsi": 50}
    _mtf_cache[instId] = (out, now)
    return out


def calc_mtf_alignment(mtf: dict, side: str) -> tuple[int, str]:
    """ð¯ å¤ææ¡å±æ¯è©åï¼æé« +15ï¼â (åæ¸, èªªæ)"""
    expect = 1 if side == "LONG" else -1
    h1 = mtf.get("1H", {}).get("supertrend", 0)
    h4 = mtf.get("4H", {}).get("supertrend", 0)
    score = 0
    if h1 == expect:
        score += 8
    elif h1 == -expect:
        score -= 5
    if h4 == expect:
        score += 7
    elif h4 == -expect:
        score -= 5
    score = max(-15, min(15, score))

    align_desc = []
    align_desc.append(f"1H={'é ' if h1 == expect else 'å' if h1 == -expect else 'ä¸­'}")
    align_desc.append(f"4H={'é ' if h4 == expect else 'å' if h4 == -expect else 'ä¸­'}")
    return score, " / ".join(align_desc)


def calc_volume_quality(df: list, lookback: int = 20) -> tuple[float, int]:
    """ð æäº¤éç¢ºèªï¼æå¾ K ç·é vs å N æåé â (åæ¸, è©å -10~+8)"""
    if len(df) < lookback + 1:
        return 1.0, 0
    seg = df[-(lookback + 1):-1]
    avg = sum(c["v"] for c in seg) / lookback
    if avg <= 0:
        return 1.0, 0
    ratio = df[-1]["v"] / avg
    if ratio >= 2.0:
        s = 8
    elif ratio >= 1.5:
        s = 5
    elif ratio >= 1.0:
        s = 2
    elif ratio >= 0.5:
        s = 0
    else:
        s = -10  # æ²éçè¨èç´æ¥æ£ï¼éæ¿¾åçªç ´
    return round(ratio, 2), s


def adjust_tp_by_sr(
    entry: float, side: str, tp_levels: list, df: list
) -> tuple[list, list]:
    """ð¯ åæ TPï¼è¥åºå® R å TP è½å¨å¼· S/R åæ¹ï¼æ TP æå°ééµä½å

    â ï¸ ä¿®å¾© v14.4 collapse bugï¼æ ¡æ­£å¾è¥ TP é åºäºæï¼TP3 â¤ TP2ï¼ï¼
       èªååå¾©åå¼æå¼·å¶ä¿çæå°éè·ï¼ç¢ºä¿ TP1 < TP2 < TP3ï¼LONGï¼/
       TP1 > TP2 > TP3ï¼SHORTï¼

    åå³ï¼(èª¿æ´å¾ TP åè¡¨, èª¿æ´ç´é)
    """
    sup, res = calc_snr(df, lookback=100)
    out = list(tp_levels)
    notes = []

    if side == "LONG":
        ceiling = res * 0.998
        for i, tp in enumerate(out):
            if tp > res * 1.001 and ceiling > entry:
                notes.append(
                    f"TP{i + 1} ç± {tp:.4f} æ ¡æ­£å° {ceiling:.4f}ï¼é¿éé»å {res:.4f}ï¼"
                )
                out[i] = ceiling
        # å¼·å¶ TP1 < TP2 < TP3ï¼è¥æ ¡æ­£å¾éçï¼åå¾©åå¼
        for i in range(1, len(out)):
            if out[i] <= out[i - 1]:
                if tp_levels[i] > out[i - 1]:
                    notes.append(
                        f"TP{i + 1} æ ¡æ­£å¾ â¤ TP{i}ï¼åå¾©åå¼ {tp_levels[i]:.4f}"
                    )
                    out[i] = tp_levels[i]
                else:
                    out[i] = out[i - 1] * 1.001
                    notes.append(f"TP{i + 1} å¼·å¶ +0.1% ç¶­æé åº")
    else:
        floor = sup * 1.002
        for i, tp in enumerate(out):
            if tp < sup * 0.999 and floor < entry:
                notes.append(
                    f"TP{i + 1} ç± {tp:.4f} æ ¡æ­£å° {floor:.4f}ï¼é¿éæ¯æ {sup:.4f}ï¼"
                )
                out[i] = floor
        # å¼·å¶ TP1 > TP2 > TP3
        for i in range(1, len(out)):
            if out[i] >= out[i - 1]:
                if tp_levels[i] < out[i - 1]:
                    notes.append(
                        f"TP{i + 1} æ ¡æ­£å¾ â¥ TP{i}ï¼åå¾©åå¼ {tp_levels[i]:.4f}"
                    )
                    out[i] = tp_levels[i]
                else:
                    out[i] = out[i - 1] * 0.999
                    notes.append(f"TP{i + 1} å¼·å¶ -0.1% ç¶­æé åº")

    return out, notes


def calc_vwap(df: list, lookback: int = 20) -> float:
    """ðª VWAP éå æ¬åå¹ï¼å¸å HLC/3 Ã Volume / sum(V)ï¼"""
    if not df:
        return 0.0
    seg = df[-lookback:] if len(df) >= lookback else df
    total_pv = sum((c["h"] + c["l"] + c["c"]) / 3 * c["v"] for c in seg)
    total_v = sum(c["v"] for c in seg)
    return total_pv / total_v if total_v > 0 else seg[-1]["c"]


def calc_vwap_score(df: list, side: str, lookback: int = 20) -> tuple[int, str]:
    """ðª VWAP åé¢è©å â (-3 ~ +3, æè¿°)

    å¤å®ï¼å¹å¨ VWAP ä¸æ¹ = å¤é ­å¼·å¢ +3
    ç©ºå®ï¼å¹å¨ VWAP ä¸æ¹ = ç©ºé ­å¼·å¢ +3
    éå¢ææ£å
    """
    if len(df) < 5:
        return 0, ""
    vwap = calc_vwap(df, lookback)
    price = df[-1]["c"]
    if vwap <= 0:
        return 0, ""
    dist_pct = (price - vwap) / vwap * 100

    if side == "LONG":
        if dist_pct > 0.3:
            return 3, f"å¹æ¼ VWAP ä¸æ¹ {dist_pct:.2f}%"
        if dist_pct > 0:
            return 1, "å¹ç¥é«æ¼ VWAP"
        if dist_pct < -0.3:
            return -3, f"å¹æ¼ VWAP ä¸æ¹ {abs(dist_pct):.2f}% å¤é ­å¼±å¢"
        return 0, "å¹æ¥è¿ VWAP"
    else:
        if dist_pct < -0.3:
            return 3, f"å¹æ¼ VWAP ä¸æ¹ {abs(dist_pct):.2f}%"
        if dist_pct < 0:
            return 1, "å¹ç¥ä½æ¼ VWAP"
        if dist_pct > 0.3:
            return -3, f"å¹æ¼ VWAP ä¸æ¹ {dist_pct:.2f}% ç©ºé ­å¼±å¢"
        return 0, "å¹æ¥è¿ VWAP"


def detect_pullback(df: list, side: str) -> bool:
    """ð åµæ¸¬åæ¸¬é²å ´ï¼æå¾ä¸æ ¹ K åºç¾æ¹ååè½å½±ç· + æ¶ç·åå"""
    if len(df) < 3:
        return False
    last = df[-1]
    body = abs(last["c"] - last["o"])
    if body == 0:
        return False
    upper = last["h"] - max(last["c"], last["o"])
    lower = min(last["c"], last["o"]) - last["l"]
    if side == "LONG":
        return lower > body * 1.2 and last["c"] > last["o"]
    return upper > body * 1.2 and last["c"] < last["o"]


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 7. è©åç³»çµ±ï¼è¦æ ¼ 100 åå¶ï¼
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def calc_score(
    df: list,
    side: str,
    current_price: float,
    mtf: dict | None = None,
    instId: str | None = None,
) -> tuple[int, str, dict]:
    """ç¸½å = è¶¨å¢30 + RSI25 + OB20 + FVG15 + SNR5 + PA5 + æµåæ§5 + åè½5 + MTF15 + Volume8 = æé« 138
    ï¼é«æ¼ 100 æ¯å çº v14 æ°å¢ MTF + Volume å æ¬ï¼éæª»ä»é è¨­ 68ï¼
    """
    detail = {}
    score = 0

    # è¶¨å¢ (30)
    st = calc_supertrend(df)
    if (side == "LONG" and st == 1) or (side == "SHORT" and st == -1):
        score += 30
        detail["trend"] = 30
    elif st == 0:
        score += 15
        detail["trend"] = 15
    else:
        detail["trend"] = 0

    # RSI (25)
    rsi = calc_rsi(df)
    detail["rsi_value"] = round(rsi, 1)
    if side == "LONG":
        if 30 <= rsi <= 50:
            score += 25
            detail["rsi"] = 25
        elif 50 < rsi < 70:
            score += 15
            detail["rsi"] = 15
        else:
            detail["rsi"] = 0
    else:
        if 50 <= rsi <= 70:
            score += 25
            detail["rsi"] = 25
        elif 30 < rsi < 50:
            score += 15
            detail["rsi"] = 15
        else:
            detail["rsi"] = 0

    # OB (20)
    ob = find_order_block(df, side)
    if ob and ob["low"] * 0.995 <= current_price <= ob["high"] * 1.005:
        score += 20
        detail["ob"] = 20
        detail["ob_low"]  = ob["low"]
        detail["ob_high"] = ob["high"]
    else:
        detail["ob"] = 0

    # FVG (15)
    fvg = find_fvg(df, side)
    if fvg and fvg["low"] * 0.997 <= current_price <= fvg["high"] * 1.003:
        score += 15
        detail["fvg"] = 15
        detail["fvg_low"]  = fvg["low"]
        detail["fvg_high"] = fvg["high"]
    else:
        detail["fvg"] = 0

    # SNR (5)
    sup, res = calc_snr(df)
    if side == "LONG" and current_price <= sup * 1.01:
        score += 5
        detail["snr"] = 5
    elif side == "SHORT" and current_price >= res * 0.99:
        score += 5
        detail["snr"] = 5
    else:
        detail["snr"] = 0

    # å¹æ ¼è¡çº (5)
    detail["pa"] = 5 if detect_price_action(df, side) else 0
    score += detail["pa"]

    # æµåæ§æè© (5)
    detail["liq"] = 5 if detect_liquidity_sweep(df, side) else 0
    score += detail["liq"]

    # åè½ (5)
    detail["mom"] = 5 if calc_momentum_ratio(df, side) else 0
    score += detail["mom"]

    # ð¯ MTF å¤ææ¡å±æ¯ (-15 ~ +15)
    if mtf is None and instId:
        mtf = fetch_mtf_trend(instId)
    if mtf:
        mtf_score, mtf_desc = calc_mtf_alignment(mtf, side)
        score += mtf_score
        detail["mtf"] = mtf_score
        detail["mtf_desc"] = mtf_desc

    # ð æäº¤é (-10 ~ +8)
    vol_ratio, vol_score = calc_volume_quality(df)
    score += vol_score
    detail["volume"] = vol_score
    detail["volume_ratio"] = vol_ratio

    # ðª EMA å¤é±ææå (-5 ~ +5)
    ema_score, ema_desc = calc_ema_alignment(df, side)
    score += ema_score
    detail["ema"] = ema_score
    detail["ema_desc"] = ema_desc

    # ðª VWAP åé¢ï¼èå¾è©åç¨ï¼ä¸é¡¯ç¤ºçµ¦ç¨æ¶ â _ åç¶´ï¼
    vwap_score, vwap_desc = calc_vwap_score(df, side)
    score += vwap_score
    detail["_vwap"] = vwap_score
    detail["_vwap_desc"] = vwap_desc

    # ð æ¹ååå¥½èª¿æ´ï¼å¾æ­·å²å­¸ç¿ï¼
    bias_dir, bias_amount, bias_note = get_direction_bias()
    if bias_dir:
        if bias_dir == side:
            score += bias_amount
            detail["direction_bias"] = bias_amount
            detail["direction_bias_note"] = bias_note
        elif bias_dir == ("SHORT" if side == "LONG" else "LONG"):
            score -= bias_amount
            detail["direction_bias"] = -bias_amount
            detail["direction_bias_note"] = bias_note

    grade = (
        "A+ æ¥µå¼· ð¥"
        if score >= 85
        else "A å¼·å â­"
        if score >= 70
        else "B+ åæ ¼ â"
        if score >= 68
        else "è§æ âª"
    )
    # ð å³å¥å¸å ´çæä¾æ ¼å¼å¨ä½¿ç¨
    regime_info = detect_market_regime(df)
    detail["regime"] = regime_info["regime"]
    detail["adx"]    = regime_info["adx"]

    return score, grade, detail


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 8. è¨èçæ
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def generate_signal(
    instId: str,
    df: list,
    current_price: float,
    funding_rate: float | None = None,
    score_threshold: int | None = None,
    atr_max_pct: float = 0.04,
    signal_expire_hours: int = SIGNAL_EXPIRE_HOURS,
) -> dict | None:
    """ð¯ çææä½³äº¤æè¨è"""
    if df is None or len(df) < 50:
        return None

    threshold = score_threshold if score_threshold is not None else SCORE_THRESHOLD

    atr = calc_atr(df)
    if atr / current_price > atr_max_pct:
        # æ³¢åéå¤§è·³éï¼æ­¢ææè¢«æé£ï¼
        return None

    # æ¥µç«¯è³éè²»çæéåéæ¿¾ï¼å¤é ­æè³éè²»çå¤ªé«ä»£è¡¨å¤æ¹ææ ï¼
    funding_penalty_long = funding_rate and funding_rate > 0.0008
    funding_penalty_short = funding_rate and funding_rate < -0.0008

    coin = instId.split("-")[0]

    # ð å¸å ´çæè­å¥ï¼è¶¨å¢/éçªï¼â å½±é¿éæª»
    regime_info = detect_market_regime(df)
    if regime_info["regime"] == "range":
        threshold += 5  # éçªå¸è¦æ±æ´å´æ ¼
    if regime_info["volatile"]:
        threshold += 3  # é«æ³¢åå ç¢¼æé«éæª»

    # ð å¤ææ¡æä¸æ¬¡çµ¦å©åæ¹åå±ç¨
    mtf = fetch_mtf_trend(instId)

    candidates = []
    for side in ("LONG", "SHORT"):
        score, grade, detail = calc_score(df, side, current_price, mtf=mtf)
        if side == "LONG" and funding_penalty_long:
            score -= 5
        if side == "SHORT" and funding_penalty_short:
            score -= 5

        # è¨»è¨å¸å ´çæå° detail
        detail["regime"] = regime_info["regime"]
        detail["adx"] = regime_info["adx"]
        detail["atr_pct"] = regime_info["atr_pct"]

        # ð é²å ´ææ©ï¼æåæ¸¬ K ç· +3 å
        if detect_pullback(df, side):
            score += 3
            detail["pullback"] = True

        # ð§  çµ±è¨å­¸ç¿ï¼æ¡¶ + KNN éè·¯ï¼
        adj_simple, notes_simple = apply_learning_adjustment(
            score, side, detail, funding_rate, coin
        )
        adj_knn, notes_knn = apply_knn_learning(
            score, side, detail, funding_rate, coin, mtf, regime_info
        )
        adjusted_score = adj_simple + (adj_knn - score)
        learning_notes = notes_simple + notes_knn
        if learning_notes:
            detail["learning_notes"] = learning_notes
            detail["learning_adjust"] = adjusted_score - score
        score = adjusted_score

        if score < threshold:
            continue

        # ── 限價進場：OB底 → FVG底 → 固定回調 0.3% ──
        _ob_h = detail.get("ob_high")
        _ob_l = detail.get("ob_low")
        _fvg_l = detail.get("fvg_low")
        _fvg_h = detail.get("fvg_high")
        _max_off = 0.015  # 最多離場 1.5%，避免掛太遠
        if side == "LONG":
            if _ob_l and _ob_l < current_price * 0.999:
                raw_limit = _ob_l         # OB 底部 — 機構支撐入場
            elif _fvg_l and _fvg_l < current_price * 0.999:
                raw_limit = _fvg_l        # FVG 底部填充
            else:
                raw_limit = current_price * (1 - 0.003)  # 固定回調 0.3%
            entry = max(raw_limit, current_price * (1 - _max_off))
        else:
            if _ob_h and _ob_h > current_price * 1.001:
                raw_limit = _ob_h         # OB 頂部 — 機構阻力做空
            elif _fvg_h and _fvg_h > current_price * 1.001:
                raw_limit = _fvg_h        # FVG 頂部填充
            else:
                raw_limit = current_price * (1 + 0.003)  # 固定反彈 0.3%
            entry = min(raw_limit, current_price * (1 + _max_off))
        entry = round(entry, 4)
        _limit_ref_price = current_price  # 掛單時市價，供通知使用
        sl_dist = atr * 1.5
        sl = entry - sl_dist if side == "LONG" else entry + sl_dist
        risk = abs(entry - sl)

        # â è¦æ ¼åçï¼1.5R / 3.0R / 5.0R
        if side == "LONG":
            tp_levels = [entry + risk * 1.5, entry + risk * 3.0, entry + risk * 5.0]
        else:
            tp_levels = [entry - risk * 1.5, entry - risk * 3.0, entry - risk * 5.0]

        # ð¯ åæ TP æ ¡æ­£ï¼é è¨­éé â åºå® 1.5R/3R/5R ä¸åï¼
        cfg_rr_mode = load_config()
        if not cfg_rr_mode.get("fixed_rr_mode", True):
            tp_levels, tp_notes = adjust_tp_by_sr(entry, side, tp_levels, df)
            if tp_notes:
                detail["tp_adjust_notes"] = tp_notes

        # âï¸ R:R æä½éæª» â TP1 è³å°è¦æ N Rï¼å¦åæçµï¼å  0.02 å®¹å·®é¿åæµ®é»èª¤å·®ï¼
        cfg_rr = load_config()
        min_rr = cfg_rr.get("min_rr_ratio", 1.5)
        actual_tp1_r = abs(tp_levels[0] - entry) / max(risk, 1e-9)
        if actual_tp1_r < min_rr - 0.02:
            logging.info(
                f"[{instId}] {side} è¨è R:R={actual_tp1_r:.2f} < {min_rr}ï¼æçµ"
            )
            continue

        # ð§± æ OB åéå­é²è¨èï¼çµ¦å¤±æéå ´ç¨ï¼
        ob_zone = find_order_block(df, side)

        candidates.append(
            {
                "instId": instId,
                "side": side,
                "tf": "15m",
                "entry": round(entry, 4),
                "sl": round(sl, 4),
                "tp1": round(tp_levels[0], 4),
                "tp2": round(tp_levels[1], 4),
                "tp3": round(tp_levels[2], 4),
                "score": score,
                "grade": grade,
                "detail": detail,
                "funding_rate": funding_rate,
                "mtf_snapshot": mtf,
                "regime_snapshot": regime_info,
                "ob_zone": ob_zone,            # ð§± OB å¤±æéå ´ç¨
                "created": time.time(),
                "expires": time.time() + signal_expire_hours * 3600,
            }
        )

    return max(candidates, key=lambda x: x["score"]) if candidates else None


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 9. æä¹åï¼å·å» / è¨è / äº¤æï¼
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def _load_json(path: str, default):
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        logging.warning(f"â ï¸ è®å {path} å¤±æï¼{e}")
    return default


def _save_json(path: str, data) -> None:
    try:
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp, path)
    except Exception as e:
        logging.error(f"â å¯«å¥ {path} å¤±æï¼{e}")


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 9.5 éç½®ç±æ´æ°èé©è­
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def _deep_merge(base: dict, override: dict) -> dict:
    """éè¿´åä½µï¼override è¦è baseï¼ä½ä¿ç base ä¸­ override æ²è¦èçéµ"""
    out = dict(base)
    for k, v in override.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _deep_merge(out[k], v)
        else:
            out[k] = v
    return out


def _validate_config(cfg: dict) -> list:
    """ð¡ï¸ é©è­ config åçæ§ â åå³é¯èª¤è¨æ¯åè¡¨ï¼ç©ºä»£è¡¨ééï¼"""
    errs = []
    if not (50 <= cfg.get("score_threshold", 0) <= 100):
        errs.append("score_threshold å¿é å¨ 50â100")
    if not (1 <= cfg.get("max_signals", 0) <= 10):
        errs.append("max_signals å¿é å¨ 1â10")
    if cfg.get("cooldown_hours", -1) < 0:
        errs.append("cooldown_hours ä¸è½çºè² ")
    if cfg.get("signal_expire_hours", 0) <= 0:
        errs.append("signal_expire_hours å¿é  > 0")
    pv = cfg.get("price_verification", {})
    if not (0 < pv.get("max_deviation_pct", 0) < 10):
        errs.append("price_verification.max_deviation_pct æå¨ 0â10%")
    cb = cfg.get("circuit_breaker", {})
    if cb.get("soft_threshold", 0) >= cb.get("hard_threshold", 99):
        errs.append("soft_threshold æ < hard_threshold")
    for w in cfg.get("blackout_windows_tw", []):
        try:
            for k in ("start", "end"):
                hh, mm = map(int, w[k].split(":"))
                assert 0 <= hh < 24 and 0 <= mm < 60
        except Exception:
            errs.append(f"blackout_windows_tw ææ®µæ ¼å¼é¯èª¤ï¼{w}")
    return errs


def load_config() -> dict:
    """ð è¼å¥ config.jsonï¼ä¸å­å¨æé©è­å¤±æåç¨é è¨­å¼ï¼"""
    user_cfg = _load_json(CONFIG_FILE, {})
    merged = _deep_merge(DEFAULT_CONFIG, user_cfg) if user_cfg else dict(DEFAULT_CONFIG)
    errs = _validate_config(merged)
    if errs:
        logging.warning("â ï¸ éç½®é©è­å¤±æï¼å¨é¢ fallback å°é è¨­å¼ï¼" + "; ".join(errs))
        return dict(DEFAULT_CONFIG)
    return merged


def is_cooling(instId: str, cooldown_hours: float = COOLDOWN_HOURS) -> bool:
    """ð§ æ¯å¦éå¨å·å»æå§ï¼æä¹åçæ¬ï¼"""
    cd = _load_json(COOLDOWN_FILE, {})
    last = cd.get(instId)
    if last is None:
        return False
    return (time.time() - float(last)) < cooldown_hours * 3600


def mark_cooldown(instId: str, cooldown_hours: float = COOLDOWN_HOURS) -> None:
    cd = _load_json(COOLDOWN_FILE, {})
    cd[instId] = time.time()
    # é ä¾¿æ¸é¤éæç´é
    cutoff = time.time() - cooldown_hours * 3600 * 3
    cd = {k: v for k, v in cd.items() if float(v) > cutoff}
    _save_json(COOLDOWN_FILE, cd)


def record_trade(
    coin: str,
    side: str,
    order_id: str,
    entry: float,
    close_price: float,
    close_type: str,
    score: int,
    sig_snapshot: dict | None = None,
) -> None:
    """ð è¨éäº¤ææ­·å² + é¤µçµ¦å­¸ç¿æ©å¶"""
    is_win = close_type in ("TP1", "TP2", "TP3", "LOCK")
    is_be = close_type == "BE"
    pnl = (
        (close_price - entry) / entry * 100
        if side == "LONG"
        else (entry - close_price) / entry * 100
    )
    snap = sig_snapshot or {}
    detail = snap.get("detail", {}) or {}
    funding_rate = snap.get("funding_rate")
    mtf = snap.get("mtf_snapshot")
    regime = snap.get("regime_snapshot")

    # ð§¬ é²å ´æçç¹å¾µåéï¼çµ¦ KNN å­¸ç¿æ¥ç¸ä¼¼åº¦ç¨ï¼
    features = vectorize_signal(score, side, detail, funding_rate, mtf, regime)

    trade = {
        "time": tw_now().strftime("%Y-%m-%d %H:%M"),
        "date": tw_now().strftime("%Y-%m-%d"),
        "order_id": order_id,
        "coin": coin,
        "side": side,
        "entry": entry,
        "close": close_price,
        "close_type": close_type,
        "pnl": round(pnl, 2),
        "is_win": is_win,
        "is_be": is_be,
        "score": score,
        "funding_rate": funding_rate,
        "detail": detail,
        "features": features,        # ð§¬ KNN ç¨
        "mtf": mtf,                  # é²å ´æ 1H/4H è¶¨å¢
        "regime": regime,            # é²å ´æå¸å ´çæ
    }
    history = _load_json(TRADE_HISTORY_FILE, [])
    history.append(trade)
    _save_json(TRADE_HISTORY_FILE, history)
    logging.info(f"ð è¨éäº¤æï¼{coin} {order_id} {close_type}")

    # ð§  é¤µçµ¦å­¸ç¿æ©å¶
    try:
        update_learning(trade, sig_snapshot)
    except Exception as e:
        logging.warning(f"â ï¸ æ´æ°å­¸ç¿çæå¤±æï¼{e}")


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 9.6 å­¸ç¿æ©å¶ï¼æ¯ç­äº¤æçµæå¾æ´æ°æ¡¶ â è©åæèªåå¥ç¨èª¿æ´ï¼
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def _bucket_score(score: int) -> str:
    if score >= 90:
        return "score:90+"
    if score >= 80:
        return "score:80-89"
    if score >= 70:
        return "score:70-79"
    return "score:60-69"


def _bucket_rsi(rsi: float, side: str) -> str:
    bucket = int(rsi // 10) * 10
    return f"rsi_{side.lower()}:{bucket}-{bucket + 9}"


def _bucket_funding(fr) -> str:
    if fr is None:
        return "fund:none"
    if fr > 0.0008:
        return "fund:very_pos"
    if fr > 0.0001:
        return "fund:pos"
    if fr > -0.0001:
        return "fund:neutral"
    if fr > -0.0008:
        return "fund:neg"
    return "fund:very_neg"


def _bucket_session_tw() -> str:
    """ä»¥å°ç£æéç²åååäº¤æææ®µ"""
    h = tw_now().hour
    if 0 <= h < 6:
        return "sess:asia_dawn"
    if 6 <= h < 14:
        return "sess:asia_day"
    if 14 <= h < 21:
        return "sess:europe"
    return "sess:us"


def _signal_buckets(score: int, side: str, detail: dict, funding_rate, coin: str) -> list:
    """æè¨èç¹å¾µææå¤åæ¡¶ â ä¾å­¸ç¿æ¥è©¢"""
    rsi = (detail or {}).get("rsi_value", 50)
    return [
        _bucket_score(score),
        _bucket_rsi(rsi, side),
        _bucket_funding(funding_rate),
        _bucket_session_tw(),
        f"coin:{coin}",
        f"coin_side:{coin}_{side}",
    ]


def update_learning(trade: dict, sig_snapshot: dict | None = None) -> None:
    """ð§  æ¯ç­äº¤æçµæå¾æ´æ°å­¸ç¿æ¡¶èæå¹£ç¨®çµ±è¨"""
    state = _load_json(LEARNING_FILE, {})
    state.setdefault("buckets", {})
    state.setdefault("by_coin", {})
    state.setdefault("loss_reasons", [])
    state.setdefault("updated_at", 0)

    score = trade.get("score", 0)
    coin = trade.get("coin", "?")
    side = trade.get("side", "?")
    close_type = trade.get("close_type", "?")
    funding_rate = trade.get("funding_rate")
    detail = trade.get("detail") or (sig_snapshot.get("detail") if sig_snapshot else {})

    is_win = close_type in ("TP1", "TP2", "TP3", "LOCK")
    is_be = close_type == "BE"
    is_loss = close_type == "SL"

    for b in _signal_buckets(score, side, detail, funding_rate, coin):
        bd = state["buckets"].setdefault(
            b, {"win": 0, "loss": 0, "be": 0, "total": 0}
        )
        bd["total"] += 1
        if is_win:
            bd["win"] += 1
        elif is_loss:
            bd["loss"] += 1
        elif is_be:
            bd["be"] += 1

    cd = state["by_coin"].setdefault(
        coin, {"win": 0, "loss": 0, "be": 0, "total": 0}
    )
    cd["total"] += 1
    if is_win:
        cd["win"] += 1
    elif is_loss:
        cd["loss"] += 1
    elif is_be:
        cd["be"] += 1

    state["updated_at"] = time.time()
    _save_json(LEARNING_FILE, state)


def apply_learning_adjustment(
    score: int,
    side: str,
    detail: dict,
    funding_rate,
    coin: str,
) -> tuple[int, list]:
    """ð§  å¥ç¨å­¸ç¿çæ â (èª¿æ´å¾åæ¸, å¥ç¨ç´é)"""
    cfg = load_config()
    lcfg = cfg.get("learning", {})
    if not lcfg.get("enabled", True):
        return score, []

    state = _load_json(LEARNING_FILE, {})
    buckets = state.get("buckets", {})
    min_samples = lcfg.get("min_samples", 5)
    max_adj = lcfg.get("max_score_adjust", 10)

    notes = []
    adj_total = 0
    for b in _signal_buckets(score, side, detail, funding_rate, coin):
        bd = buckets.get(b)
        if not bd or bd.get("total", 0) < min_samples:
            continue
        wr = bd["win"] / bd["total"]
        if wr < 0.30:
            d = -3
        elif wr < 0.40:
            d = -2
        elif wr > 0.70:
            d = +2
        elif wr > 0.60:
            d = +1
        else:
            continue
        adj_total += d
        notes.append(f"{b} (n={bd['total']}, åç {wr:.0%}) â {d:+d}")

    adj_total = max(-max_adj, min(max_adj, adj_total))
    return score + adj_total, notes


def _summarize_trades(trades: list) -> dict:
    n = len(trades)
    if n == 0:
        return {"n": 0}
    win = sum(1 for t in trades if t.get("close_type") in ("TP1", "TP2", "TP3", "LOCK"))
    loss = sum(1 for t in trades if t.get("close_type") == "SL")
    be = sum(1 for t in trades if t.get("close_type") == "BE")
    pnl = sum(t.get("pnl", 0) for t in trades)
    pnls = [t.get("pnl", 0) for t in trades]
    avg = pnl / n if n else 0
    biggest_win = max(pnls) if pnls else 0
    biggest_loss = min(pnls) if pnls else 0
    return {
        "n": n,
        "win": win,
        "loss": loss,
        "be": be,
        "wr": win / n * 100 if n else 0,
        "pnl": pnl,
        "avg": avg,
        "max_win": biggest_win,
        "max_loss": biggest_loss,
    }


def format_daily_report(date: str | None = None) -> str:
    """ð æ¥å ±ï¼ç¶å¤©äº¤ææ¦è¦½ + ç¸¾æ"""
    if date is None:
        date = tw_now().strftime("%Y-%m-%d")
    history = _load_json(TRADE_HISTORY_FILE, [])
    today = [t for t in history if t.get("date") == date]
    s = _summarize_trades(today)
    if s["n"] == 0:
        return f"ð­ *æ¥å ± {date}*\nç¶æ¥å°ç¡äº¤æç´é"

    lines = [
        f"ð *æ¥å ± {date}*",
        "ââââââââââââââ",
        f"äº¤æç­æ¸ï¼{s['n']}",
        f"å / å¹³ / æï¼{s['win']} / {s['be']} / {s['loss']}",
        f"åçï¼`{s['wr']:.0f}%`",
        f"ç¸½ PnLï¼`{s['pnl']:+.2f}%`",
        f"å¹³åï¼`{s['avg']:+.2f}%/ç­`",
        f"æå¤§ç²å©ï¼`{s['max_win']:+.2f}%`ãæå¤§è§æï¼`{s['max_loss']:+.2f}%`",
        "",
    ]

    # åå¹£ç¨®è¡¨ç¾
    by_coin = {}
    for t in today:
        c = t.get("coin", "?")
        by_coin.setdefault(c, []).append(t)
    if by_coin:
        lines.append("ð *åå¹£ç¨®è¡¨ç¾*ï¼")
        for c, ts in sorted(by_coin.items(), key=lambda x: -sum(t.get("pnl", 0) for t in x[1])):
            sub = _summarize_trades(ts)
            lines.append(
                f"  {c}: {sub['n']} ç­ (å {sub['win']}/æ {sub['loss']}) "
                f"PnL `{sub['pnl']:+.2f}%`"
            )

    return "\n".join(lines)


def format_monthly_report(year_month: str | None = None) -> str:
    """ð æå ±ï¼ç¶æç¸¾æ + å­¸ç¿é²å±"""
    if year_month is None:
        year_month = tw_now().strftime("%Y-%m")
    history = _load_json(TRADE_HISTORY_FILE, [])
    month = [t for t in history if t.get("date", "").startswith(year_month)]
    s = _summarize_trades(month)
    if s["n"] == 0:
        return f"ð­ *æå ± {year_month}*\næ¬æå°ç¡äº¤æç´é"

    lines = [
        f"ð *æå ± {year_month}*",
        "ââââââââââââââ",
        f"ç¸½äº¤æï¼{s['n']} ç­",
        f"å / å¹³ / æï¼{s['win']} / {s['be']} / {s['loss']}",
        f"åçï¼`{s['wr']:.0f}%`",
        f"ç¸½ PnLï¼`{s['pnl']:+.2f}%`",
        f"å¹³åï¼`{s['avg']:+.2f}%/ç­`",
        f"æå¤§ç²å©ï¼`{s['max_win']:+.2f}%`ãæå¤§è§æï¼`{s['max_loss']:+.2f}%`",
        "",
    ]

    # é£å / é£æ
    cur_streak = 0
    streak_type = None
    max_win_streak = 0
    max_loss_streak = 0
    for t in month:
        ct = t.get("close_type")
        is_w = ct in ("TP1", "TP2", "TP3", "LOCK")
        is_l = ct == "SL"
        if is_w:
            if streak_type == "win":
                cur_streak += 1
            else:
                streak_type = "win"
                cur_streak = 1
            max_win_streak = max(max_win_streak, cur_streak)
        elif is_l:
            if streak_type == "loss":
                cur_streak += 1
            else:
                streak_type = "loss"
                cur_streak = 1
            max_loss_streak = max(max_loss_streak, cur_streak)

    lines.append(f"ð¥ æå¤§é£åï¼{max_win_streak}ãâï¸ æå¤§é£æï¼{max_loss_streak}")
    lines.append("")

    # åå¹£ç¨®
    by_coin = {}
    for t in month:
        c = t.get("coin", "?")
        by_coin.setdefault(c, []).append(t)
    if by_coin:
        lines.append("ð *åå¹£ç¨®è¡¨ç¾*ï¼")
        ranked = sorted(by_coin.items(), key=lambda x: -sum(t.get("pnl", 0) for t in x[1]))
        for c, ts in ranked:
            sub = _summarize_trades(ts)
            lines.append(
                f"  {c}: {sub['n']} ç­ Â· åç `{sub['wr']:.0f}%` Â· PnL `{sub['pnl']:+.2f}%`"
            )

    return "\n".join(lines)


def format_learning_report() -> str:
    """ð§  /learning å½ä»¤ â é¡¯ç¤ºæ©å¨äººå­¸å°äºä»éº¼"""
    state = _load_json(LEARNING_FILE, {})
    buckets = state.get("buckets", {})
    by_coin = state.get("by_coin", {})
    loss_reasons = state.get("loss_reasons", [])

    if not buckets and not by_coin:
        return (
            "ð§  *æ©å¨äººå­¸ç¿çæ*\n\n"
            "ð­ ç®åéæ²ç´¯ç©è¶³å¤ è³æ\n"
            "è³å°éè¦ 5 ç­å·²çµæäº¤æææéå§å¥ç¨å­¸ç¿èª¿æ´"
        )

    lines = ["ð§  *æ©å¨äººå­¸ç¿çæ*", "ââââââââââââââ", ""]

    # 1. æå¹£ç¨®åç
    if by_coin:
        lines.append("ð *åå¹£ç¨®æ°ç¸¾*ï¼")
        sorted_coins = sorted(by_coin.items(), key=lambda x: -x[1].get("total", 0))
        for coin, d in sorted_coins[:12]:
            n = d.get("total", 0)
            w = d.get("win", 0)
            l = d.get("loss", 0)
            be = d.get("be", 0)
            wr = w / n * 100 if n else 0
            lines.append(
                f"  {coin}: {n} ç­ï¼å {w} / å¹³ {be} / æ {l}ï¼åç `{wr:.0f}%`ï¼"
            )
        lines.append("")

    # 2. é«åççµåï¼æ¨£æ¬ â¥ 5ï¼
    high_wr = [
        (b, d) for b, d in buckets.items()
        if d.get("total", 0) >= 5 and d["win"] / d["total"] > 0.6
    ]
    if high_wr:
        lines.append("â *é«åççµåï¼>60%ï¼*ï¼")
        for b, d in sorted(high_wr, key=lambda x: -x[1]["win"] / x[1]["total"])[:5]:
            wr = d["win"] / d["total"] * 100
            lines.append(f"  `{b}` â {d['total']} ç­ï¼åç `{wr:.0f}%`")
        lines.append("")

    # 3. ä½åççµå
    low_wr = [
        (b, d) for b, d in buckets.items()
        if d.get("total", 0) >= 5 and d["win"] / d["total"] < 0.4
    ]
    if low_wr:
        lines.append("â ï¸ *ä½åççµåï¼<40%ï¼*ï¼")
        for b, d in sorted(low_wr, key=lambda x: x[1]["win"] / x[1]["total"])[:5]:
            wr = d["win"] / d["total"] * 100
            lines.append(f"  `{b}` â {d['total']} ç­ï¼åç `{wr:.0f}%`")
        lines.append("")

    # 4. ä¸»è¦æ­¢æåå 
    if loss_reasons:
        from collections import Counter
        cnt = Counter(r.get("title", "?") for r in loss_reasons[-30:])
        lines.append("ð *æè¿ 30 ç­æ­¢æä¸»å  TOP3*ï¼")
        for title, c in cnt.most_common(3):
            lines.append(f"  {title} Ã {c}")
        lines.append("")

    lines.append("ð¡ _éäºçµ±è¨æ¯ç­äº¤æçµç®å¾èªåæ´æ°ï¼ä¸æ¬¡ç¸ä¼¼æå¢çè¨èè©åæèªåå¾®èª¿_")
    return "\n".join(lines)


def vectorize_signal(
    score: int,
    side: str,
    detail: dict,
    funding_rate,
    mtf: dict | None = None,
    regime: dict | None = None,
) -> dict:
    """ð§¬ æè¨èç¹å¾µææåéï¼çµ¦ KNN ç¨ï¼"""
    rsi = (detail or {}).get("rsi_value", 50)
    return {
        "score": float(score),
        "rsi": float(rsi),
        "atr_pct": float((detail or {}).get("atr_pct", 1.0)),
        "funding": float(funding_rate or 0) * 1000,
        "vol_ratio": float((detail or {}).get("volume_ratio", 1.0)),
        "adx": float((regime or {}).get("adx", 20)),
        "mtf_h1": 1.0 if (mtf or {}).get("1H", {}).get("supertrend") == (1 if side == "LONG" else -1) else 0.0,
        "mtf_h4": 1.0 if (mtf or {}).get("4H", {}).get("supertrend") == (1 if side == "LONG" else -1) else 0.0,
        "side": 1.0 if side == "LONG" else 0.0,
    }


_FEATURE_SCALE = {
    "score": 30, "rsi": 50, "atr_pct": 3, "funding": 2,
    "vol_ratio": 3, "adx": 50, "mtf_h1": 1, "mtf_h4": 1, "side": 1,
}


def find_similar_trades(features: dict, history: list, k: int = 10) -> list:
    """ð§¬ KNNï¼æ¾æç¸ä¼¼ç k ç­æç¹å¾µçæ­·å²äº¤æï¼æ­å¼è·é¢ï¼å·²æ­¸ä¸åï¼"""
    candidates = []
    for t in history:
        f = t.get("features")
        if not f:
            continue
        d2 = 0.0
        for key, scale in _FEATURE_SCALE.items():
            diff = (features.get(key, 0) - f.get(key, 0)) / max(scale, 1)
            d2 += diff * diff
        candidates.append((d2, t))
    candidates.sort(key=lambda x: x[0])
    return [t for _, t in candidates[:k]]


def apply_knn_learning(
    score: int,
    side: str,
    detail: dict,
    funding_rate,
    coin: str,
    mtf: dict | None,
    regime: dict | None,
) -> tuple[int, list]:
    """ð§¬ KNN å­¸ç¿ï¼æ¾æç¸ä¼¼ç 10 ç­æ­·å²äº¤æï¼çåç â (èª¿æ´å¾åæ¸, ç´é)"""
    cfg = load_config()
    if not cfg.get("learning", {}).get("knn_enabled", True):
        return score, []
    history = _load_json(TRADE_HISTORY_FILE, [])
    if len(history) < 10:
        return score, []
    feat = vectorize_signal(score, side, detail, funding_rate, mtf, regime)
    similar = find_similar_trades(feat, history, k=10)
    if len(similar) < 3:
        return score, []
    wins = sum(1 for t in similar if t.get("close_type") in ("TP1", "TP2", "TP3", "LOCK"))
    losses = sum(1 for t in similar if t.get("close_type") == "SL")
    n = len(similar)
    wr = wins / n
    notes = [f"ð§¬ KNNï¼{n} ç­æç¸ä¼¼è¨è â å {wins} / æ {losses} (åç {wr:.0%})"]
    if wr < 0.30:
        return score - 8, notes + ["KNN ä½åç â -8"]
    if wr < 0.40:
        return score - 4, notes + ["KNN åä½åç â -4"]
    if wr > 0.70:
        return score + 5, notes + ["KNN é«åç â +5"]
    if wr > 0.60:
        return score + 3, notes + ["KNN ä¸­é«åç â +3"]
    return score, notes


def record_loss_reason(coin: str, side: str, reasons: list) -> None:
    """è¨éæ­¢æä¸»å å° learning_stateï¼ä¾å¾çºæ¥è©¢ï¼"""
    state = _load_json(LEARNING_FILE, {})
    state.setdefault("loss_reasons", [])
    for r in reasons[:1]:  # åªè¨ç¬¬ä¸åä¸»å 
        state["loss_reasons"].append({
            "ts": time.time(),
            "coin": coin,
            "side": side,
            "code": r.get("code"),
            "title": r.get("title"),
        })
    # åªä¿çæè¿ 100 ç­
    state["loss_reasons"] = state["loss_reasons"][-100:]
    _save_json(LEARNING_FILE, state)


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 9.65 è¦ç¤åæï¼SL/BE/LOCK å¾è§£éçºä»éº¼ï¼
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def analyze_loss(sig: dict, df_at_loss: list) -> list:
    """ð æ¯è¼é²å ´éè¿ vs åºå ´éè¿çå¸æ³ï¼åæ¨ä¸»å ï¼æå¤ 3 åï¼"""
    if not df_at_loss or len(df_at_loss) < 20:
        return [{
            "code": "INSUFFICIENT",
            "title": "ð è³æä¸è¶³",
            "detail": "é²å ´å¾ K ç·å¤ªå°ï¼ç¡æ³è©³ç´°åæ",
            "severity": 0,
        }]

    side = sig["side"]
    expect = 1 if side == "LONG" else -1
    n = len(df_at_loss)
    df_then = df_at_loss[: max(20, n // 3)]
    df_now = df_at_loss

    reasons = []

    # 1. è¶¨å¢åè½
    st_then = calc_supertrend(df_then)
    st_now = calc_supertrend(df_now)
    if st_then == expect and st_now == -expect:
        reasons.append({
            "code": "TREND_REVERSAL",
            "title": "ð è¶¨å¢åè½",
            "detail": f"é²å ´æ Supertrend é å¢ï¼{'å¤' if expect == 1 else 'ç©º'}ï¼ï¼æ­¢æåå·²ç¿»ååå",
            "severity": 30,
        })

    # 2. RSI åè½å´©å¡ / åè½
    rsi_then = calc_rsi(df_then)
    rsi_now = calc_rsi(df_now)
    if side == "LONG" and rsi_then > 45 and rsi_now < 35 and (rsi_then - rsi_now) > 12:
        reasons.append({
            "code": "RSI_COLLAPSE",
            "title": "ð å¤é ­åè½ç¦è§£",
            "detail": f"RSI å¾ {rsi_then:.0f} æ¥è·è³ {rsi_now:.0f}ï¼ä¸è· {rsi_then - rsi_now:.0f} åï¼",
            "severity": 25,
        })
    elif side == "SHORT" and rsi_then < 55 and rsi_now > 65 and (rsi_now - rsi_then) > 12:
        reasons.append({
            "code": "RSI_REBOUND",
            "title": "ð ç©ºé ­åè½åè½",
            "detail": f"RSI å¾ {rsi_then:.0f} åå½è³ {rsi_now:.0f}ï¼ä¸æ¼² {rsi_now - rsi_then:.0f} åï¼",
            "severity": 25,
        })

    # 3. æµåæ§æè©ï¼åååçªç ´ï¼
    sweep_dir = "SHORT" if side == "LONG" else "LONG"
    if detect_liquidity_sweep(df_now[-12:], sweep_dir):
        reasons.append({
            "code": "LIQ_SWEEP",
            "title": "ð æµåæ§æè©",
            "detail": "æ­¢æååºç¾åååçªç ´æéå¾å¿«éæ¶åï¼çä¼¼ä¸»åææ",
            "severity": 22,
        })

    # 4. æ³¢åçæ¿å¢
    atr_then = calc_atr(df_then)
    atr_now = calc_atr(df_now)
    if atr_then > 0 and atr_now / atr_then > 1.5:
        reasons.append({
            "code": "VOL_SPIKE",
            "title": "ðª æ³¢åçæ¿å¢",
            "detail": f"ATR å¾ {atr_then:.4f} æ´å¼µè³ {atr_now:.4f}ï¼{(atr_now / atr_then - 1) * 100:.0f}% å¢å¹ï¼",
            "severity": 18,
        })

    # 5. é£çºåå K ç·
    last10 = df_now[-10:]
    against = sum(
        1 for b in last10
        if (side == "LONG" and b["c"] < b["o"]) or (side == "SHORT" and b["c"] > b["o"])
    )
    if against >= 7:
        reasons.append({
            "code": "AGAINST_MOMENTUM",
            "title": "ðª æçºåååè½",
            "detail": f"åºå ´å 10 æ ¹ K ç·ä¸­ {against} æ ¹ååæ¶ç·ï¼è¶¨å¢å·²è½",
            "severity": 15,
        })

    # 6. OB / FVG çµæ§å¤±æ
    ob = find_order_block(df_then, side)
    if ob:
        breached = (
            (side == "LONG" and df_now[-1]["c"] < ob["low"])
            or (side == "SHORT" and df_now[-1]["c"] > ob["high"])
        )
        if breached:
            reasons.append({
                "code": "OB_BROKEN",
                "title": "ð§± è¨å®å¡è·ç ´",
                "detail": "é²å ´ä¾æç SMC è¨å®å¡å·²è¢«æ¶ç¤è·ç ´ï¼çµæ§å¤±æ",
                "severity": 20,
            })

    if not reasons:
        reasons.append({
            "code": "NORMAL_NOISE",
            "title": "ð æ­£å¸¸æ³¢å",
            "detail": "æªåµæ¸¬å°æç¢ºçè¶¨å¢åè½æçµæ§ç ´å£ï¼å¯è½æ¯ ATR ç¯åå§çæ­£å¸¸éè¨ææ",
            "severity": 5,
        })

    reasons.sort(key=lambda x: -x["severity"])
    return reasons[:3]


def _generate_lessons(reasons: list) -> list:
    """æ ¹æä¸»å ç¢çãä¸æ¬¡è©²æéº¼å¤æ·ãçå»ºè­°"""
    advice_map = {
        "TREND_REVERSAL": "é²å ´å¾è¥ Supertrend ç¿»åååï¼å»ºè­°ç«å³æ¸åæä¸»ååºå ´ï¼ä¸è¦ç­æ­¢æ",
        "RSI_COLLAPSE": "RSI å¾ä¸­æ§åï¼>45ï¼æ¥è·å°è¶è³£ï¼<35ï¼éå¸¸ä»£è¡¨åè½è½æï¼å¯ä½çºæåé¢å ´ä¿¡è",
        "RSI_REBOUND": "RSI å¾ä¸­æ§åï¼<55ï¼åå½å°è¶è²·ï¼>65ï¼éå¸¸ä»£è¡¨ç©ºé ­åè½ç¦è§£ï¼ææ©å¹³åé¿æ",
        "LIQ_SWEEP": "æéåæ­¢æè¥åå K é¨å¾åºç¾ï¼å¤åæ¯ä¸»åèªå¤/èªç©ºï¼ä¸æ¬¡å¯æ SL æé  0.2 ATR",
        "VOL_SPIKE": "ATR çªç¶æ´å¼µä»£è¡¨é²å¥é«æ³¢ååï¼å»ºè­°è©²å¹£ç¨®æ«å 1â2 å°ææç¸®å°åä½",
        "AGAINST_MOMENTUM": "åå K é£çº 7 æ ¹ä»¥ä¸ = è¶¨å¢æç¢ºï¼ææ¯åè¨ SL æ´æ©ä¸»åæ­¢æéæ",
        "OB_BROKEN": "SMC è¨å®å¡ä¸æ¦æ¶ç¤è·ç ´ä»£è¡¨çµæ§å¤±æï¼éæç¹¼çºæ±å®è§æææ¾å¤§",
        "NORMAL_NOISE": "æ¬æ¬¡å±¬æ­£å¸¸æ³¢åéè¨ï¼å¯è½ SL è¨­å¾å¤ªç·ï¼ä¸æ¬¡ ATRÃ1.5 â ATRÃ1.8 ææ´ç©©",
        "INSUFFICIENT": "é²å ´å¾è³æä¸è¶³ï¼ç¡æ³è©³ç´°æ­¸å ",
    }
    out = []
    seen = set()
    for r in reasons[:2]:
        code = r.get("code")
        if code in seen or code not in advice_map:
            continue
        seen.add(code)
        out.append(advice_map[code])
    return out


def _fmt_postmortem(
    sig: dict,
    mode: str,
    reasons: list,
    lessons: list,
    similar_stats: tuple | None = None,
) -> str:
    """ð è¦ç¤åæè¨æ¯"""
    coin = sig["instId"].split("-")[0]
    order_id = sig.get("order_id", "N/A")
    side = sig["side"]
    direction = "åå¤" if side == "LONG" else "åç©º"
    label = (
        "â æ­¢æ"
        if mode == "LOSS"
        else "ð ä¿æ¬"
        if mode == "BE"
        else "ð éå©"
        if mode == "LOCK"
        else "ð¯ æ­¢ç"
    )

    lines = [
        f"ð *{coin} è¦ç¤åæ*",
        f"ââââââââââââââ",
        f"ð è¨å®ï¼`{order_id}`",
        f"â° æéï¼{tw_ts()}",
        f"æ¹åï¼{direction}ãçµç®ï¼{label}",
        f"åå§è©åï¼{sig.get('score', 0)} å",
        "",
        "ð *ä¸»è¦åå ï¼ä¾å´éåº¦ï¼*ï¼",
    ]
    for i, r in enumerate(reasons, 1):
        lines.append(f"{i}. {r['title']}")
        lines.append(f"   _{r['detail']}_")

    if lessons:
        lines.append("")
        lines.append("ð¡ *ä¸æ¬¡è©²æéº¼å¤æ·*ï¼")
        for l in lessons:
            lines.append(f"  â¢ {l}")

    if similar_stats:
        n, w, l, be = similar_stats
        if n >= 3:
            wr = w / n * 100
            lines.append("")
            lines.append(
                f"ð åé¡è¨­å®æ­·å²ï¼{n} ç­ï¼å {w} / å¹³ {be} / æ {l}ï¼åç `{wr:.0f}%`ï¼"
            )

    lines.append("")
    lines.append("ð§  _æ­¤æ¬¡ä¸»å å·²å¯«å¥å­¸ç¿è³æï¼ä¸æ¬¡ç¸ä¼¼ææ³è©åèªåèª¿æ´_")
    return "\n".join(lines)


def get_similar_stats(score: int, side: str, detail: dict, funding_rate, coin: str) -> tuple:
    """å¾å­¸ç¿çæåãåé¡è¨­å®ãçæ­·å²åè² """
    state = _load_json(LEARNING_FILE, {})
    buckets = state.get("buckets", {})
    # åãcoin_sideãéåæå·é«çæ¡¶
    key = f"coin_side:{coin}_{side}"
    bd = buckets.get(key, {})
    n = bd.get("total", 0)
    w = bd.get("win", 0)
    l = bd.get("loss", 0)
    be = bd.get("be", 0)
    return (n, w, l, be)


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 9.7 ç³»çµ±çæï¼çæ·ç´éï¼
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def get_system_state() -> dict:
    return _load_json(SYSTEM_STATE_FILE, {})


def set_system_state(state: dict) -> None:
    _save_json(SYSTEM_STATE_FILE, state)


def check_health() -> tuple[bool, str]:
    """ð©º ç³»çµ±å¥åº·æª¢æ¥ â (æåé¡?, è¨æ¯)

    è§¸ç¼æ¢ä»¶ï¼
      1. è¶é 24 å°ææ²æåééä»»ä½ TG è¨æ¯
      2. é£çº 5 æ¬¡ææç°å¸¸çµæ
    ï¼6 å°æå§ä¸éè¤è­¦å ±ï¼
    """
    state = get_system_state()
    last_tg = state.get("last_tg_sent", 0)
    last_warn = state.get("last_health_warning", 0)
    fail_count = state.get("scan_failure_count", 0)

    # 6h å§ä¸éè¤è­¦å ±
    if time.time() - last_warn < 6 * 3600:
        return False, ""

    # æ¢ä»¶ 1ï¼24h æ²éé TG
    if last_tg > 0:
        hours_since = (time.time() - last_tg) / 3600
        if hours_since > 24:
            state["last_health_warning"] = time.time()
            set_system_state(state)
            return True, (
                f"â ï¸ *ç³»çµ±å¥åº·è­¦å ±*\n"
                f"ââââââââââââââ\n"
                f"â° æéï¼{tw_ts()}\n"
                f"\n"
                f"å·²è¶é *{hours_since:.0f} å°æ*æ²ç¼åºä»»ä½è¨è / éç¥\n"
                f"\n"
                f"ð¡ å¯è½åå ï¼\n"
                f"  â¢ TG_TOKEN å¤±æ\n"
                f"  â¢ OKX API ç°å¸¸\n"
                f"  â¢ è¨èå¨è¢«å­¸ç¿æ©å¶ / é¢¨æ§éæ¿¾\n"
                f"  â¢ GitHub Actions éé¡èç¡\n"
                f"\n"
                f"è«æª¢æ¥ GitHub Actions é é¢è Telegram bot çæ"
            )

    # æ¢ä»¶ 2ï¼é£çºå¤±æ 5 æ¬¡
    if fail_count >= 5:
        state["last_health_warning"] = time.time()
        set_system_state(state)
        return True, (
            f"â ï¸ *ç³»çµ±å¥åº·è­¦å ±*\n"
            f"ââââââââââââââ\n"
            f"â° æéï¼{tw_ts()}\n"
            f"\n"
            f"ä¸»ææå·²é£çºå¤±æ *{fail_count} æ¬¡*\n"
            f"\n"
            f"ð¡ è«é² GitHub Actions æ¥æè¿ä¸æ¬¡å¤±æç logï¼æ @ æå¹«ä½  debug"
        )
    return False, ""


def increment_failure_count() -> None:
    """ææå¤±ææå¼å« â å¤±æè¨æ¸ +1"""
    state = get_system_state()
    state["scan_failure_count"] = state.get("scan_failure_count", 0) + 1
    set_system_state(state)


def reset_failure_count() -> None:
    """æææåæå¼å« â éç½®å¤±æè¨æ¸"""
    state = get_system_state()
    if state.get("scan_failure_count", 0) > 0:
        state["scan_failure_count"] = 0
        set_system_state(state)


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 9.8 é£çºè§æçæ·
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def check_circuit_breaker(cfg: dict) -> tuple[bool, str, int]:
    """ð æª¢æ¥é£çºè§æçæ· â (æ¯å¦æ«å, è¨æ¯, é£ææ¬¡æ¸)"""
    cb = cfg.get("circuit_breaker", {})
    if not cb.get("enabled", True):
        return False, "", 0

    history = _load_json(TRADE_HISTORY_FILE, [])
    # åªçæè¿ 20 ç­å·²çµæäº¤æï¼å« LOCK éå©ï¼
    recent = [
        t for t in history
        if t.get("close_type") in ("SL", "BE", "LOCK", "TP1", "TP2", "TP3")
    ][-20:]
    if not recent:
        return False, "", 0

    # å¾å°¾å·´å¾åæ¸é£æï¼SL è¨æãTP1/2/3/BE ä¸­æ·é£æï¼
    losses = 0
    last_loss_time: datetime | None = None
    for t in reversed(recent):
        if t.get("close_type") == "SL":
            losses += 1
            if last_loss_time is None:
                try:
                    last_loss_time = datetime.strptime(
                        t["time"], "%Y-%m-%d %H:%M"
                    ).replace(tzinfo=TW_TZ)
                except Exception:
                    last_loss_time = tw_now()
        else:
            break

    if losses == 0 or last_loss_time is None:
        return False, "", 0

    elapsed_h = (tw_now() - last_loss_time).total_seconds() / 3600

    hard_n = cb.get("hard_threshold", 5)
    hard_h = cb.get("hard_pause_hours", 24)
    soft_n = cb.get("soft_threshold", 3)
    soft_h = cb.get("soft_pause_hours", 4)

    if losses >= hard_n and elapsed_h < hard_h:
        return (
            True,
            f"ð¨ *ç¡¬çæ·è§¸ç¼*\né£çº {losses} æ¬¡æ­¢æï¼ç³»çµ±æ«å {hard_h} å°æ\n"
            f"å©é¤ç´ `{hard_h - elapsed_h:.1f}` å°ææ¢å¾©",
            losses,
        )
    if losses >= soft_n and elapsed_h < soft_h:
        return (
            True,
            f"â ï¸ *è»çæ·è§¸ç¼*\né£çº {losses} æ¬¡æ­¢æï¼æ«å {soft_h} å°æ\n"
            f"å©é¤ç´ `{soft_h - elapsed_h:.1f}` å°ææ¢å¾©",
            losses,
        )
    return False, "", losses


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 9.85 v14.1 èªåæ«åçå¹£ + é£æå·éæ
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def is_coin_underperforming(coin: str, cfg: dict) -> tuple[bool, str]:
    """â¸ï¸ æª¢æ¥å®ä¸å¹£ç¨®éå» N å¤©æ¯å¦è¡¨ç¾å¤ªå·®ï¼è¦èªåæ«å"""
    cap_cfg = cfg.get("coin_auto_pause", {})
    if not cap_cfg.get("enabled", True):
        return False, ""

    days = cap_cfg.get("days", 7)
    min_trades = cap_cfg.get("min_trades", 5)
    max_wr = cap_cfg.get("max_winrate", 0.30)

    history = _load_json(TRADE_HISTORY_FILE, [])
    cutoff_ts = time.time() - days * 86400

    recent = []
    for t in history:
        if t.get("coin") != coin:
            continue
        try:
            t_dt = datetime.strptime(t["time"], "%Y-%m-%d %H:%M").replace(tzinfo=TW_TZ)
            if t_dt.timestamp() > cutoff_ts:
                recent.append(t)
        except Exception:
            continue

    if len(recent) < min_trades:
        return False, ""

    wins = sum(1 for t in recent if t.get("close_type") in ("TP1", "TP2", "TP3", "LOCK"))
    wr = wins / len(recent)
    if wr < max_wr:
        return True, (
            f"{coin} éå» {days} å¤© {len(recent)} ç­ï¼"
            f"åç `{wr:.0%}` < `{max_wr:.0%}` â æ«å {cap_cfg.get('pause_hours', 24)}h"
        )
    return False, ""


def get_direction_bias() -> tuple[str | None, int, str]:
    """ð å¾æ­·å²äº¤æç®åºå¤ç©ºæ¹ååå¥½ â (åå¥½æ¹å, å åé, èªªæ)"""
    cfg = load_config()
    db_cfg = cfg.get("direction_bias", {})
    if not db_cfg.get("enabled", True):
        return None, 0, ""

    min_diff = db_cfg.get("min_diff_pct", 15)
    min_samples = db_cfg.get("min_samples", 10)
    bonus = db_cfg.get("bonus", 3)

    history = _load_json(TRADE_HISTORY_FILE, [])
    closed = [t for t in history if t.get("close_type") in ("SL", "BE", "LOCK", "TP1", "TP2", "TP3")]

    longs = [t for t in closed if t.get("side") == "LONG"]
    shorts = [t for t in closed if t.get("side") == "SHORT"]
    if len(longs) < min_samples or len(shorts) < min_samples:
        return None, 0, ""

    long_wins = sum(1 for t in longs if t["close_type"] in ("TP1", "TP2", "TP3", "LOCK"))
    short_wins = sum(1 for t in shorts if t["close_type"] in ("TP1", "TP2", "TP3", "LOCK"))
    long_wr = long_wins / len(longs) * 100
    short_wr = short_wins / len(shorts) * 100
    diff = long_wr - short_wr

    if abs(diff) < min_diff:
        return None, 0, ""
    preferred = "LONG" if diff > 0 else "SHORT"
    return preferred, bonus, f"{preferred} æ­·å²åç {long_wr if preferred == 'LONG' else short_wr:.0f}% è¼é«ï¼å·® {abs(diff):.0f}%ï¼"


def format_direction_stats() -> str:
    """ð æ¹ååççµ±è¨å ±è¡¨ï¼çµ¦ /direction å½ä»¤ç¨ï¼"""
    history = _load_json(TRADE_HISTORY_FILE, [])
    closed = [t for t in history if t.get("close_type") in ("SL", "BE", "LOCK", "TP1", "TP2", "TP3")]
    longs = [t for t in closed if t.get("side") == "LONG"]
    shorts = [t for t in closed if t.get("side") == "SHORT"]

    def calc_stats(trades):
        n = len(trades)
        if n == 0:
            return None
        wins = sum(1 for t in trades if t["close_type"] in ("TP1", "TP2", "TP3", "LOCK"))
        loss = sum(1 for t in trades if t["close_type"] == "SL")
        be = sum(1 for t in trades if t["close_type"] == "BE")
        pnl = sum(t.get("pnl", 0) for t in trades)
        return {"n": n, "win": wins, "loss": loss, "be": be, "wr": wins / n * 100, "pnl": pnl}

    l = calc_stats(longs)
    s = calc_stats(shorts)

    lines = ["ð *æ¹ååççµ±è¨*", "ââââââââââââââ"]
    if l:
        lines.append(
            f"ð¢ LONGï¼{l['n']} ç­ï¼å {l['win']} / å¹³ {l['be']} / æ {l['loss']}ï¼"
        )
        lines.append(f"   åç `{l['wr']:.0f}%` Â· PnL `{l['pnl']:+.2f}%`")
    else:
        lines.append("ð¢ LONGï¼æ«ç¡è³æ")
    if s:
        lines.append(
            f"ð´ SHORTï¼{s['n']} ç­ï¼å {s['win']} / å¹³ {s['be']} / æ {s['loss']}ï¼"
        )
        lines.append(f"   åç `{s['wr']:.0f}%` Â· PnL `{s['pnl']:+.2f}%`")
    else:
        lines.append("ð´ SHORTï¼æ«ç¡è³æ")

    bias_dir, bias_amount, bias_note = get_direction_bias()
    if bias_dir:
        lines.append("")
        lines.append(f"ð¯ *ç³»çµ±ç¶ååå¥½ï¼{bias_dir}*")
        lines.append(f"   {bias_note}")
        lines.append(f"   ä¸æ¬¡åæ¹åè¨è +{bias_amount} / åæ¹å -{bias_amount}")
    else:
        lines.append("")
        lines.append("âï¸ ç³»çµ±æªåå¥½æ¹åï¼è³æä¸è¶³æåçæ¥è¿ï¼")
    return "\n".join(lines)


def format_audit_report() -> str:
    """ð¬ ææ¨æææ§å¯©æ¥ â æäº¤æåæãæ»¿è¶³ X æ¢ä»¶ vs ä¸æ»¿è¶³ãå°æ¯åç

    é©è­ v14 å çææè©åé æ¯å¦ççææï¼
      - ç¥ç´è¨èï¼95+ï¼vs ä¸è¬ï¼80-94ï¼
      - MTF 1H é å¢ vs ä¸­æ§ / åå
      - é«éè½ï¼â¥1.5Ãï¼vs ä½éè½ï¼<1Ãï¼
      - å¤é ­ vs ç©ºé ­
      - è¶¨å¢å¸ vs éçªå¸
      - EMA å®ç¾æå vs å¶ä»
    """
    history = _load_json(TRADE_HISTORY_FILE, [])
    closed = [
        t for t in history
        if t.get("close_type") in ("SL", "BE", "LOCK", "TP1", "TP2", "TP3", "OB_FAIL")
    ]
    n_closed = len(closed)
    if n_closed < 10:
        return (
            f"ð­ *ææ¨æææ§å¯©æ¥*\n\n"
            f"è³æä¸è¶³ï¼{n_closed} ç­ < 10ï¼ã\n"
            f"è³å°ç´¯ç© 10 ç­å·²çµæäº¤ææè½å¯©æ¥ææ¨æåº¦ã"
        )

    def stats(trades):
        n = len(trades)
        if n == 0:
            return None
        wins = sum(1 for t in trades if t["close_type"] in ("TP1", "TP2", "TP3", "LOCK"))
        return {"n": n, "wr": wins / n * 100}

    def _verdict(diff_pct: float) -> str:
        if diff_pct > 10:
            return "â"
        if diff_pct > 0:
            return "â ï¸"
        return "â"

    overall = stats(closed)
    lines = [
        f"ð¬ *ææ¨æææ§å¯©æ¥*",
        f"ââââââââââââââ",
        f"æ¨£æ¬ï¼{n_closed} ç­å·²çµæäº¤æ",
        f"æ´é«åçï¼`{overall['wr']:.0f}%`",
        f"",
    ]

    sections = []

    # 1ï¸â£ ç¥ç´è¨èï¼95+ï¼vs ä¸è¬ï¼80-94ï¼
    god = [t for t in closed if t.get("score", 0) >= 95]
    normal = [t for t in closed if 80 <= t.get("score", 0) < 95]
    if len(god) >= 2 and len(normal) >= 5:
        g = stats(god)
        nm = stats(normal)
        diff = g["wr"] - nm["wr"]
        sections.append(
            f"{_verdict(diff)} *ç¥ç´è¨è vs ä¸è¬*\n"
            f"  ç¥ç´ï¼95+ï¼ï¼{g['n']} ç­ / `{g['wr']:.0f}%`\n"
            f"  ä¸è¬ï¼80-94ï¼ï¼{nm['n']} ç­ / `{nm['wr']:.0f}%`\n"
            f"  å·®ç°ï¼`{diff:+.0f}%`"
        )

    # 2ï¸â£ MTF 1H é å¢ vs ä¸­æ§
    mtf_aligned = [t for t in closed if (t.get("features") or {}).get("mtf_h1", 0) == 1.0]
    mtf_other = [t for t in closed if (t.get("features") or {}).get("mtf_h1", 1.0) == 0.0]
    if len(mtf_aligned) >= 3 and len(mtf_other) >= 3:
        a = stats(mtf_aligned)
        o = stats(mtf_other)
        diff = a["wr"] - o["wr"]
        sections.append(
            f"{_verdict(diff)} *MTF 1H é å¢ vs ä¸­æ§*\n"
            f"  é å¢ï¼{a['n']} ç­ / `{a['wr']:.0f}%`\n"
            f"  ä¸­æ§ï¼{o['n']} ç­ / `{o['wr']:.0f}%`\n"
            f"  å·®ç°ï¼`{diff:+.0f}%`"
        )

    # 3ï¸â£ é«éè½ vs ä½éè½
    high_vol = [t for t in closed if (t.get("features") or {}).get("vol_ratio", 1.0) >= 1.5]
    low_vol = [t for t in closed if (t.get("features") or {}).get("vol_ratio", 1.0) < 1.0]
    if len(high_vol) >= 3 and len(low_vol) >= 3:
        h = stats(high_vol)
        l = stats(low_vol)
        diff = h["wr"] - l["wr"]
        sections.append(
            f"{_verdict(diff)} *é«éè½ vs ä½éè½*\n"
            f"  é«éï¼â¥1.5Ãï¼ï¼{h['n']} ç­ / `{h['wr']:.0f}%`\n"
            f"  ä½éï¼<1Ãï¼ï¼{l['n']} ç­ / `{l['wr']:.0f}%`\n"
            f"  å·®ç°ï¼`{diff:+.0f}%`"
        )

    # 4ï¸â£ ADX è¶¨å¢å¸ vs éçªå¸
    trend_mkt = [t for t in closed if (t.get("regime") or {}).get("regime") == "trend"]
    range_mkt = [t for t in closed if (t.get("regime") or {}).get("regime") == "range"]
    if len(trend_mkt) >= 3 and len(range_mkt) >= 3:
        t_st = stats(trend_mkt)
        r_st = stats(range_mkt)
        diff = t_st["wr"] - r_st["wr"]
        sections.append(
            f"{_verdict(diff)} *è¶¨å¢å¸ vs éçªå¸*\n"
            f"  è¶¨å¢å¸ï¼ADX>25ï¼ï¼{t_st['n']} ç­ / `{t_st['wr']:.0f}%`\n"
            f"  éçªå¸ï¼ADX<18ï¼ï¼{r_st['n']} ç­ / `{r_st['wr']:.0f}%`\n"
            f"  å·®ç°ï¼`{diff:+.0f}%`"
        )

    # 5ï¸â£ å¤ç©ºæ¹å
    longs = [t for t in closed if t.get("side") == "LONG"]
    shorts = [t for t in closed if t.get("side") == "SHORT"]
    if longs and shorts:
        l_st = stats(longs)
        s_st = stats(shorts)
        diff = l_st["wr"] - s_st["wr"]
        balance_emoji = "â" if abs(diff) < 10 else "â ï¸" if abs(diff) < 20 else "â"
        sections.append(
            f"{balance_emoji} *æ¹åå¹³è¡¡*\n"
            f"  LONGï¼{l_st['n']} ç­ / `{l_st['wr']:.0f}%`\n"
            f"  SHORTï¼{s_st['n']} ç­ / `{s_st['wr']:.0f}%`\n"
            f"  å·®ç°ï¼`{diff:+.0f}%`"
        )

    if sections:
        lines.append("\n\n".join(sections))
        lines.append("")
    else:
        lines.append("åé åçµæ¨£æ¬ä¸è¶³ï¼éç´¯ç©æ´å¤äº¤æ")
        lines.append("")

    lines.append("ð¡ *å¤è®æ¨æº*")
    lines.append("  â = è©²é ææ¨ææï¼å·®ç° > 10%ï¼")
    lines.append("  â ï¸ = ééææï¼å·®ç° 0â10%ï¼")
    lines.append("  â = ååéä¿ï¼å»ºè­°éæ¬æééï¼")
    return "\n".join(lines)


def is_coin_overheating(coin: str, cfg: dict) -> tuple[bool, str]:
    """ð¥ éåº¦éä¸­ä¿è­·ï¼æå¹£é£ N åå¾æ«åä¸è¼ª"""
    oh_cfg = cfg.get("overheating", {})
    if not oh_cfg.get("enabled", True):
        return False, ""

    threshold = oh_cfg.get("win_streak_threshold", 3)
    cooldown_h = oh_cfg.get("cooldown_hours", 4)

    history = _load_json(TRADE_HISTORY_FILE, [])
    coin_closed = [
        t for t in history
        if t.get("coin") == coin
        and t.get("close_type") in ("SL", "BE", "LOCK", "TP1", "TP2", "TP3")
    ]
    if len(coin_closed) < threshold:
        return False, ""

    last_n = coin_closed[-threshold:]
    if not all(t["close_type"] in ("TP1", "TP2", "TP3", "LOCK") for t in last_n):
        return False, ""

    try:
        last_win_dt = datetime.strptime(last_n[-1]["time"], "%Y-%m-%d %H:%M").replace(tzinfo=TW_TZ)
    except Exception:
        return False, ""

    elapsed_h = (tw_now() - last_win_dt).total_seconds() / 3600
    if elapsed_h < cooldown_h:
        remaining = cooldown_h - elapsed_h
        return True, (
            f"{coin} å·²é£ {threshold} åï¼æ«åä¸è¼ªé¿åéåº¦ä¾è³´ï¼å©é¤ `{remaining:.1f}h`ï¼"
        )
    return False, ""


def check_cooling_off(cfg: dict) -> tuple[bool, int, str]:
    """âï¸ é£æå·éæ â (æ¯å¦å·éä¸­, å©é¤ç§æ¸, èªªæ)"""
    co_cfg = cfg.get("cooling_off", {})
    if not co_cfg.get("enabled", True):
        return False, 0, ""

    threshold = co_cfg.get("loss_threshold", 2)
    period_min = co_cfg.get("period_minutes", 30)

    history = _load_json(TRADE_HISTORY_FILE, [])
    closed = [t for t in history if t.get("close_type") in ("SL", "BE", "LOCK", "TP1", "TP2", "TP3")]
    if len(closed) < threshold:
        return False, 0, ""

    last_n = closed[-threshold:]
    if not all(t.get("close_type") == "SL" for t in last_n):
        return False, 0, ""

    try:
        last_sl_dt = datetime.strptime(last_n[-1]["time"], "%Y-%m-%d %H:%M").replace(tzinfo=TW_TZ)
    except Exception:
        return False, 0, ""

    elapsed = (tw_now() - last_sl_dt).total_seconds()
    cooling_sec = period_min * 60
    if elapsed < cooling_sec:
        remaining = int(cooling_sec - elapsed)
        return True, remaining, (
            f"é£ {threshold} æå·éæï¼å©é¤ `{remaining // 60}` åéå¾æ¢å¾©éæ°å®"
        )
    return False, 0, ""


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 9.87 v14.6 å´æ ¼æ¯æ¥é¢¨æ§
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def get_today_stats() -> dict:
    """ð ä»æ¥äº¤æçµ±è¨ï¼ä¾å°ç£æéæ¥æï¼"""
    today_str = tw_now().strftime("%Y-%m-%d")
    history = _load_json(TRADE_HISTORY_FILE, [])
    today_trades = [t for t in history if t.get("date") == today_str]
    closed = [
        t for t in today_trades
        if t.get("close_type") in ("SL", "BE", "LOCK", "TP1", "TP2", "TP3", "OB_FAIL")
    ]
    return {
        "trades_count": len(today_trades),
        "closed_count": len(closed),
        "pnl_pct": sum(t.get("pnl", 0) for t in closed),
        "wins": sum(1 for t in closed if t.get("close_type") in ("TP1", "TP2", "TP3", "LOCK")),
        "losses": sum(1 for t in closed if t.get("close_type") == "SL"),
    }


def check_daily_limits(cfg: dict, tracker) -> tuple[bool, str]:
    """ð¡ï¸ æ¯æ¥é¢¨æ§æª¢æ¥ â (æ¯å¦æ«å, è¨æ¯)

    ä¸æ¢ç´ç·ï¼
      1. åææåæ¸ä¸éï¼max_concurrent_positionsï¼
      2. ç¶æ¥æå¤±ä¸éï¼daily_loss_limit_pctï¼
      3. æ¯æ¥è¨èæ¸ä¸éï¼max_daily_signalsï¼
    """
    dl_cfg = cfg.get("daily_limits", {})
    if not dl_cfg.get("enabled", True):
        return False, ""

    stats = get_today_stats()

    # â  åææåæ¸
    max_concurrent = dl_cfg.get("max_concurrent_positions", 2)
    open_count = sum(
        1 for s in tracker.signals.values()
        if s.get("status") in ("PENDING", "ACTIVE", "BE", "TRAIL")
    )
    if open_count >= max_concurrent:
        return True, (
            f"ð¦ æåæ¸å·²éä¸éï¼éå®ä¸­ *{open_count}* / ä¸é *{max_concurrent}*"
        )

    # â¡ ç¶æ¥ç´¯è¨æå¤±
    loss_limit = dl_cfg.get("daily_loss_limit_pct", 5.0)
    if stats["pnl_pct"] < -loss_limit:
        return True, (
            f"â ï¸ ç¶æ¥ PnL `{stats['pnl_pct']:.2f}%` å·²è·ç ´åæç´ç· `-{loss_limit}%`"
            f"ï¼{stats['losses']} æ / {stats['wins']} åï¼ï¼åæ­¢éæ°å®å°éå¤©"
        )

    # â¢ æ¯æ¥è¨èæ¸
    max_daily = dl_cfg.get("max_daily_signals", 6)
    if stats["trades_count"] >= max_daily:
        return True, (
            f"ð ä»æ¥è¨èæ¸ *{stats['trades_count']}* å·²éä¸é *{max_daily}*ï¼åæ­¢éæ°å®"
        )

    return False, ""


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 9.9 ééµææ®µéæ¿¾
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def _in_window(cur_min: int, start_min: int, end_min: int) -> bool:
    """æ¯æ´è·¨åå¤ææ®µï¼å¦ 23:50â00:10ï¼"""
    if start_min <= end_min:
        return start_min <= cur_min < end_min
    return cur_min >= start_min or cur_min < end_min


def is_in_news_window(cfg: dict) -> tuple[bool, str]:
    """ð° æ°èäºä»¶ææ®µæª¢æ¥ï¼èªè¨äºä»¶ + NFP èªåè¦åï¼"""
    now = tw_now()

    # 1. config ä¸­çèªè¨äºä»¶
    for nb in cfg.get("news_blackouts", []):
        try:
            start = datetime.fromisoformat(nb["start"])
            end = datetime.fromisoformat(nb["end"])
            if start.tzinfo is None:
                start = start.replace(tzinfo=TW_TZ)
                end = end.replace(tzinfo=TW_TZ)
            if start <= now <= end:
                return True, nb.get("reason", "æ°èäºä»¶")
        except Exception:
            continue

    # 2. NFP èªåè¦åï¼æ¯æç¬¬ä¸åé±äº 21:25â22:30ï¼å°ç£æéï¼
    auto = cfg.get("auto_news_blackout", {})
    if auto.get("nfp", True):
        if now.weekday() == 4 and now.day <= 7:
            cur = now.hour * 60 + now.minute
            if 21 * 60 + 25 <= cur < 22 * 60 + 30:
                return True, "NFP éè¾²ï¼èªååµæ¸¬ï¼"

    # 3. CPI ç´è«æ¯æä¸­æ¬ 21:25â22:30
    if auto.get("cpi", True):
        if 10 <= now.day <= 16:
            cur = now.hour * 60 + now.minute
            if 21 * 60 + 25 <= cur < 22 * 60 + 30:
                return True, "CPI æ¸æææ®µï¼èªååµæ¸¬ï¼"

    return False, ""


def is_blackout_time(cfg: dict) -> tuple[bool, str]:
    """ð æª¢æ¥ç¶åæ¯å¦å¨ç¦æ­¢äº¤æææ®µï¼å°ç£æéï¼"""
    windows = cfg.get("blackout_windows_tw", [])
    now = tw_now()
    cur_min = now.hour * 60 + now.minute
    for w in windows:
        try:
            sh, sm = map(int, w["start"].split(":"))
            eh, em = map(int, w["end"].split(":"))
            if _in_window(cur_min, sh * 60 + sm, eh * 60 + em):
                return True, w.get("reason", "ç¦æ­¢ææ®µ")
        except Exception:
            continue
    return False, ""


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 10. è¨èè¿½è¹¤
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
class SignalTracker:
    def __init__(self, filepath: str = ACTIVE_SIGNALS_FILE):
        self.filepath = filepath
        self.signals: dict = _load_json(filepath, {})
        self.transitions = 0

    def _save(self) -> None:
        _save_json(self.filepath, self.signals)

    def add(self, signal: dict, active: bool = False) -> tuple[str, str]:
        """æ°å¢è¨è â åå³ (key, order_id)"""
        order_id = f"{int(time.time())}-{uuid.uuid4().hex[:8].upper()}"
        key = f"{signal['instId']}_{signal['side']}_{order_id}"
        now_ts = time.time()
        self.signals[key] = {
            **signal,
            "order_id": order_id,
            "status": "ACTIVE" if active else "PENDING",
            "hit_tp1": False,
            "hit_tp2": False,
            "hit_tp3": False,
            "activated_at": now_ts if active else None,
            "entry_message_id": None,
            # ðª¡ æ­·å²æéè£æçæ¸¸æ¨ï¼ç§ï¼ï¼ä¸æ¬¡ _check_one å¾éä¹å¾ç K ç·éå§æ
            "last_checked_ts": now_ts if active else None,
        }
        self._save()
        logging.info(f"ð æ°å¢è¨å®ï¼{order_id} ({signal['instId']} {signal['side']})")
        return key, order_id

    def set_entry_message_id(self, key: str, message_id: int | None) -> None:
        if key in self.signals and message_id:
            self.signals[key]["entry_message_id"] = message_id
            self._save()

    def _send_postmortem(self, sig: dict, mode: str) -> None:
        """ð SL/BE/LOCK/OB_FAIL å¾éè¦ç¤åæè¨æ¯ï¼ä¸åéé»å¤±æï¼"""
        coin = sig.get("instId", "?").split("-")[0]
        order_id = sig.get("order_id", "?")

        try:
            cfg = load_config()
            pm_cfg = cfg.get("post_mortem", {})
            if not pm_cfg.get("enabled", True):
                return
            if mode == "LOCK" and pm_cfg.get("loss_only", False):
                return  # LOCK ä¸ç®æï¼loss_only æ¨¡å¼ä¸è·³é

            activated_at = sig.get("activated_at") or sig.get("created") or 0
            all_candles = fetch_candles_full(sig["instId"], limit=100)
            df_at_loss = [
                {"ts": c["ts"], "o": c["o"], "h": c["h"], "l": c["l"], "c": c["c"], "v": c["v"]}
                for c in all_candles
                if (c["ts"] / 1000) >= (activated_at - 900)
            ]

            # ð¡ï¸ è³æä¸è¶³ä¹è¦éï¼é¿åãçºä»éº¼æ²åå ï¼ã
            if len(df_at_loss) < 10:
                send_tg(
                    f"ð *{coin} è¦ç¤*\n"
                    f"ââââââââââââââ\n"
                    f"ð è¨å®ï¼`{order_id}`\n"
                    f"â° æéï¼{tw_ts()}\n"
                    f"\n"
                    f"ð *çµè«ï¼é²å ´å¾è³æå¤ªå°ï¼å {len(df_at_loss)} æ ¹ K ç·ï¼*\n"
                    f"\n"
                    f"ð¡ å¯è½åå ï¼\n"
                    f"  â¢ è¨èåéæ²å¤ä¹å°±è¢«æéææ\n"
                    f"  â¢ é²å ´æéè·ç¾å¨ < 15 åé\n"
                    f"\n"
                    f"å»ºè­°æåç¿» K ç·çæ¯åªæ ¹ K è§¸ç¼ SLï¼ä¸¦æ³¨ææ¯å¦é«æ³¢åææ®µ",
                    reply_to_message_id=sig.get("entry_message_id"),
                )
                return

            reasons = analyze_loss(sig, df_at_loss)
            lessons = _generate_lessons(reasons)
            similar = get_similar_stats(
                sig.get("score", 0),
                sig["side"],
                sig.get("detail", {}),
                sig.get("funding_rate"),
                coin,
            )

            msg = _fmt_postmortem(sig, mode, reasons, lessons, similar)
            send_tg(msg, reply_to_message_id=sig.get("entry_message_id"))

            if mode == "LOSS":
                record_loss_reason(coin, sig["side"], reasons)
        except Exception as e:
            logging.error(f"â è¦ç¤åæå¤±æï¼{e}")
            # ð¡ï¸ ä¾å¤ä¹é fallbackï¼ä¸åéé»
            try:
                send_tg(
                    f"ð *{coin} è¦ç¤é¯èª¤*\n"
                    f"ââââââââââââââ\n"
                    f"ð è¨å®ï¼`{order_id}`\n"
                    f"\n"
                    f"â ï¸ è¦ç¤åæç¼çä¾å¤ï¼`{str(e)[:120]}`\n"
                    f"\n"
                    f"è¨å®å·²æ­£å¸¸å¹³åï¼è«æåæª¢è¦ K ç·ã",
                    reply_to_message_id=sig.get("entry_message_id"),
                )
            except Exception:
                pass

    def has_open_position(self, instId: str) -> bool:
        """ð è©²å¹£ç¨®æ¯å¦éææªçµæçè¨èï¼PENDING / ACTIVE / BE / TRAILï¼

        ç¨éï¼é¿åå¨å¹³ååå°åä¸å¹£ç¨®éè¤éåã
        """
        for sig in self.signals.values():
            if sig.get("instId") == instId and sig.get("status") in (
                "PENDING", "ACTIVE", "BE", "TRAIL"
            ):
                return True
        return False

    def check_all(self) -> None:
        """æª¢æ¥ææè¨èä¸¦ç¼ééç¥"""
        self.transitions = 0
        to_remove = []
        for key, sig in list(self.signals.items()):
            if self._check_one(key, sig):
                to_remove.append(key)
        for key in to_remove:
            del self.signals[key]
        if to_remove:
            self._save()

    def _check_one(self, key: str, sig: dict) -> bool:
        """æª¢æ¥å®ä¸è¨è â True ä»£è¡¨çµæï¼è¦å¾è¿½è¹¤ç§»é¤ï¼

        v12.2ï¼æ­·å² K ç·è£æç
          - PENDINGï¼å¹æ ¼é²å¥è§¸ç¼åéæè½ ACTIVE
          - ACTIVE/BE/TRAILï¼æ last_checked_ts ä¹å¾ææ K ç·ï¼ä¾æåºéæ ¹èç
            â³ æ¯æ ¹ K ç·æª¢æ¥ TP1 â TP2 â TP3 â SLï¼SL ç¨æ´æ°å¾çå¼ï¼
            â³ å³ä¾¿ cron æ¼è·ãè¨èæ´»äº 3 å°æææª¢æ¥ï¼æ­·å²æéä¹ä¸ææ¼
          - SL è§¸ç¼æä¾çæèªååé¡ï¼æ­¢æ(LOSS) / ä¿æ¬(BE) / éå©(LOCK)
        """
        try:
            price = fetch_price(sig["instId"])
            if price <= 0:
                return False

            sig["current_price"] = price
            status = sig["status"]

            # ââ PENDINGï¼ç­å¾é²å ´ ââ
            if status == "PENDING":
                return self._check_pending(sig, price)

            if status not in ("ACTIVE", "BE", "TRAIL"):
                return False

            # ââ æ last_checked_ts ä¹å¾çææ K ç·ï¼ä¾æåºèç ââ
            all_candles = fetch_candles_full(sig["instId"])
            last_ts_s = (
                sig.get("last_checked_ts")
                or sig.get("activated_at")
                or sig.get("created")
                or 0
            )
            last_ts_ms = int(last_ts_s * 1000)
            new_candles = [c for c in all_candles if c["ts"] > last_ts_ms]

            # ðª v14.7ï¼å³æå¹åä½µé²æå¾ä¸æ ¹ K ç·ï¼OKX K ç· API å¶æ 5â10 ç§å»¶é²ï¼
            # å³æ ticker æ¯ K ç·æ´å¿«åæ ååçæéï¼
            if new_candles and price > 0:
                last = dict(new_candles[-1])
                last["h"] = max(last["h"], price)
                last["l"] = min(last["l"], price)
                new_candles[-1] = last

            for c in new_candles:
                if self._process_candle(sig, c):
                    return True

            # ææ¸¸æ¨æ¨é²å°æå¾ä¸æ ¹ãå·²æ¶ç·ãK ç·ï¼æªæ¶ç·ä¸æ¬¡åæï¼
            confirmed = [c for c in new_candles if c["confirmed"]]
            if confirmed:
                sig["last_checked_ts"] = max(c["ts"] for c in confirmed) / 1000.0

            self._save()
            return False
        except Exception as e:
            logging.error(f"â check_one [{key}] é¯èª¤ï¼{e}")
            return False

    def _check_pending(self, sig: dict, price: float) -> bool:
        """PENDING çææª¢æ¥ï¼ç­å¾å¹æ ¼é²å¥åéè½ ACTIVEï¼éæèªååæ¶"""
        coin = sig["instId"].split("-")[0]
        order_id = sig.get("order_id", "N/A")
        side = sig["side"]
        entry, sl = sig["entry"], sig["sl"]
        tp1, tp2, tp3 = sig["tp1"], sig["tp2"], sig["tp3"]
        kb = _order_keyboard(order_id)

        if time.time() > sig["expires"]:
            send_tg(
                f"â° *{coin} è¨èéæ*\n"
                f"ð è¨å®ï¼`{order_id}`\n"
                f"é²å ´ `{entry:.4f}` æªè§¸ç¼ï¼å·²èªååæ¶"
            )
            self.transitions += 1
            return True

        in_zone = (
            side == "LONG"
            and entry * (1 - 0.006) <= price <= entry * (1 + 0.002)
        ) or (
            side == "SHORT"
            and entry * (1 - 0.002) <= price <= entry * (1 + 0.006)
        )
        if in_zone:
            now_ts = time.time()
            sig["status"] = "ACTIVE"
            sig["activated_at"] = now_ts
            sig["last_checked_ts"] = now_ts
            msg_id = send_tg(
                _fmt_entry(
                    coin, side, order_id, price, entry, sl,
                    tp1, tp2, tp3, sig["score"], sig.get("funding_rate"),
                    detail=sig.get("detail"),
                ),
                reply_markup=kb,
            )
            if msg_id:
                sig["entry_message_id"] = msg_id
            self._save()
            self.transitions += 1
        return False

    def _process_candle(self, sig: dict, candle: dict) -> bool:
        """å°å®ä¸ K ç·æª¢æ¥ TP1 â TP2 â TP3 â SL â True ä»£è¡¨è¨èçµæ

        - ç¨ K ç·ç high / low ä½æ¥µå¼ï¼èªç¶æ¶µèæéï¼
        - å¤ TP å¨åä¸æ ¹ K ç·é½è§¸å°æï¼ä¾åºæ´æ° SLï¼TP1âä¿æ¬ãTP2âéå©ï¼
        - èçå®ææ TP å¾ï¼åç¨ãæçµ SL å¼ãæª¢æ¥ SL æ¯å¦è§¸ç¼
        """
        side = sig["side"]
        entry = sig["entry"]
        sl = sig["sl"]
        tp1, tp2, tp3 = sig["tp1"], sig["tp2"], sig["tp3"]
        coin = sig["instId"].split("-")[0]
        order_id = sig.get("order_id", "N/A")
        reply_to = sig.get("entry_message_id")
        kb = _order_keyboard(order_id)
        ch, cl, cc = candle["h"], candle["l"], candle["c"]

        if side == "LONG":
            favor_hit = lambda t: ch >= t
            against_hit = lambda t: cl <= t
            wick_favor = lambda t: cc < t and ch >= t        # æ¶ç¤æªå°ãå½±ç·è§¸å
            wick_against = lambda t: cc > t and cl <= t      # æ¶ç¤æªç ´ãå½±ç·æé
        else:
            favor_hit = lambda t: cl <= t
            against_hit = lambda t: ch >= t
            wick_favor = lambda t: cc > t and cl <= t
            wick_against = lambda t: cc < t and ch >= t

        # ð§± OB å¤±æéå ´ï¼åå¨éæ²å° TP1 åæª¢æ¥ï¼
        if not sig.get("hit_tp1"):
            ob_zone = sig.get("ob_zone")
            cfg_oi = load_config().get("ob_invalidation", {})
            if ob_zone and cfg_oi.get("enabled", True):
                buf = cfg_oi.get("break_buffer_pct", 0.2) / 100
                ob_low = ob_zone.get("low", 0)
                ob_high = ob_zone.get("high", 0)
                # LONGï¼OB low æ¶ç¤è¢«æç©¿ â å¤±æ
                # SHORTï¼OB high æ¶ç¤è¢«çªç ´ â å¤±æ
                broken = (
                    side == "LONG" and cc < ob_low * (1 - buf)
                ) or (
                    side == "SHORT" and cc > ob_high * (1 + buf)
                )
                if broken:
                    pnl = (
                        (cc - entry) / entry * 100
                        if side == "LONG"
                        else (entry - cc) / entry * 100
                    )
                    send_tg(
                        f"â ï¸ *{coin} OB å¤±æï¼ä¸»åéå ´*\n"
                        f"ââââââââââââââ\n"
                        f"ð è¨å®ï¼`{order_id}`\n"
                        f"â° æéï¼{tw_ts()}\n"
                        f"æ¹åï¼{'åå¤' if side == 'LONG' else 'åç©º'}\n"
                        f"éå ´å¹ï¼`{cc:.4f}`\n"
                        f"çµç®ï¼`{pnl:+.2f}%`\n"
                        f"\n"
                        f"ð¡ é²å ´ä¾æç SMC è¨å®å¡å·²è¢«æ¶ç¤è·ç ´\n"
                        f"   çµæ§å¤±æï¼æåéå ´é¿åæ´å¤§è§æ",
                        reply_markup=kb,
                        reply_to_message_id=reply_to,
                    )
                    record_trade(coin, side, order_id, entry, cc, "OB_FAIL", sig["score"], sig)
                    # ð OB å¤±æä¹éè¦ç¤åæ
                    self._send_postmortem(sig, "LOSS")
                    self.transitions += 1
                    return True

        # ð¥ TP1
        if not sig.get("hit_tp1") and favor_hit(tp1):
            sig["hit_tp1"] = True
            sig["sl"] = entry
            sig["status"] = "BE"
            sl = entry
            pnl = (
                (tp1 - entry) / entry * 100
                if side == "LONG"
                else (entry - tp1) / entry * 100
            )
            send_tg(
                _fmt_tp(
                    coin, side, order_id, "TP1", tp1, pnl, 1.5,
                    wick_triggered=wick_favor(tp1),
                ),
                reply_markup=kb,
                reply_to_message_id=reply_to,
            )
            record_trade(coin, side, order_id, entry, tp1, "TP1", sig["score"], sig)
            self._save()
            self.transitions += 1

        # ð¥ TP2
        if not sig.get("hit_tp2") and favor_hit(tp2):
            sig["hit_tp2"] = True
            sig["sl"] = tp1
            sig["status"] = "TRAIL"
            sl = tp1
            pnl = (
                (tp2 - entry) / entry * 100
                if side == "LONG"
                else (entry - tp2) / entry * 100
            )
            send_tg(
                _fmt_tp(
                    coin, side, order_id, "TP2", tp2, pnl, 3.0,
                    wick_triggered=wick_favor(tp2),
                ),
                reply_markup=kb,
                reply_to_message_id=reply_to,
            )
            record_trade(coin, side, order_id, entry, tp2, "TP2", sig["score"], sig)
            self._save()
            self.transitions += 1

        # ð TP3 â çµæ
        if not sig.get("hit_tp3") and favor_hit(tp3):
            sig["hit_tp3"] = True
            pnl = (
                (tp3 - entry) / entry * 100
                if side == "LONG"
                else (entry - tp3) / entry * 100
            )
            send_tg(
                _fmt_tp(
                    coin, side, order_id, "TP3", tp3, pnl, 5.0,
                    wick_triggered=wick_favor(tp3),
                ),
                reply_markup=kb,
                reply_to_message_id=reply_to,
            )
            record_trade(coin, side, order_id, entry, tp3, "TP3", sig["score"], sig)
            self.transitions += 1
            return True

        # ð SLï¼ç¨æ´æ°å¾ç sl å¼ï¼â ä¾çæåé¡
        if against_hit(sl):
            if sig.get("hit_tp2"):
                mode, r_value, close_type = "LOCK", 1.5, "LOCK"
            elif sig.get("hit_tp1"):
                mode, r_value, close_type = "BE", 0.0, "BE"
            else:
                mode, r_value, close_type = "LOSS", -1.0, "SL"
            pnl = (
                (sl - entry) / entry * 100
                if side == "LONG"
                else (entry - sl) / entry * 100
            )
            send_tg(
                _fmt_sl(
                    coin, side, order_id, sl, pnl, mode, r_value,
                    wick_triggered=wick_against(sl),
                ),
                reply_markup=kb,
                reply_to_message_id=reply_to,
            )
            record_trade(coin, side, order_id, entry, sl, close_type, sig["score"], sig)
            # ð è¦ç¤åæ
            self._send_postmortem(sig, mode)
            self.transitions += 1
            return True

        return False

    def send_position_updates(self) -> None:
        """ð ç¼éæææåçé²åº¦æ´æ°

        v14.7 å  15 åé throttleï¼æ¯ 15 åéæå¤éä¸æ¬¡ï¼
        é¿å 1 åé cron æ TP/SL éæ¨ç­éè¦è¨æ¯æ´å°ä¸é¢å»ã
        """
        state = get_system_state()
        now = time.time()
        last_sent = state.get("last_position_update_ts", 0)
        interval = 15 * 60  # 15 åé
        if now - last_sent < interval:
            return

        cnt = 0
        for sig in self.signals.values():
            if sig["status"] not in ("ACTIVE", "BE", "TRAIL"):
                continue
            price = fetch_price(sig["instId"])
            if price <= 0:
                continue
            send_tg(
                _fmt_position(sig, price),
                reply_markup=_order_keyboard(sig.get("order_id", "")),
                reply_to_message_id=sig.get("entry_message_id"),
            )
            cnt += 1
        if cnt:
            state["last_position_update_ts"] = now
            set_system_state(state)
            logging.info(f"ð å·²ç¼é {cnt} ç­æåæ´æ°ï¼ä¸æ¬¡ææ© 15 åéå¾ï¼")

    def get_position_stats(self) -> str:
        """ð æåçµ±è¨ï¼çµ¦ /stats å½ä»¤ç¨ï¼"""
        positions = list(self.signals.values())
        if not positions:
            return "ð­ *ç®åç¡æå*\n\nð ç³»çµ±æçºææä¸­..."

        lines = [f"ð *è¿½è¹¤ä¸­è¨èï¼{len(positions)} ç­ï¼*", "â" * 22, ""]
        for i, p in enumerate(positions):
            price = fetch_price(p["instId"]) or p["entry"]
            coin = p["instId"].split("-")[0]
            coin_emoji = (
                "ð " if "BTC" in p["instId"] else "ð·" if "ETH" in p["instId"] else "ð£"
            )
            side_emoji = "ð¢" if p["side"] == "LONG" else "ð´"
            order_id = p.get("order_id", "N/A")
            pnl = (
                (price - p["entry"]) / p["entry"] * 100
                if p["side"] == "LONG"
                else (p["entry"] - price) / p["entry"] * 100
            )
            pnl_emoji = "ð¢" if pnl >= 0 else "ð´"
            progress = (
                "ð TP3"
                if p.get("hit_tp3")
                else "ð¥ TP2"
                if p.get("hit_tp2")
                else "ð¥ TP1"
                if p.get("hit_tp1")
                else "â³ ç­å¾"
            )
            lines.append(
                f"{coin_emoji} *#{coin}* Â· {side_emoji} {p['side']} Â· {p.get('score', 0)} å\n"
                f"ð è¨å®ï¼`{order_id}`\n"
                f"çæï¼{p['status']}\n"
                f"ç¶å `{price:.4f}` {pnl_emoji}{pnl:+.2f}%\n"
                f"é²å ´ `{p['entry']:.4f}` Â· æ­¢æ `{p['sl']:.4f}`\n"
                f"TP1 `{p['tp1']:.4f}` Â· TP2 `{p['tp2']:.4f}` Â· TP3 `{p['tp3']:.4f}`\n"
                f"é²åº¦ï¼{progress}"
            )
            if i < len(positions) - 1:
                lines.append("â" * 22)
        return "\n".join(lines)


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 11. ä¸»ææ
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def run_monitor(tracker: SignalTracker, in_run_polls: int = 1, poll_interval: int = 30) -> None:
    """ð é«é »ç£æ§æ¨¡å¼ â åªæª¢æ¥æ¢æè¨èç PENDING é²å ´ / TP / SLï¼ä¸çææ°è¨è

    in_run_polls: ä¸æ¬¡ cron å·è¡å§è¼ªè©¢å¹¾æ¬¡ï¼æ­é poll_interval ç§ééï¼
      é è¨­ 1 æ¬¡ = ç´é  cron é »çï¼è¨­æ 3 + interval=20 â ä¸æ¬¡ cron å§ 1 åéå§æ 3 æ¬¡

    ç¨æ³ï¼python main.py monitor
    å»ºè­°æ­é monitor-only.yml workflowï¼æ¯ 3 åé cronï¼
    """
    if not tracker.signals:
        logging.info("ð­ ç¡è¿½è¹¤ä¸­è¨èï¼monitor è·³é")
        return

    n = len(tracker.signals)
    logging.info(f"ð monitor æ¨¡å¼ååï¼è¿½è¹¤ä¸­ {n} ç­è¨è Ã {in_run_polls} è¼ª")

    total_transitions = 0
    for poll_idx in range(in_run_polls):
        if not tracker.signals:
            logging.info("ð­ ææè¨èå·²çµæï¼ææ©æ¶å·¥")
            break
        try:
            tracker.check_all()
            total_transitions += tracker.transitions
            if poll_idx < in_run_polls - 1:
                time.sleep(poll_interval)
        except Exception as e:
            logging.error(f"â monitor poll {poll_idx + 1} åºé¯ï¼{e}")

    logging.info(f"â monitor å®æï¼{in_run_polls} è¼ªå±è§¸ç¼ {total_transitions} æ¬¡çæè®å")


def run_scan(tracker: SignalTracker) -> int:
    """ð å·è¡ææï¼æ´å v12 å¨é¨é¢¨æ§ï¼"""
    logging.info("ð éå§ææ...")

    # ð©º å¥åº·ç£æ§ï¼åæª¢æ¥èªå·±æ¯å¦ç°å¸¸ï¼
    unhealthy, health_msg = check_health()
    if unhealthy:
        send_tg(health_msg)

    # ââ 0. ç±è¼å¥éç½® ââ
    cfg = load_config()
    coins = cfg.get("coins", ALL_COINS)
    max_signals = cfg.get("max_signals", MAX_SIGNALS)
    score_thr = cfg.get("score_threshold", SCORE_THRESHOLD)
    cooldown_h = cfg.get("cooldown_hours", COOLDOWN_HOURS)
    expire_h = cfg.get("signal_expire_hours", SIGNAL_EXPIRE_HOURS)
    atr_max = cfg.get("atr_max_pct", 0.04)
    pv_cfg = cfg.get("price_verification", {})
    pv_enabled = pv_cfg.get("enabled", True)
    pv_max_dev = pv_cfg.get("max_deviation_pct", 0.5)
    pv_block_unverified = pv_cfg.get("block_on_unverified", False)

    state = get_system_state()

    # ââ 1. é£çºè§æçæ· ââ
    paused, msg, losses = check_circuit_breaker(cfg)
    if paused:
        if not state.get("circuit_active"):
            send_tg(msg)
            state["circuit_active"] = True
            state["circuit_since"] = time.time()
            set_system_state(state)
        logging.warning(f"ð çæ·ä¸­ï¼é£æ {losses}ï¼â ä»æçºç£æ§æ¢æè¨è")
        # çæ·æéä¸éæ°å®ï¼ä½è¦ç¹¼çºè¿½æ¢æå®
        tracker.check_all()
        tracker.send_position_updates()
        return 0
    else:
        if state.get("circuit_active"):
            send_tg("â *çæ·å·²è§£é¤*\nç³»çµ±æ¢å¾©æ­£å¸¸ææï¼ç¹¼çºå æ²¹ ð")
            state["circuit_active"] = False
            state["circuit_since"] = None
            set_system_state(state)

    # ââ 2. ééµææ®µéæ¿¾ ââ
    blocked, btime_reason = is_blackout_time(cfg)
    if blocked:
        logging.info(f"ð ç¦æ­¢äº¤æææ®µï¼{btime_reason}ï¼ï¼ä¸éæ°å®ä½ç¹¼çºç£æ§")
        tracker.check_all()
        tracker.send_position_updates()
        return 0

    # ââ 2.5 æ°èäºä»¶ææ®µéæ¿¾ ââ
    in_news, news_reason = is_in_news_window(cfg)
    if in_news:
        logging.info(f"ð° æ°èäºä»¶ææ®µï¼{news_reason}ï¼ï¼ä¸éæ°å®ä½ç¹¼çºç£æ§")
        tracker.check_all()
        tracker.send_position_updates()
        return 0

    # ââ 2.7 é£æå·éæ ââ
    cooling, remaining_sec, cool_msg = check_cooling_off(cfg)
    if cooling:
        logging.info(f"âï¸ {cool_msg}")
        tracker.check_all()
        tracker.send_position_updates()
        return 0

    # ââ 2.8 ð¡ï¸ æ¯æ¥é¢¨æ§ç´ç·ï¼æåæ¸ / ç´¯è¨æå¤± / è¨èæ¸ï¼ââ
    limit_hit, limit_msg = check_daily_limits(cfg, tracker)
    if limit_hit:
        logging.info(f"ð¡ï¸ {limit_msg}")
        tracker.check_all()
        tracker.send_position_updates()
        return 0

    # ââ 2.9 â¡ æ©æéåºï¼ææå¹£ç¨®é½ä¸å¯éå®æè·³éé API å¼å« ââ
    eligible_coins = []
    for instId in coins:
        if tracker.has_open_position(instId):
            continue
        if is_cooling(instId, cooldown_h):
            continue
        cn = instId.split("-")[0]
        if is_coin_underperforming(cn, cfg)[0]:
            continue
        if is_coin_overheating(cn, cfg)[0]:
            continue
        eligible_coins.append(instId)

    if not eligible_coins:
        logging.info(f"ð­ ææ {len(coins)} å¹£ç¨®é½ä¸å¯éå®ï¼å·å» / æå / æ«åï¼ï¼åè·ç£æ§")
        tracker.check_all()
        tracker.send_position_updates()
        reset_failure_count()
        return 0

    # ââ 3. ææå¯éå®çå¹£ç¨®ï¼å·²ç¯©é¸éå·å» / æå / æ«å / éç±ï¼ââ
    sent = 0
    logging.info(f"ð¯ å¯éå®å¹£ç¨®ï¼{len(eligible_coins)} å â {[c.split('-')[0] for c in eligible_coins]}")
    for instId in eligible_coins:
        if sent >= max_signals:
            break
        coin_name = instId.split("-")[0]

        try:
            okx_price = fetch_price(instId)
            if okx_price <= 0:
                logging.warning(f"[{instId}] ç¡æ³åå¾ OKX å¹æ ¼")
                continue

            # 3.3 ð¡ TradingView ç¬¬äºä¾æºé©è­
            if pv_enabled:
                ok, tv_price, diff = verify_price(
                    instId, okx_price, pv_max_dev, pv_block_unverified
                )
                if not ok:
                    if tv_price is None:
                        logging.warning(f"[{instId}] TV ç¡æ³é©è­ï¼æ ¹æè¨­å®æä¸")
                    else:
                        send_tg(
                            f"â ï¸ *{instId.split('-')[0]} å¹æ ¼ç°å¸¸*\n"
                            f"OKX `{okx_price:.4f}` vs TV `{tv_price:.4f}`\n"
                            f"åé¢ `{diff:.3f}%` > é¾å¼ `{pv_max_dev}%`\n"
                            f"â¸ æ¬è¼ªè·³éè©²å¹£ç¨®"
                        )
                    continue

            df = fetch_candles(instId)
            if df is None:
                continue

            funding = fetch_funding_rate(instId)
            signal = generate_signal(
                instId,
                df,
                okx_price,
                funding,
                score_threshold=score_thr,
                atr_max_pct=atr_max,
                signal_expire_hours=expire_h,
            )
            if not signal:
                continue

            in_zone = (
                signal["side"] == "LONG"
                and signal["entry"] * (1 - 0.006) <= okx_price <= signal["entry"] * (1 + 0.002)
            ) or (
                signal["side"] == "SHORT"
                and signal["entry"] * (1 - 0.002) <= okx_price <= signal["entry"] * (1 + 0.006)
            )

            key, order_id = tracker.add(signal, active=in_zone)

            if in_zone:
                msg = _fmt_entry(
                    coin=instId.split("-")[0],
                    side=signal["side"],
                    order_id=order_id,
                    price=okx_price,
                    entry=signal["entry"],
                    sl=signal["sl"],
                    tp1=signal["tp1"],
                    tp2=signal["tp2"],
                    tp3=signal["tp3"],
                    score=signal["score"],
                    funding_rate=funding,
                    detail=signal.get("detail"),
                )
                msg_id = send_tg(msg, reply_markup=_order_keyboard(order_id))
                tracker.set_entry_message_id(key, msg_id)
                logging.info(f"â {instId} é²å ´éç¥å·²éåºï¼è¨å® {order_id}")
            else:
                _d = signal.get("detail") or {}
                _lref = signal.get("_limit_ref_price", okx_price)
                _diff_pct = (signal["entry"] - _lref) / _lref * 100
                _wait_label = (
                    f"等待回調 `{abs(_diff_pct):.2f}%`" if signal["side"] == "LONG"
                    else f"等待反彈 `{abs(_diff_pct):.2f}%`"
                )
                _limit_src = (
                    "OB 底部支撐" if _d.get("ob_low") and signal["side"] == "LONG"
                    else "OB 頂部阻力" if _d.get("ob_high") and signal["side"] == "SHORT"
                    else "FVG 填充區" if _d.get("fvg_low") or _d.get("fvg_high")
                    else "固定 0.3% 回調"
                )
                _emoji = "🟢" if signal["side"] == "LONG" else "🔴"
                _dir = "做多" if signal["side"] == "LONG" else "做空"
                send_tg(
                    f"{_emoji} *{instId.split('-')[0]} 限價掛單*\n"
                    f"──────────────\n"
                    f"🔖 單號：`{order_id}`\n"
                    f"⏰ 時間：{tw_ts()}\n"
                    f"方向：{_dir}\n"
                    f"📍 限價進場：`{signal['entry']:.4f}`\n"
                    f"📊 掛單時市價：`{_lref:.4f}`\n"
                    f"📉 {_wait_label}\n"
                    f"📌 掛單依據：{_limit_src}\n"
                    f"評分：*{signal['score']} 分*\n\n"
                    f"⏳ 等價格回到限價區間，自動發進場確認",
                    reply_markup=_order_keyboard(order_id),
                )
                logging.info(f"⏳ {instId} 限價掛單已建立 {signal['entry']:.4f}，單號 {order_id}")

            mark_cooldown(instId, cooldown_h)
            sent += 1
        except Exception as e:
            logging.error(f"[{instId}] ææå¤±æï¼{e}")
            continue

    # ââ 4. æ¢æè¨èæª¢æ¥ + æåæ´æ° ââ
    tracker.check_all()
    tracker.send_position_updates()

    logging.info(f"â ææå®æï¼æ¬è¼ªæ°å¢ {sent} ç­è¨è")
    # ð©º éç½®å¤±æè¨æ¸
    reset_failure_count()
    return sent


# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# 12. ä¸»å¥å£
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
def main() -> None:
    try:
        logging.info("=" * 50)
        logging.info("ð¤ Alpha Oracle Pro v11.0 åå")
        logging.info(f"â° å°ç£æéï¼{tw_ts()}")
        logging.info("=" * 50)

        tracker = SignalTracker(ACTIVE_SIGNALS_FILE)

        # å½ä»¤èç
        if len(sys.argv) > 1:
            cmd = sys.argv[1]
            if cmd in ("/stats", "/æå", "stats"):
                send_tg(tracker.get_position_stats())
                return
            if cmd in ("/learning", "/å­¸ç¿", "/coach", "learning"):
                send_tg(format_learning_report())
                return
            if cmd in ("/daily", "/æ¥å ±", "daily"):
                date = sys.argv[2] if len(sys.argv) > 2 else None
                send_tg(format_daily_report(date))
                return
            if cmd in ("/monthly", "/æå ±", "monthly"):
                ym = sys.argv[2] if len(sys.argv) > 2 else None
                send_tg(format_monthly_report(ym))
                return
            if cmd in ("/direction", "/æ¹å", "direction"):
                send_tg(format_direction_stats())
                return
            if cmd in ("/audit", "/å¯©æ¥", "audit"):
                send_tg(format_audit_report())
                return
            if cmd in ("monitor", "/monitor", "/ç£æ§"):
                # é«é »è¼éç£æ§æ¨¡å¼ï¼åªè¿½æ¢æè¨èï¼
                # å¯é¸ï¼python main.py monitor 3 20 â ä¸æ¬¡ cron å§æ 3 æ¬¡ãæ¯æ¬¡éé 20s
                polls = int(sys.argv[2]) if len(sys.argv) > 2 else 1
                interval = int(sys.argv[3]) if len(sys.argv) > 3 else 30
                run_monitor(tracker, in_run_polls=polls, poll_interval=interval)
                return

        run_scan(tracker)
        logging.info("ð ç¨å¼å·è¡å®æ")

    except Exception as e:
        logging.error(f"ð¥ ç³»çµ±é¯èª¤ï¼{e}")
        # ð©º å¤±æè¨æ¸ +1ï¼è§¸ç¼å¥åº·è­¦å ±ï¼
        try:
            increment_failure_count()
        except Exception:
            pass
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
