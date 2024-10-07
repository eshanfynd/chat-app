from fastapi import APIRouter
from chat.router import chat_router_v1
from fastapi.responses import JSONResponse


def ping():
    return JSONResponse(status_code=200, content={"success": True})


app_router = APIRouter()
app_router.add_api_route("/_healthz", methods=['GET'], endpoint=ping())

api_router_v1 = APIRouter(prefix='/v1.0')
api_router_v1.include_router(chat_router_v1)

app_router.include_router(api_router_v1)
