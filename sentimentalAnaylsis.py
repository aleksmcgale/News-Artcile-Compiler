import requests
from pprint import pprint
import webScrape
from spacy.lang.en import English
import json
import ast
import re


def document_to_analyze(url):
    nlp = English()
    nlp.add_pipe(nlp.create_pipe('sentencizer'))
    text = webScrape.get_website_text(url)
    text = re.sub(r'https:\\*/\\*/.*?\s', ' ', text)
    strip = nlp(text)
    doc = {'documents': []}
    i = 0
    for sent in strip.sents:
        doc['documents'].append({'id': '' + str(i + 1), 'language': 'en', 'text': str(sent)})
        i += 1
    j = json.dumps(doc)
    j = ast.literal_eval(j)
    return j


def analyze_for_tags(text_path):

    subscription_key = '19a834cea02e402c8f0fe1659cf37884'
    assert subscription_key

    sentiment_base_url = "https://canadacentral.api.cognitive.microsoft.com/text/analytics/v2.0/"

    analyze_url = sentiment_base_url + "sentiment"

    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(analyze_url, headers=headers, json=text_path)
    languages = response.json()
    pprint(languages)
    return languages


def avergae_sentiment(json_sent):
    x = json_sent['documents']
    total_amount = len(x)
    total = 0
    i = 0
    while i < total_amount:
        total += x[i]['score']
        i += 1
    t = total / total_amount
    if t < 0.4:
        return -1
    elif (t >= 0.4) and (t <=0.6):
        return 0
    else:
        return 1


if __name__ == '__main__':
    # function call
    b = document_to_analyze('https://www.bbc.com/news/world-europe-47161500')
    a = analyze_for_tags(b)
    print(a)
    c = avergae_sentiment(a)
    print(c)
