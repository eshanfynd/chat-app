from fastapi import APIRouter

from chat.views import chat

chat_router_v1 = APIRouter(prefix='/chat')

# chat_router_v1.add_api_route("", methods=['GET'], endpoint=chat)
chat_router_v1.add_api_websocket_route("/{mobile_no}", endpoint=chat)
