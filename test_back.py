from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

lukas_like = [
    0, 100, 1000
]

@app.route('/lukas', methods = ["GET"])
def lukas() :
    return jsonify(lukas_like)

app.run()