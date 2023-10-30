from fastapi import FastAPI, Query, Body, HTTPException, Depends, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
from scraper_service import retrieve_message, retrieve_comments
from sessions import client_max
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/retrieve_message", status_code=200)
async def status_check(channel: str = Body(), hours: int = Body()):
    return await retrieve_message(client_max, channel, hours)

@app.post("/retrieve_comments", status_code=200)
async def status_check(channel: str = Body(), message_id: int = Body()):
    return await retrieve_comments(client_max, channel, message_id)