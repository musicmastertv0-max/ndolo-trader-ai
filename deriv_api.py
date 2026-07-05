# Deriv API connection layer (starter)

import websocket
import json

DERIV_APP_ID = 1089  # demo app id (safe test ID)

def on_message(ws, message):
    data = json.loads(message)
    print("Market Data:", data)

def on_open(ws):
    print("Connected to Deriv WebSocket")
    # Subscribe to Volatility 100 tick data
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

if __name__ == "__main__":
    start_deriv_stream()
