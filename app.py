from flask import Flask
app = Flask(__name__)
from GoogleNews import GoogleNews
from datetime import datetime as dt
import datetime
from resp import *
import lavaa
from api_docs import api_docs

@app.route('/')
def home():
    return docs

@app.route('/docs')
def docs():
    return docs

@app.route('/api/v1/<lat>/<lon>')
def v1(lat, lon):

    location = get_location_data(lat, lon)

    urls = [[],[],[],[],[]]

    now = dt.now()
    today_date = now.strftime("%m/%d/%Y")
    week_ago_date = (now - datetime.timedelta(days = 7)).strftime("%m/%d/%Y")

    googlenews = GoogleNews()
    googlenews.setlang('en')
    googlenews = GoogleNews(start=week_ago_date,end=today_date)

    categories = ["policies", "education", "biology", "economy", "statistics"]
    queries = [
        str(location) + " coronavirus " + categories[0] + " news",
        str(location) + " coronavirus " + categories[1] + " news",
        str(location) + " coronavirus " + categories[2] + " news",
        str(location) + " coronavirus " + categories[3] + " news",
        str(location) + " coronavirus " + categories[4] + " news"
    ]

    for query in queries:
        index = queries.index(query)
        googlenews.search(query)
        results = googlenews.result()
        for i in range(10):
            urls[index].append(results[i]['link'])


    success_string = "True"



    return {
        "lat": lat,
        "lon": lon,
        "success": success_string,
        "time": {
            "timestamp": now,
        },
        "data": {
            "policies": {
                "urls": urls[0],
            },
            "education": {
                "urls": urls[1],
            },
            "biology": {
                "urls": urls[2],
            },
            "economy": {
                "urls": urls[3],
            },
            "statistics": {
                "urls": urls[4],
            },
        },
    }



@app.route('/api/v2/<lat>/<lon>')
def v2(lat, lon):

    location = get_location_data(lat, lon)


    urls = [[],[],[],[],[]]
    extractive_scores = [[],[],[],[],[]]
    abstractive_scores = [[],[],[],[],[]]

    now = dt.now()
    today_date = now.strftime("%m/%d/%Y")
    week_ago_date = (now - datetime.timedelta(days = 7)).strftime("%m/%d/%Y")

    googlenews = GoogleNews()
    googlenews.setlang('en')
    googlenews = GoogleNews(start=week_ago_date,end=today_date)

    categories = ["policies", "education", "biology", "economy", "statistics"]
    queries = [
        str(location) + " coronavirus " + categories[0] + " news",
        str(location) + " coronavirus " + categories[1] + " news",
        str(location) + " coronavirus " + categories[2] + " news",
        str(location) + " coronavirus " + categories[3] + " news",
        str(location) + " coronavirus " + categories[4] + " news"
    ]

    for query in queries:
        index = queries.index(query)
        googlenews.search(query)
        results = googlenews.result()
        for i in range(10):
            urls[index].append(results[i]['link'])
            extractive_scores[index].append(lavaa.lavaa_extractive(query, results[i]['link']))
            abstractive_scores[index].append(lavaa.lavaa_abstractive(query, results[i]['link']))


    success_string = "True"



    return {
        "lat": lat,
        "lon": lon,
        "success": success_string,
        "time": {
            "timestamp": now,
        },
        "data": {
            "policies": {
                "urls": urls[0],
                "scores": {
                    "extractive": extractive_scores[0],
                    "abstractive": abstractive_scores[0]
                }
            },
            "education": {
                "urls": urls[1],
                "scores": {
                    "extractive": extractive_scores[1],
                    "abstractive": abstractive_scores[1]
                }
            },
            "biology": {
                "urls": urls[2],
                "scores": {
                    "extractive": extractive_scores[2],
                    "abstractive": abstractive_scores[2]
                }
            },
            "economy": {
                "urls": urls[3],
                "scores": {
                    "extractive": extractive_scores[3],
                    "abstractive": abstractive_scores[3]
                }
            },
            "statistics": {
                "urls": urls[4],
                "scores": {
                    "extractive": extractive_scores[4],
                    "abstractive": abstractive_scores[4]
                }
            },
        },
    }



if __name__ == '__main__':
    app.run(debug=True)
