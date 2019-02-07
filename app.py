from flask import Flask, render_template, request
from werkzeug.utils import secure_filename, redirect
import newsapi
import sys
import webScrape
import sentimentalAnaylsis

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        name = name + '&'
        date = date + '&'
        #replace input either with date or a date one month before use

        open_news = newsapi.newsAPI(name, '2019-01-12&')
        #uncomment below with valid APIKey

        news = open_news['articles']
        x = len(news)
        i = 0
        result = []
        while i < x:
            j = newsapi.analyze_news_json(open_news, i)
            #url = j['url']
            #b = sentimentalAnaylsis.document_to_analyze(url)
            #a = sentimentalAnaylsis.analyze_for_tags(b)
            result.append(j)
            #c = sentimentalAnaylsis.avergae_sentiment(a)
            #if c == 0:
                #result.append(j)
            i += 1

        return render_template('index.html', result = result)



if __name__ == '__main__':
    app.run(debug =True,host='0.0.0.0')

