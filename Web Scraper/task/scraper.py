import os
import requests
import string

from bs4 import BeautifulSoup


saved_articles = []
og_url = 'https://www.nature.com/nature/articles'
num_pages = int(input())
type_of_articles = input()


def clean_name(an_article):
    an_article = an_article.find('a', {'data-track-label': 'link'}).text.translate(str.maketrans(
        '', '', string.punctuation)).strip().replace(' ', '_')
    return an_article


def get_url(current_article, is_body=False):
    if is_body:
        suffix = current_article.find('a').get('href')
    else:
        suffix = current_article.find('li', class_="c-pagination__item").get('href')
    return f'https://www.nature.com{suffix}'


def get_news(this_url, this_type):
    soup = get_soup(this_url)
    articles = soup.find_all('article')
    for article in articles:
        article_type = article.find('span', class_='c-meta__type')
        if this_type in article_type:
            body_url = get_url(article, True)
            body_soup = get_soup(body_url)
            article_body = body_soup.find('div', class_='article__body').text.strip()
            saved_articles.append(clean_name(article))
            with open(f'{clean_name(article)}.txt', 'wb') as the_article:
                the_article.write(article_body.encode())
                print(os.getcwd())


def get_soup(url):
    r = requests.get(url)
    return BeautifulSoup(r.content, 'html.parser')


def save_news(number_of_pages, types, url):
    the_page = url
    for num in range(1, number_of_pages):
        get_news(the_page, types)
        the_page = get_url(the_page)


save_news(num_pages, type_of_articles, og_url)
