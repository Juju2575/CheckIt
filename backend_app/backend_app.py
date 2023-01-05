from flask import Flask, jsonify, request
from flask_cors import CORS
from euronews_scraping import euronews_retrieve_info

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)
url = ['']
to_check_article = ['']


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
    # try:
    #    return jsonify(euronews_retrieve_info(to_check_article[0]))
    # print(to_check_article[0])
    return jsonify(euronews_retrieve_info(to_check_article[0]))
    # except:
    #    return jsonify()


@app.route('/sendArticle', methods=["POST"])
def change_article():
    to_check_article[0] = request.data.decode("utf-8")
    j = jsonify(to_check_article[0])
    j.headers.add('Access-Control-Allow-Origin', '*')

    return j
    # return jsonify()


app.run()
