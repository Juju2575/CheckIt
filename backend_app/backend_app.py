from flask import Flask, jsonify, request
from flask_cors import CORS
from euronews_scraping import *
import sys

corres_dict = {'euronews': Euronews_Article,
               'monde-diplomatique': Monde_Article,
               'lemonde': Monde_Article,
               '': Euronews_Article}
app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route("/articleInfos", methods=["GET"])
def show_infos():
    try:
        for k in corres_dict.keys():
            if k in request.headers["Text"]:
                art = corres_dict[k]()
        art.url = request.headers["Text"]
        art.set_website()
        art.retrieve_info()
        art.topic_analysis()
        # art.title = 'Hello'
        # art.topics = "[topic 1, topic 2]"

        print(art.__dict__)
        return jsonify(art.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        return jsonify()


app.run()
