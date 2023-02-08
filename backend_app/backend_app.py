from flask import Flask, jsonify, request
from flask_cors import CORS
from euronews_scraping import Euronews_Article

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route('/articleInfos', methods=["GET"])
def show_infos():
    try:
        art = Euronews_Article()
        art.url = request.headers['Text']
        art.set_website()
        art.retrieve_info()
        print(art.__dict__)
        return jsonify(art.__dict__)
    except Exception as e:
        print(e)
        return jsonify()


app.run()
