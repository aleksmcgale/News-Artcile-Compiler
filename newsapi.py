import requests


def newsAPI(client, from_date, to_date = None):
    if to_date is None:

        main_url = ('https://newsapi.org/v2/everything?'
                    'q=' + client +
                    'from=' + from_date +
                    'sortBy=popularity&'
                    'language=en&'
                    'apiKey=50e6ebb46d9e40df97a709aff1499c75')
    else:
        main_url = ('https://newsapi.org/v2/everything?'
                    'q=' + client +
                    'from=' + from_date +
                    'to=' + to_date +
                    'sortBy=popularity&'
                    'language=en&'
                    'apiKey=50e6ebb46d9e40df97a709aff1499c75')

    open_page = requests.get(main_url).json()

    article = open_page["articles"]

    results = []

    for ar in article:
        results.append(ar["title"])

    return open_page


def analyze_news_json(l1, i):
    r1 = {}
    r1['author'] =(l1['articles'][i]['author'])
    r1['title'] =(l1['articles'][i]['title'])
    r1['description'] = (l1['articles'][i]['description'])
    r1['url'] = (l1['articles'][i]['url'])
    r1['urlToImage']= (l1['articles'][i]['urlToImage'])
    r1['publishedAt'] = (l1['articles'][i]['publishedAt'])
    r1['content'] = (l1['articles'][i]['content'])

    return r1



if __name__ == '__main__':
    # function call
    open_news = newsAPI('Canada&','2019-01-07&')
    print(open_news)
    news = open_news['articles']
    x = len(news)
    print(x)
    i = 0
    while i < x:
        j = analyze_news_json(open_news, i)
        i+=1
    j = analyze_news_json(open_news, 10)




