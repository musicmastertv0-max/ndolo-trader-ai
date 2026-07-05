# Deriv API - Live tick provider (fixed)

import websocket
import json

DERIV_APP_ID = 1089

# This will be set by bot.py
price_callback = None

def set_price_callback(callback):
    global price_callback
    price_callback = callback

def on_message(ws, message):
    data = json.loads(message)

    if "tick" in data:
        price = data["tick"]["quote"]

        print("Live Price:", price)

        if price_callback:
            price_callback(price)

def on_open(ws):
    print("Connected to Deriv WebSocket")

    request = {
        "ticks": "R_100",
        "subscribe": 1
    }

    ws.send(json.dumps(request))

def start_deriv_stream():
    url = f"wss://ws.derivws.com/websockets/v3?app_id={DERIV_APP_ID}"

    ws = websocket.WebSocketApp(
        url,
        on_message=on_message,
        on_open=on_open
    )

    ws.run_forever()
