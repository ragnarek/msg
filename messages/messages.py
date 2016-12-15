from flask import Flask
from flask import request
from flask import jsonify
from dateutil import parser
import time

import api

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to message api. Post a message to a channel or read from a channel."

@app.route("/<channel>/", methods=['GET', 'POST'])
@app.route("/<channel>/<message_id>", methods=['GET'])
def channel(channel=None, message_id=None):
    if request.method == 'GET':
        fromDate = getDate(request.args["from"]) if "from" in request.args else float("-inf")
        toDate = getDate(request.args["to"]) if "to" in request.args != None else float("inf")
        messages = api.get(channel, fromDate, toDate, message_id)

        if messages == None:
            return send_error(404, "Channel: ["+channel+"] not found.")
        if message_id != None and len(messages) > 0:
            return jsonify(messages[0])
        return jsonify(messages)

    if request.method == 'POST':
        if not request.is_json:
            return send_error(406, "Use 'Content-type':'application/json'")
        if message_id != None:
            return send_error(405, "Method not allowed")
        message = request.get_json()
        stored_message = api.add(channel, message)
        return ("", 201, {"Content-Type": "application/json", "Location": request.host + "/" + channel + "/" + stored_message["id"]})

    return send_error(405, "Method not allowed")

def send_error(code, message):
    respMessage = {"error": code, "message": message}
    resp = (jsonify(**respMessage), code, {"Content-Type": "application/json"})
    return resp

@app.errorhandler(404)
def not_found(error):
    return send_error(404, "Not found")

@app.errorhandler(400)
def bad_request(error):
    return send_error(400, "Bad Request")

@app.errorhandler(500)
def internal_servererror(error):
    return send_error(500, "Internal Server Error")

def getDate(dateVal):
    try:
        return long(dateVal)
    except ValueError:
        return long(round(time.mktime(parser.parse(dateVal).timetuple()) * 1000))

if __name__ == "__main__":
    app.run()