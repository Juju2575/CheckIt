from flask import Flask, jsonify, request
from flask_cors import CORS
from euronews_scraping import euronews_retrieve_info

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)
url = ['']


@app.route('/receiveUrl', methods=["POST"])
def addOne():
    url_sent = request.json['name']
    url[0] = url_sent
    return jsonify(url[0])


@app.route('/sendData', methods=["GET"])
def show_website():
    if url[0] != '':
        if '.fr' in url[0]:
            return jsonify(url[0].split('.fr')[0])
        return jsonify(url[0])
    else:
        return jsonify(url[0])


@app.route('/articleInfos', methods=["GET"])
def show_infos():
    return jsonify(euronews_retrieve_info('https://fr.euronews.com/2022/12/13/conference-de-soutien-a-lukraine-laide-doit-arriver-en-temps-reel-sur-le-terrain'))

    try:
        return jsonify(euronews_retrieve_info('https://fr.euronews.com/2022/12/13/conference-de-soutien-a-lukraine-laide-doit-arriver-en-temps-reel-sur-le-terrain'))
    except:
        return jsonify()


app.run()
