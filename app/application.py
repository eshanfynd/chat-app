# from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.router import app_router
from fastapi.middleware.cors import CORSMiddleware

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     yield


def get_app() -> FastAPI:
    whatsapp = FastAPI(
        debug=True,
        title="whatsapp",
        docs_url=None,
        openapi_url="/openapi.json",
        # default_response_class=ORJSONResponse,
        lifespan=None
    )

    # whatsapp.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=["*"],  # Only allow this origins
    #     allow_credentials=True,
    #     allow_methods=["*"],  # Allows all methods
    #     allow_headers=["*"],  # Allows all headers
    # )

    whatsapp.include_router(app_router)

    @whatsapp.get('/start')
    def start():
        return "inside"

    return whatsapp
