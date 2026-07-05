# Ndolo Trader AI - Live Signal Bot (upgraded)

import json
import threading
from deriv_api import start_deriv_stream

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

print("🤖 Ndolo Trader AI LIVE starting...")
print("Assets:", config["assets"])

latest_price = None

# This will receive live data from deriv_api.py (we will improve next step)
def run_market_stream():
    start_deriv_stream()

# Strategy engine (simple placeholder)
def strategy(price):
    if price is None:
        return None

    if price % 2 == 0:
        return "BUY"
    else:
        return "SELL"

# Start market data thread
threading.Thread(target=run_market_stream, daemon=True).start()

# Main loop
while True:
    signal = strategy(latest_price)
    if signal:
        print("Signal:", signal)
