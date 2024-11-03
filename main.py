from fastapi import FastAPI, Request
from llm.jokes import joke

router = FastAPI()
tags = "Chat"

@router.get("/llm/chat/jokes/{user}")
def chat(
    request: Request,
    user:str
):
    response = joke(user=user)
    return response
    