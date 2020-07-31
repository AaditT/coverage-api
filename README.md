# COVerage RESTful API "coverage-api"

## Welcome!

#### API v1

Version 1 is optimized for speed.  
Returns JSON object in following format  
`
{
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
    `

#### API v2

Version 2 is optimized for querying metrics.  
Returns JSON object in following format  
`{  
  "success": True,  
  "lat": lat,  
  "lon": lon,  
  "time": {  
    "timestamp": now,  
  },  
  "data": {  
    "policies": {  
      "urls": [url1, url2, url3, etc],  
      "scores": {  
        "extractive": [score1, score2, score3, etc],  
        "abstractive": [score1, score2, score3, etc],  
      }  
    },  
    "education": {  
      "urls": [url1, url2, url3, etc],  
      "scores": {  
        "extractive": [score1, score2, score3, etc],  
        "abstractive": [score1, score2, score3, etc],  
      }  
    },  
    "biology": {  
      "urls": [url1, url2, url3, etc],  
      "scores": {  
        "extractive": [score1, score2, score3, etc],  
        "abstractive": [score1, score2, score3, etc],  
      }  
    },  
    "economy": {  
      "urls": [url1, url2, url3, etc],  
      "scores": {  
        "extractive": [score1, score2, score3, etc],  
        "abstractive": [score1, score2, score3, etc],  
      }  
      "scores": {  
        "extractive": [score1, score2, score3, etc],  
        "abstractive": [score1, score2, score3, etc],  
      }  
    },  
    "statistics": {  
      "urls": [url1, url2, url3, etc],  
      "scores": {  
        "extractive": [score1, score2, score3, etc],  
        "abstractive": [score1, score2, score3, etc],  
      }  
    },  
  },  
}`
