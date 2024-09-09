from typing import Optional
from fastapi import FastAPI, Query, Body, HTTPException, Depends, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
from scraper_service import retrieve_message, retrieve_comments
from sessions import client_max
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/retrieve_message", status_code=200)
async def status_check(channel: str = Body(), hours: int = Body(), code: Optional[int] = Body(None)):
    return await retrieve_message(client_max, channel, hours, code)

@app.post("/retrieve_comments", status_code=200)
async def status_check(channel: str = Body(), message_id: int = Body(), translate: bool = Body(default=False), code: Optional[int] = Body(None)):
    return await retrieve_comments(client_max, channel, message_id, translate, code)

