# Deriv Trade Executor (AUTH REQUIRED)

import json
import websocket

DERIV_APP_ID = 1089

# IMPORTANT: paste your API token here later
API_TOKEN = pat_8014c88bba9a38ab12fb250a861b1d505464a75a8f9865c75e6da3e6bd570903

ws = None

def on_open(ws):
    print("🔐 Connected to Deriv Trading Server")

    # authorize request
    auth_request = {
        "authorize": API_TOKEN
    }
    ws.send(json.dumps(auth_request))


def on_message(ws, message):
    data = json.loads(message)
    print("AUTH RESPONSE:", data)


def connect():
    global ws

    url = f"wss://ws.derivws.com/websockets/v3?app_id={DERIV_APP_ID}"

    ws = websocket.WebSocketApp(
        url,
        on_open=on_open,
        on_message=on_message
    )

    ws.run_forever()


if __name__ == "__main__":
    connect()
