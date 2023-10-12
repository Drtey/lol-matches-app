import requests, json, os
from fastapi import FastAPI, APIRouter
from . import settings

router = APIRouter(
    prefix="",
    tags=['riotAPI']
)

@router.get("/{player}")
async def summoner(player: str):
        url = f"{settings.euw1}summoner/v4/summoners/by-name/{player}?api_key={settings.api_key}"
        response = requests.get(url).json()
        summoner = json.loads(json.dumps(response))
        
        return summoner

    
@router.get("/liveMatch/{player}")
async def lMatch(player: str):
        url = f"{settings.euw1}summoner/v4/summoners/by-name/{player}?api_key={settings.api_key}"
        response = requests.get(url).json()
        summoner = json.loads(json.dumps(response))
        
        url =  f"{settings.euw1}spectator/v4/active-games/by-summoner/{summoner['id']}?api_key={settings.api_key}"
        response = requests.get(url).json()
        game = json.loads(json.dumps(response))
        
        return game


@router.get("/match/{gameId}")
async def detailedMatch(gameId: str):
        url = f"{settings.europe}match/v5/matches/{gameId}?api_key={settings.api_key}"
        print(url)
        response = requests.get(url).json()
        game = json.loads(json.dumps(response)) 
        
        return game


@router.get("/matches/{player}")
async def matches(player: str):
        url = f"{settings.euw1}summoner/v4/summoners/by-name/{player}?api_key={settings.api_key}"
        response = requests.get(url).json()
        summoner = json.loads(json.dumps(response))
        
        url = f"{settings.europe}match/v5/matches/by-puuid/{str(summoner['puuid'])}/ids?api_key={settings.api_key}"
        response = requests.get(url).json()
        games = json.loads(json.dumps(response))

        return games
