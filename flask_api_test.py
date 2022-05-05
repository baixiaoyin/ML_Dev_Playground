from flask import Flask, jsonify, request

app = Flask(__name__)

players = [{"name": "Chris Paul", "age": 36}]

@app.get("/")
def index():
    return 'Hello World!'

@app.get("/players")
def get_players():
    return (jsonify(players))

@app.post("/players")
def create_team():
    player = {"name": request.json['name'], "age": request.json['age'] }
    players.append(player)
    return (jsonify(players))

if __name__ == "__main__":
    # app.run()
    app.run(host='127.0.0.1',port=8000,debug=True)