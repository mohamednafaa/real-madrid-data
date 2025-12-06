import http.client
import os
import json
from dotenv import load_dotenv

load_dotenv('.env')

api_token = os.getenv('API_KEY')

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-apisports-key': api_token
    }

conn.request("GET", "/teams/statistics?season=2019&team=541&league=140", headers=headers)

res = conn.getresponse()
data = res.read()

with open('backend/app/team_stats.json', 'w') as f:
    json.dump(json.loads(data.decode("utf-8")), f, indent=4)