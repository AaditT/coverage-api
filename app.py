from flask import Flask
app = Flask(__name__)
from GoogleNews import GoogleNews
from datetime import datetime as dt
import datetime
import lavaa
import json

@app.route('/')
def home():
    return """
    <h1> COVerage RESTful API </h1>

    <h2> Welcome!

    <h3><a href="/docs">Read the API documentation</a></h3>
    <iframe src="https://giphy.com/embed/lXiRLb0xFzmreM8k8" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/vector-newspaper-flat-lXiRLb0xFzmreM8k8"></p>

    """


@app.route('/docs')
def docs():
    return """
    <h3><a href="/"> <- Home </a></h3>
    <h1> COVerage RESTful API </h1>

    <h2> Welcome to the docs!

    <h4> API v1 </h4>
    <code> /api/v1/county(region)/state(or country) </code>
      <p>
        Version 1 is optimized for speed. <br>
        Returns JSON object in following format <br>
        <code>
          { <br>
           &nbsp; "county": county, <br>
          &nbsp; "state": state, <br>
          &nbsp; "time": { <br>
           &nbsp; &nbsp; "timestamp": now, <br>
            &nbsp; }, <br>
          &nbsp; "data": { <br>
           &nbsp; &nbsp; "policies": { <br>
          &nbsp; &nbsp; &nbsp; "urls": [url1, url2, url3, etc], <br>
          &nbsp; &nbsp; }, <br>
          &nbsp; &nbsp; "education": { <br>
          &nbsp; &nbsp; &nbsp; "urls": [url1, url2, url3, etc], <br>
          &nbsp; &nbsp; }, <br>
          &nbsp; &nbsp; "biology": { <br>
          &nbsp; &nbsp; &nbsp; "urls": [url1, url2, url3, etc], <br>
          &nbsp; &nbsp; }, <br>
          &nbsp; &nbsp; "economy": { <br>
          &nbsp; &nbsp; &nbsp; "urls": [url1, url2, url3, etc], <br>
          &nbsp; &nbsp; }, <br>
          &nbsp; &nbsp; "statistics": { <br>
          &nbsp; &nbsp; &nbsp; "urls": [url1, url2, url3, etc], <br>
          &nbsp; &nbsp; }, <br>
            &nbsp; }, <br>
            }
        </code>
      </p>

      <h4> API v2 </h4>
      <code> /api/v2/county/state </code>
      <p>
        Version 2 is optimized for querying metrics. <br>
        Returns JSON object in following format <br>
        <code>
          { <br>
          &nbsp; "success": True, <br>
           &nbsp; "county": county, <br>
          &nbsp; "state": state, <br>
          &nbsp; "time": { <br>
           &nbsp; &nbsp; "timestamp": now, <br>
            &nbsp; }, <br>
          &nbsp; "data": { <br>
           &nbsp; &nbsp; "policies": { <br>
          &nbsp; &nbsp; &nbsp; "urls": [url1, url2, url3, etc], <br>
          &nbsp; &nbsp; &nbsp; "scores": { <br>
            &nbsp;  &nbsp; &nbsp; &nbsp; "extractive": [score1, score2, score3, etc], <br>
          &nbsp;  &nbsp; &nbsp; &nbsp; "abstractive": [score1, score2, score3, etc], <br>
          &nbsp; &nbsp; &nbsp; } <br>
          &nbsp; &nbsp; }, <br>
          &nbsp; &nbsp; "education": { <br>
          &nbsp; &nbsp; &nbsp; "urls": [url1, url2, url3, etc], <br>
          &nbsp; &nbsp; &nbsp; "scores": { <br>
            &nbsp;  &nbsp; &nbsp; &nbsp; "extractive": [score1, score2, score3, etc], <br>
          &nbsp;  &nbsp; &nbsp; &nbsp; "abstractive": [score1, score2, score3, etc], <br>
          &nbsp; &nbsp; &nbsp; } <br>
          &nbsp; &nbsp; }, <br>
          &nbsp; &nbsp; "biology": { <br>
          &nbsp; &nbsp; &nbsp; "urls": [url1, url2, url3, etc], <br>
          &nbsp; &nbsp; &nbsp; "scores": { <br>
            &nbsp;  &nbsp; &nbsp; &nbsp; "extractive": [score1, score2, score3, etc], <br>
          &nbsp;  &nbsp; &nbsp; &nbsp; "abstractive": [score1, score2, score3, etc], <br>
          &nbsp; &nbsp; &nbsp; } <br>
          &nbsp; &nbsp; }, <br>
          &nbsp; &nbsp; "economy": { <br>
          &nbsp; &nbsp; &nbsp; "urls": [url1, url2, url3, etc], <br>
          &nbsp; &nbsp; &nbsp; "scores": { <br>
            &nbsp;  &nbsp; &nbsp; &nbsp; "extractive": [score1, score2, score3, etc], <br>
          &nbsp;  &nbsp; &nbsp; &nbsp; "abstractive": [score1, score2, score3, etc], <br>
          &nbsp; &nbsp; &nbsp; } <br>
           &nbsp; &nbsp; &nbsp; "scores": { <br>
            &nbsp;  &nbsp; &nbsp; &nbsp; "extractive": [score1, score2, score3, etc], <br>
          &nbsp;  &nbsp; &nbsp; &nbsp; "abstractive": [score1, score2, score3, etc], <br>
          &nbsp; &nbsp; &nbsp; } <br>
          &nbsp; &nbsp; }, <br>
          &nbsp; &nbsp; "statistics": { <br>
          &nbsp; &nbsp; &nbsp; "urls": [url1, url2, url3, etc], <br>
          &nbsp; &nbsp; &nbsp; "scores": { <br>
            &nbsp;  &nbsp; &nbsp; &nbsp; "extractive": [score1, score2, score3, etc], <br>
          &nbsp;  &nbsp; &nbsp; &nbsp; "abstractive": [score1, score2, score3, etc], <br>
          &nbsp; &nbsp; &nbsp; } <br>
          &nbsp; &nbsp; }, <br>
            &nbsp; }, <br>
            }
        </code>
      </p>

    """
@app.route('/api/v1/<county>/<state>')
def v1(county, state):

    location = (county + ", " + state)

    urls = [[],[],[],[],[],[]]

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
        str(location) + " COVID-19 " + categories[5]
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
            "donations": {
                "urls": urls[5],
            },
        },
    }
    loaded_data = json.dumps(data)
    # print(type(loaded_data))
    # print(loaded_data)
    return loaded_data
    

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

if __name__ == '__main__':
    app.run(debug=True)
