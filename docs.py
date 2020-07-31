docs = """
<h1> COVerage RESTful API </h1>

<h2> Welcome!

<h4> API v1 </h4>
<code> /api/v1/lat/lon </code>
  <p>
    Version 1 is optimized for speed. <br>
    Returns JSON object in following format <br>
    <code>
      { <br>
       &nbsp; "lat": lat, <br>
      &nbsp; "lon": lon, <br>
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
  <code> /api/v2/lat/lon </code>
  <p>
    Version 2 is optimized for querying metrics. <br>
    Returns JSON object in following format <br>
    <code>
      { <br>
      &nbsp; "success": True, <br>
       &nbsp; "lat": lat, <br>
      &nbsp; "lon": lon, <br>
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
