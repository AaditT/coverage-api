from flask import *
from GoogleNews import GoogleNews
from datetime import datetime as dt
import datetime
import lavaa
import json
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/docs')
def docs():
    return render_template("docs.html")


@app.route('/api/v3/<county>/<state>')
def v3(county, state):
    location = (county + ", " + state)

    policy_urls = []
    education_urls = []
    biology_urls = []
    economy_urls = []
    stats_urls = []
    now = dt.now()
    today_date = now.strftime("%m/%d/%Y")
    week_ago_date = (now - datetime.timedelta(days = 7)).strftime("%m/%d/%Y")

    googlenews = GoogleNews()
    googlenews.setlang('en')
    googlenews = GoogleNews(start=week_ago_date,end=today_date)

    categories = ["policies", "education", "biology", "economy", "statistics", "donations"]
    queries = [
        str(location) + " COVID-19 " + categories[0] + " news",
        str(location) + " COVID-19 " + categories[1] + " news",
        str(location) + " COVID-19 " + categories[2] + " news",
        str(location) + " COVID-19 " + categories[3] + " news",
        str(location) + " COVID-19 " + categories[4] + " news",
        str(location) + " COVID-19 " + categories[5] + " news"
    ]

    def querier(query):
        index = queries.index(query)
        googlenews = GoogleNews()
        googlenews.setlang('en')
        googlenews = GoogleNews(start=week_ago_date,end=today_date)
        googlenews.search(query)
        results = googlenews.result()
        if (index == 0):
            for i in range(len(results)):
                policy_urls.append(results[i]['link'])
        elif (index == 1):
            for i in range(len(results)):
                education_urls.append(results[i]['link'])
        elif (index == 2):
            for i in range(len(results)):
                biology_urls.append(results[i]['link'])
        elif (index == 3):
            for i in range(len(results)):
                economy_urls.append(results[i]['link'])
        elif (index == 4):
            for i in range(len(results)):
                stats_urls.append(results[i]['link'])

    # Mulithreading
    t1 = threading.Thread(target=querier, args=(queries[0],))
    t2 = threading.Thread(target=querier, args=(queries[1],))
    t3 = threading.Thread(target=querier, args=(queries[2],))
    t4 = threading.Thread(target=querier, args=(queries[3],))
    t5 = threading.Thread(target=querier, args=(queries[4],))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    success_string = "True"



    data = {
        "county": county,
        "state": state,
        "success": success_string,
        # "time": {
        #     "timestamp": now,
        # },
        "data": {
            "policies": {
                "urls": policy_urls,
            },
            "education": {
                "urls": education_urls,
            },
            "biology": {
                "urls": biology_urls,
            },
            "economy": {
                "urls": economy_urls,
            },
            "statistics": {
                "urls": policy_urls,
            },
            "donations": {
                "urls": stats_urls,
            },
        },
    }
    loaded_data = json.dumps(data)
    # print(type(loaded_data))
    # print(loaded_data)
    return loaded_data


"""
COVerage Formula - not in use, too time consuming
- plan to add multithreading to improve speed

@app.route('/api/v2/<county>/<state>')
def v2(county, state):

    location = (county + ", " + state)


    urls = [[],[],[],[],[]]
    extractive_scores = [[],[],[],[],[]]
    abstractive_scores = [[],[],[],[],[]]

    now = dt.now()
    today_date = now.strftime("%m/%d/%Y")
    week_ago_date = (now - datetime.timedelta(days = 7)).strftime("%m/%d/%Y")

    googlenews = GoogleNews()
    googlenews.setlang('en')
    googlenews = GoogleNews(start=week_ago_date,end=today_date)

    categories = ["policies", "education", "biology", "economy", "statistics", "donations"]
    queries = [
        str(location) + " coronavirus " + categories[0] + " news",
        str(location) + " coronavirus " + categories[1] + " news",
        str(location) + " coronavirus " + categories[2] + " news",
        str(location) + " coronavirus " + categories[3] + " news",
        str(location) + " coronavirus " + categories[4] + " news",
        str(location) + " coronavirus " + categories[5]
    ]

    for query in queries:
        index = queries.index(query)
        googlenews = GoogleNews()
        googlenews.setlang('en')
        googlenews = GoogleNews(start=week_ago_date,end=today_date)
        googlenews.search(query)
        results = googlenews.result()
        for i in range(len(results)):
            urls[index].append(results[i]['link'])
            extractive_scores[index].append(lavaa.lavaa_extractive(query, results[i]['link']))
            abstractive_scores[index].append(lavaa.lavaa_abstractive(query, results[i]['link']))


    success_string = "True"



    return {
        "county": county,
        "state": state,
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
            "donations": {
                "urls": urls[5],
                "scores": {
                    "extractive": extractive_scores[5],
                    "abstractive": abstractive_scores[5]
                }
            }
        },
    }
"""
if __name__ == '__main__':
    app.run(debug=True)
