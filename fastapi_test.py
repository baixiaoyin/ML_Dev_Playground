# inside of a Python .py file

import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Player(BaseModel):
    name: str
    age: int

CP3 = Player(name="Chris Paul", age=36)

players = [CP3]

@app.get("/")
def index():
    return 'Hello World!'

@app.get("/players")
def get_players():
    return players

@app.post("/players")
def create_player(player: Player):
    players.append(player)
    return players

if __name__ == "__main__":
    # uvicorn.run("main:app")
    uvicorn.run(app, host="127.0.0.1", port=8000)