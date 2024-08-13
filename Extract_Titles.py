import requests
from bs4 import BeautifulSoup

google_news_url="https://news.google.com/news/rss"

def get_headlines(rss_url):
    response = requests.get(url=rss_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find_all('title')
    title = list(title)
    title = [str(i)[7:-8] for i in title]
    return title

print(get_headlines(google_news_url))