from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    sender: str
    message: str


@app.post("/chat")
async def chat(message: Message):
    return {"sender": message.sender, "message": message.message}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8090)
