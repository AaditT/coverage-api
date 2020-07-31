from flask import Flask
app = Flask(__name__)
from GoogleNews import GoogleNews
from datetime import datetime as dt
import datetime
from resp import *
import lavaa

@app.route('/api/v1/<lat>/<lon>')
def index(lat, lon):

    location = get_location_data(lat, lon)

    try:
        urls = [
            [],
            [],
            [],
            [],
            [],
        ]

        scores = [
            [],
            [],
            [],
            [],
            [],
        ]

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
                scores[index].append(lavaa.lavaa_extractive(query, results[i]['link']))


        success_string = "True"

    except:
        success_string = "False"

        return {
            "success": success_string
        }


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
                "scores": scores[0]
            },
            "education": {
                "urls": urls[1],
                "scores": scores[1]
            },
            "biology": {
                "urls": urls[2],
                "scores": scores[2]
            },
            "economy": {
                "urls": urls[3],
                "scores": scores[3]
            },
            "statistics": {
                "urls": urls[4],
                "scores": scores[4]
            },
        },
    }


if __name__ == '__main__':
    app.run(debug=True)
