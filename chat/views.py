import json

from fastapi import WebSocket

websocket_mapping = {}


async def chat(mobile_no: int, websocket: WebSocket):
    await websockets.accept()
    user_sockets = websocket_mapping.get(mobile_no, [])
    user_sockets.append(websocket)
    websocket_mapping.update({
        mobile_no: user_sockets
    })
    while True:
        data = await websocket.receive_text()
        try:
            print(data)
            # message_details = {"to": 8850255428}
            message_details = json.loads(data)
            receivers = websocket_mapping.get(message_details.get("to"))
            print(receivers)
            if receivers:
                for receiver in receivers:
                    try:
                        text = message_details.get("text")
                        await receiver.send_text(f"{text}")
                    except Exception as receiverError:
                        print(str(receiverError))
                    # await receiver.send_text(f"{text} received from {mobile_no}")
        except Exception as e:
            print(e)
        # await websocket.send_text(f"acknowledge to {mobile_no}")
