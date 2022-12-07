from flask import Flask, jsonify, request


app = Flask(__name__)
app.config["DEBUG"] = True

lukas_like = [
    100,
    1000,
    0
]

@app.route('/lukas', methods = ["GET"])
def lukas() :
    return jsonify(lukas_like)

app.run()