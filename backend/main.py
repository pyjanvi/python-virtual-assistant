from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.assistant import get_response


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Virtual Assistant API is running"}


@app.post("/chat")
def chat(request: ChatRequest):
    response = get_response(request.message)

    return {
        "message": request.message,
        "response": response
    }