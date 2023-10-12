import requests, json, os
from fastapi import FastAPI
from .routers import riotAPI

app = FastAPI()

@app.get("/")
async def root():
        return {"message:" "Welcome!"}

app.include_router(riotAPI.router)