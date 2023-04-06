from flask import Flask, jsonify, request
from flask_cors import CORS
from euronews_scraping import *
from twitter_scraping import Tweet
import sys

corres_dict = {'euronews': Euronews_Article,
               'monde-diplomatique': Monde_Article,
               'lemonde': Monde_Article,
               'twitter': Tweet}
app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route("/articleInfos", methods=["GET"])
def show_infos():
    try:
        found = False
        for k in corres_dict.keys():
            if k in request.headers["Text"]:
                art = corres_dict[k]()
                found = True
        if not found:
            art = Euronews_Article()
        art.url = request.headers["Text"]
        art.retrieve_info()
        art.topic_analysis()

        print(art.__dict__)
        return jsonify(art.__dict__)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        return jsonify()


app.run()
