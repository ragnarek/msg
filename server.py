from flask import Flask
from flask import request
from flask import jsonify

import api

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to message api. Post a message to a channel or read from a channel."

@app.route("/<channel>/", methods=['GET', 'POST'])
def channel(channel=None):
    if request.method == 'GET':
        messages = api.get(channel)
        if messages == None:
            return error(404, "Channel: ["+channel+"] not found.")
        return jsonify(messages)
    if request.method == 'POST':
        if not request.is_json:
            return error(406, "Use 'Content-type':'application/json'")
        message = request.get_json()
        api.add(channel, message)
        return ("", 201, {"Content-Type": "application/json"})

def error(code, message):
    respMessage = {"error": code, "message": message}
    resp = (jsonify(**respMessage), code, {"Content-Type": "application/json"})
    return resp

if __name__ == "__main__":
    app.run()