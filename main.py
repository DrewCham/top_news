import requests

from const import NEWS_API_KEY_API_URL,NEWS_FORMAT

from keys import NEWS_API_KEY

def get_news():

    response = requests.news(NEW_API_URL.format(country_code=country_code,api_key=NEWS_API_KEY))

    if response.ok:
        data = response.json()
    else:
        data = None
    return data

def parse_news(news_output=None)

    news_articles = []

    for article in news_output['articles']:
        source_name = artical['source']['name']
        title = article['title']
        discription = article['discription']

        news_text = NEWS_FORMAT.format(title=title,body=discription,source=source_name)

        news_articles.append(news_text)

return news_articles

if __name__ == '__main__'

    new_output = get_news()
    articles = parse_news(news_output)
    print(articles)
