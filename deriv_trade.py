import json
import websocket

DERIV_APP_ID = 1089
API_TOKEN = "YOUR_TOKEN_HERE"

ws = None

def on_open(ws):
    print("🔐 Connected to Deriv")

    # Step 1: authorize
    ws.send(json.dumps({
        "authorize": API_TOKEN
    }))


def on_message(ws, message):
    data = json.loads(message)
    print("RESPONSE:", data)

    # After authorization, place a demo trade once
    if data.get("msg_type") == "authorize":
        print("✅ Authorized - placing DEMO trade...")

        trade_request = {
            "buy": 1,
            "price": 1,
            "parameters": {
                "amount": 1,
                "basis": "stake",
                "contract_type": "CALL",
                "currency": "USD",
                "duration": 1,
                "duration_unit": "t",
                "symbol": "R_100"
            }
        }

        ws.send(json.dumps(trade_request))


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
