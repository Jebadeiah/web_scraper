import requests
import string

from bs4 import BeautifulSoup


saved_articles = []
og_url = 'https://www.nature.com/nature/articles'


def get_soup(url):
    r = requests.get(url)
    return BeautifulSoup(r.content, 'html.parser')


def get_news(this_url):
    soup = get_soup(this_url)
    articles = soup.find_all('article')
    for article in articles:
        article_type = article.find('span', class_='c-meta__type')
        if 'News' in article_type:
            article_name = article.find('a', {'data-track-label': 'link'}).text
            body_url = get_body_url(article)
            body_soup = get_soup(body_url)
            article_body = body_soup.find('div', class_='article__body').text.strip()
            name = clean_name(article_name)
            saved_articles.append(name)
            with open(f'{name}.txt', 'wb') as the_article:
                the_article.write(article_body.encode())


def clean_name(name):
    name = name.translate(str.maketrans('', '', string.punctuation)).strip().replace(' ', '_')
    return name


def get_body_url(first_article):
    suffix = first_article.find('a').get('href')
    return f'https://www.nature.com{suffix}'


get_news(og_url)
