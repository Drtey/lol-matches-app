import requests, json, os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY') 
euw1 = "https://euw1.api.riotgames.com/lol/"
europe = "https://europe.api.riotgames.com/lol/"