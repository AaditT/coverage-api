from newspaper import fulltext
import requests
from nltk.corpus import wordnet   #Import wordnet from the NLTK


def lavaa_extractive(query, url):
    lavaa = 0
    text = (fulltext(requests.get(url).text)).replace("\n", " ")
    query_words = query.split()
    text_words = text.split()
    text_words_len = len(text_words)
    for word in text_words:
        if word in query_words:
            lavaa += 1
    return lavaa/text_words_len

def lavaa_abstractive(query, url):
    syn = list()
    ant = list()
    query_words = query.split()
    for word in query_words:
        for synset in wordnet.synsets(word):
           for lemma in synset.lemmas():
              syn.append(lemma.name())    #add the synonyms
              if lemma.antonyms():    #When antonyms are available, add them into the list
                ant.append(lemma.antonyms()[0].name())
    lavaa = 0
    text = (fulltext(requests.get(url).text)).replace("\n", " ")
    text_words = text.split()
    text_words_len = len(text_words)
    for word in text_words:
        if word in query_words or word in syn:
            lavaa += 1
    return lavaa/text_words_len

url = "https://www.cnn.com/2020/07/30/us/schools-reopening-district-plans/index.html"
query = "schools reopening plan"
print(lavaa_extractive(query, url))
print(lavaa_abstractive(query, url))
