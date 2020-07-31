from newspaper import fulltext
import requests
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def lavaa_extractive(query, url):
    lavaa = 0
    text = (fulltext(requests.get(url).text)).replace("\n", " ")
    query_words = query.split()
    text_words = [word for word in text.split() if not word in stop_words]
    text_words_len = len(text_words)
    for word in text_words:
        if word in query_words:
            lavaa += 1
    return lavaa/text_words_len
