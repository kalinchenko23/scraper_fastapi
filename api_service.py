from fastapi import FastAPI, Query, Body, HTTPException, Depends, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
from scraper_service import retreive_message
from sessions import client_max
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/retreive_message", status_code=200)
async def status_check(channel: str , hours: int):
    return await retreive_message(client_max, channel, hours)