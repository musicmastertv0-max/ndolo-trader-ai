# Ndolo Trader AI - Fully Connected Live Bot

import json
import threading
from deriv_api import start_deriv_stream, set_price_callback

latest_price = None

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

print("🤖 LIVE BOT STARTED")
print("Assets:", config["assets"])

def on_price_update(price):
    global latest_price
    latest_price = price

def strategy(price):
    if price is None:
        return None

    # simple movement logic
    if price > 100:
        return "SELL"
    else:
        return "BUY"

def market_thread():
    start_deriv_stream()

# connect callback
set_price_callback(on_price_update)

threading.Thread(target=market_thread, daemon=True).start()

while True:
    signal = strategy(latest_price)

    if signal:
        print("SIGNAL:", signal, "| Price:", latest_price)
