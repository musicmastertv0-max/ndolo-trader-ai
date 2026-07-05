# Ndolo Trader AI - Basic Bot Engine

import json
import time

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

print("🤖 Ndolo Trader AI started")
print("Mode:", config["mode"])
print("Assets:", config["assets"])

def analyze_market(asset):
    # Placeholder strategy (we will upgrade later)
    print(f"Analyzing {asset}...")

    # fake signal logic
    signal = "BUY" if time.time() % 2 > 1 else "SELL"
    return signal

def execute_trade(asset, signal):
    print(f"Placing {signal} trade on {asset} with amount {config['trade_amount']}")

# Main loop
while True:
    for asset in config["assets"]:
        signal = analyze_market(asset)
        execute_trade(asset, signal)

    time.sleep(10)
