#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Alpha Oracle Pro v14.0 â å°æ¥­äº¤æå¡é¤æçï¼ç¹é«ä¸­æï¼
ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
â¨ v14.0 æ°å¢ï¼è®å°æ¥­ï¼ï¼
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
from concurrent.futures import ThreadPoolExecutor, as_completed


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
# ð¬ð§ è±åæéå·¥å·ï¼èªåè­å¥ BST/GMTï¼å¤ä»¤æ+1hï¼
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
try:
    from zoneinfo import ZoneInfo
    UK_TZ = ZoneInfo("Europe/London")
except ImportError:
    UK_TZ = timezone(timedelta(hours=0))


def uk_now() -> datetime:
    """ç²åè±åæé datetimeï¼èªå BST/GMTï¼"""
    return datetime.now(UK_TZ)


def uk_date_str() -> str:
    """è±åä»æ¥æ¥æå­ä¸² YYYY-MM-DD"""
    return uk_now().strftime("%Y-%m-%d")




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
DAILY_SIGNALS_FILE = "daily_signals_state.json"
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
    "score_threshold": 75,
    "cooldown_hours": 4,
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
) -> int | None:
    """ð¤ ç¼é Telegram éç¥ â åå³ message_idï¼å¤±æå Noneï¼"""
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

    try:
        r = requests.post(
            f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
            json=payload,
            timeout=8,
        )
        if r.status_code == 200:
            return r.json().get("result", {}).get("message_id")
        logging.error(f"â TG API åæç¢¼ {r.status_code}: {r.text[:200]}")
    except Exception as e:
        logging.error(f"â TG ç¼éå¤±æï¼{e}")
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
# 3. éç¥æ ¼å¼
# âââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
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
) -> str:
    """ð é²å ´éç¥"""
    direction = "åå¤" if side == "LONG" else "åç©º"
    emoji = "ð¢" if side == "LONG" else "ð´"
    grade = "ð¥ A+ æ¥µå¼·" if score >= 85 else "â­ A å¼·å" if score >= 70 else "â B+ åæ ¼"

    tp1_pct = (tp1 - entry) / entry * 100 * (1 if side == "LONG" else -1)
    tp2_pct = (tp2 - entry) / entry * 100 * (1 if side == "LONG" else -1)
    tp3_pct = (tp3 - entry) / entry * 100 * (1 if side == "LONG" else -1)
    sl_pct = (sl - entry) / entry * 100  # å¸¶æ­£è² è

    funding_line = ""
    if funding_rate is not None:
        funding_line = f"ð° è³éè²»çï¼`{funding_rate * 100:+.4f}%`\n"

    return (
        f"{emoji} *{coin} é²å ´æé* {grade}\n"
        f"ââââââââââââââ\n"
        f"ð è¨å®ç·¨èï¼`{order_id}`\n"
        f"â° æéï¼{tw_ts()}\n"
        f"æ¹åï¼{direction}\n"
        f"é²å ´å¹ï¼`{entry:.4f}`\n"
        f"ç¶åå¹ï¼`{price:.4f}`\n"
        f"è©åï¼*{score} å*\n"
        f"{funding_line}\n"
        f"ð¯ æ­¢çç®æ¨ï¼\n"
        f"  TP1 `{tp1:.4f}` ({tp1_pct:+.2f}%)\n"
        f"  TP2 `{tp2:.4f}` ({tp2_pct:+.2f}%)\n"
        f"  TP3 `{tp3:.4f}` ({tp3_pct:+.2f}%)\n"
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

    åå³æ¯ç­å«ï¼ts(ms æ´æ¸)ão/h/l/c/öãconfirmed(bool)
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

    åå³ï¼(èª¿æ´å¾ TP åè¡¨, èª¿æ´ç´é)
    """
    sup, res = calc_snr(df, lookback=100)
    out = list(tp_levels)
    notes = []
    if side == "LONG":
        for i, tp in enumerate(out):
            if tp > res * 1.001:
                # TP é«éé»å 0.1% ä»¥ä¸ â æå°é»åå 0.2%
                new_tp = res * 0.998
                if new_tp > entry:
                    notes.append(
                        f"TP{i + 1} ç± {tp:.4f} æ ¡æ­£å° {new_tp:.4f}ï¼é¿éé»å {res:.4f}ï¼"
                    )
                    out[i] = new_tp
    else:
        for i, tp in enumerate(out):
            if tp < sup * 0.999:
                new_tp = sup * 1.002
                if new_tp < entry:
                    notes.append(
                        f"TP{i + 1} ç± {tp:.4f} æ ¡æ­£å° {new_tp:.4f}ï¼é¿éæ¯æ {sup:.4f}ï¼"
                    )
                    out[i] = new_tp
    return out, notes


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
    else:
        detail["ob"] = 0

    # FVG (15)
    fvg = find_fvg(df, side)
    if fvg and fvg["low"] * 0.997 <= current_price <= fvg["high"] * 1.003:
        score += 15
        detail["fvg"] = 15
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

    grade = (
        "A+ æ¥µå¼· ð¥"
        if score >= 85
        else "A å¼·å â­"
        if score >= 70
        else "B+ åæ ¼ â"
        if score >= 68
        else "è§æ âª"
    )
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

        entry = current_price
        sl_dist = atr * 1.5
        sl = entry - sl_dist if side == "LONG" else entry + sl_dist
        risk = abs(entry - sl)

        # â è¦æ ¼åçï¼1.5R / 3.0R / 5.0R
        if side == "LONG":
            tp_levels = [entry + risk * 1.5, entry + risk * 3.0, entry + risk * 5.0]
        else:
            tp_levels = [entry - risk * 1.5, entry - risk * 3.0, entry - risk * 5.0]

        # ð¯ åæ TP æ ¡æ­£ï¼é¿éå¼· S/Rï¼
        tp_levels, tp_notes = adjust_tp_by_sr(entry, side, tp_levels, df)
        if tp_notes:
            detail["tp_adjust_notes"] = tp_notes

        candidates.append(
            {
                "instId": instId,
                "side": side,
                "tf": "15m",
                "entry": round(entry, 6),
                "sl": round(sl, 6),
                "tp1": round(tp_levels[0], 6),
                "tp2": round(tp_levels[1], 6),
                "tp3": round(tp_levels[2], 6),
                "score": score,
                "grade": grade,
                "detail": detail,
                "funding_rate": funding_rate,
                "mtf_snapshot": mtf,
                "regime_snapshot": regime_info,
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

def get_daily_signal_count() -> int:
    """åå¾ä»æ¥ï¼è±åæéï¼å·²ç¼éçé«è³ªéè¨èæ¸"""
    state = _load_json(DAILY_SIGNALS_FILE, {})
    today = uk_date_str()
    if state.get("date_uk") != today:
        _save_json(DAILY_SIGNALS_FILE, {"date_uk": today, "count": 0})
        return 0
    return int(state.get("count", 0))


def increment_daily_signal_count() -> int:
    """éå¢ä»æ¥è¨èè¨æ¸ï¼è±åæéï¼ï¼åå³æ°è¨æ¸"""
    state = _load_json(DAILY_SIGNALS_FILE, {})
    today = uk_date_str()
    if state.get("date_uk") != today:
        state = {"date_uk": today, "count": 0}
    state["count"] = int(state.get("count", 0)) + 1
    _save_json(DAILY_SIGNALS_FILE, state)
    return state["count"]



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
        "max_win": biggest_win,
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
    "" è¨éæ­¢æä¸»å å° learning_stateï¼ä¾å¾çºæ¥è©¢ï¼"""
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
        """ð SL/BE/LOCK å¾éè¦ç¤åæè¨æ¯ï¼ä¸¦å¯«å¥ loss_reasonsï¼"""
        try:
            cfg = load_config()
            pm_cfg = cfg.get("post_mortem", {})
            if not pm_cfg.get("enabled", True):
                return
            if mode != "LOSS" and pm_cfg.get("loss_only", False):
                return

            activated_at = sig.get("activated_at") or sig.get("created") or 0
            all_candles = fetch_candles_full(sig["instId"], limit=100)
            df_at_loss = [
                {"ts": c["ts"], "o": c["o"], "h": c["h"], "l": c["l"], "c": c["c"], "v": c["v"]}
                for c in all_candles
                if (c["ts"] / 1000) >= (activated_at - 900)  # é²å ´å 15 åä½çºåºæº
            ]
            if len(df_at_loss) < 10:
                return

            reasons = analyze_loss(sig, df_at_loss)
            lessons = _generate_lessons(reasons)

            coin = sig["instId"].split("-")[0]
            similar = get_similar_stats(
                sig.get("score", 0),
                sig["side"],
                sig.get("detail", {}),
                sig.get("funding_rate"),
                coin,
            )

            msg = _fmt_postmortem(sig, mode, reasons, lessons, similar)
            send_tg(
                msg,
                reply_to_message_id=sig.get("entry_message_id"),
            )

            if mode == "LOSS":
                record_loss_reason(coin, sig["side"], reasons)
        except Exception as e:
            logging.error(f"â è¦ç¤åæå¤±æï¼{e}")

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
        """ð ç¼éæææåçé²åº¦æ´æ°ï¼æ¯è¼ªä¸æ¬¡ï¼"""
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
            logging.info(f"ð å·²ç¼é {cnt} ç­æåæ´æ°")

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

    logging.info(f"â monitor å®æï¼{in_run_polls} è¼ªe±è§¸ç¼ {total_transitions} æ¬¡çæè¢¥å")


def run_scan(tracker: SignalTracker) -> int:
    """ð å·è¡ææï¼æ´å v12 å¨é¨é¢¨æ§ï¼ä¸¦ç¼ææçï¼"""
    logging.info("ð éå§ææ...")

    # ââ 0. ç±è¼å¥éç½® ââ
    cfg = load_config()
    coins = cfg.get("coins", ALL_COINS)
    max_signals = cfg.get("max_signals", MAX_SIGNALS)
    daily_max = cfg.get("daily_max_signals", 10)
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

    # ââ 3. æ¯æ¥è¨èä¸éæª¢æ¥ ââ
    daily_sent = get_daily_signal_count()
    if daily_sent >= daily_max:
        logging.info(f"ð ä»æ¥ï¼è±åæéï¼å·²éä¸é {daily_max} å®ï¼å·²ç¼ {daily_sent}ï¼ï¼åæ­¢éæ°è¨è")
        tracker.check_all()
        tracker.send_position_updates()
        return 0

    # ââ 4. ç¯©é¸åé¸å¹£ç¨®ï¼æé¤å·å» / å·²æåï¼ââ
    candidates = []
    for instId in coins:
        if tracker.has_open_position(instId):
            logging.info(f"[{instId}] å·²ææªå¹³åè¨èï¼è·³é")
            continue
        if is_cooling(instId, cooldown_h):
            logging.info(f"[{instId}] å·å»ä¸­ï¼è·³é")
            continue
        candidates.append(instId)

    logging.info(f"ð åé¸å¹£ç¨®ï¼{len(candidates)} é»ï¼éå§ä¸¦ç¼ææ...")

    # ââ 5. ä¸¦ç¼ææï¼Phase 1ï¼IO å¯éï¼å¨é¨åææè³æï¼ââ
    def _fetch_and_analyze(instId):
        try:
            okx_price = fetch_price(instId)
            if okx_price <= 0:
                logging.warning(f"[{instId}] ç¡æ³åå¾ OKX å¹æ ¼")
                return instId, None, None, None, None

            # TradingView ç¬¬äºä¾æºé©è­
            if pv_enabled:
                ok, tv_price, diff = verify_price(instId, okx_price, pv_max_dev, pv_block_unverified)
                if not ok:
                    return instId, None, okx_price, None, (tv_price, diff)

            df = fetch_candles(instId)
            if df is None:
                return instId, None, okx_price, None, None

            funding = fetch_funding_rate(instId)
            signal = generate_signal(
                instId, df, okx_price, funding,
                score_threshold=score_thr,
                atr_max_pct=atr_max,
                signal_expire_hours=expire_h,
            )
            return instId, signal, okx_price, funding, None
        except Exception as e:
            logging.error(f"[{instId}] ææå¤±æï¼{e}")
            return instId, None, None, None, None

    results_map: dict = {}
    if candidates:
        max_workers = min(len(candidates), 10)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(_fetch_and_analyze, c): c for c in candidates}
            for future in as_completed(futures):
                result = future.result()
                results_map[result[0]] = result

    # ä¿æåå§å¹£ç¨®é åºï¼ç¢ºä¿è¨èé¸æä¸è´ï¼
    scan_results = [results_map[c] for c in candidates if c in results_map]

    # ââ 6. ä¾åºèçææçµæï¼Phase 2ï¼ç¶­æå®å·è¡ç·èçè¨èï¼ââ
    sent = 0
    for instId, signal, okx_price, funding, pv_error in scan_results:
        if sent >= max_signals:
            break
        if daily_sent + sent >= daily_max:
            logging.info(f"ð ä»æ¥ä¸é {daily_max} å®å·²éï¼åæ­¢")
            break

        # èçå¹æ ¼ç°å¸¸
        if pv_error is not None:
            tv_price, diff = pv_error
            if tv_price is not None:
                send_tg(
                    f"â ï¸ *{instId.split('-')[0]} å¹æ ¼ç°å¸¸*\n"
                    f"OKX `{okx_price:.4f}` vs TV `{tv_price:.4f}`\n"
                    f"åé¢ `{diff:.3f}%` > é¾å¼ `{pv_max_dev}%`\n"
                    f"â¸ æ¬è¼ªè·³éè©²å¹£ç¨®"
                )
            continue

        if signal is None:
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
            )
            msg_id = send_tg(msg, reply_markup=_order_keyboard(order_id))
            tracker.set_entry_message_id(key, msg_id)
            logging.info(f"â {instId} é²å ´éç¥å·²éåºï¼è¨å® {order_id}")
        else:
            send_tg(
                f"ð *{instId.split('-')[0]} è¨èå°±ä½*\n"
                f"ð è¨å®ï¼`{order_id}`\n"
                f"â° æéï¼{tw_ts()}\n"
                f"æ¹åï¼{'åå¤' if signal['side'] == 'LONG' else 'åç©º'}\n"
                f"é²å ´å¹ï¼`{signal['entry']:.4f}`ï¼ç¶å `{okx_price:.4f}`ï¼\n"
                f"è©åï¼{signal['score']} å\n\n"
                f"ð¡ é²å¥ææåéå¾æèªåè§¸ç¼é²å ´éç¥",
                reply_markup=_order_keyboard(order_id),
            )
            logging.info(f"ð {instId} PENDING è¨èå·²å»ºç«ï¼è¨å® {order_id}")

        mark_cooldown(instId, cooldown_h)
        new_daily = increment_daily_signal_count()
        logging.info(f"ð ä»æ¥ï¼è±åæéï¼ç¬¬ {new_daily} å®ï¼ä¸é {daily_max}")
        sent += 1

    # ââ 7. æ¢æè¨èæª¢æ¥ + æåæ´æ° ââ
    tracker.check_all()
    tracker.send_position_updates()

    logging.info(f"â ææå®æï¼æ¬è¼ªæ°å¢ {sent} ç­è¨è")
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
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
