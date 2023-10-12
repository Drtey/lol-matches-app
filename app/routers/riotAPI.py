import requests, json, os
from fastapi import FastAPI, APIRouter
from ..settings import api_key

euw1 = "https://euw1.api.riotgames.com/lol/"
europe = "https://europe.api.riotgames.com/lol/"

router = APIRouter(
    prefix="",
    tags=['riotAPI']
)

@router.get("/{player}")
async def summoner(player: str):
        url = f"{euw1}summoner/v4/summoners/by-name/{player}?api_key={api_key}"
        response = requests.get(url).json()
        summoner = json.loads(json.dumps(response))
        
        return summoner

    
@router.get("/liveMatch/{player}")
async def lMatch(player: str):
        url = f"{euw1}summoner/v4/summoners/by-name/{player}?api_key={api_key}"
        response = requests.get(url).json()
        summoner = json.loads(json.dumps(response))
        
        url =  f"{euw1}spectator/v4/active-games/by-summoner/{summoner['id']}?api_key={api_key}"
        response = requests.get(url).json()
        game = json.loads(json.dumps(response))
        
        return game


@router.get("/match/{gameId}")
async def detailedMatch(gameId: str):
        url = f"{europe}match/v5/matches/{gameId}'?api_key={api_key}"
        response = requests.get(url).json()
        game = json.loads(json.dumps(response))
        
        return game


@router.get("/matches/{player}")
async def matches(player: str):
        url = f"{euw1}summoner/v4/summoners/by-name/{player}?api_key={api_key}"
        response = requests.get(url).json()
        summoner = json.loads(json.dumps(response))
        
        url = f"{europe}match/v5/matches/by-puuid/{str(summoner['puuid'])}/ids?api_key={api_key}"
        response = requests.get(url).json()
        games = json.loads(json.dumps(response))
        
        return games