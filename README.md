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
    }`
