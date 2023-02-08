from flask import Flask, jsonify, request
from flask_cors import CORS
from euronews_scraping import Euronews_Article

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)
to_check_article = [Euronews_Article()]


@app.route('/articleInfos', methods=["GET"])
def show_infos():
    try:
        to_check_article[0].url = request.headers['Text']
        return jsonify(to_check_article[0].retrieve_info())
    except Exception as e:
        print(e)
        return jsonify()


app.run()
