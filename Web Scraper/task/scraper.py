import os
import requests
import string

from bs4 import BeautifulSoup


saved_articles = []
og_url = 'https://www.nature.com/nature/articles'
num_pages = int(input())
type_of_articles = input()


def build_directory(page_number):
    page_number = f'Page_{page_number + 1}'
    if page_number not in os.listdir():
        os.mkdir(page_number)
    os.chdir(page_number)


def clean_name(an_article):
    an_article = an_article.find('a', {'data-track-label': 'link'}).text.translate(str.maketrans(
        '', '', string.punctuation)).strip().replace(' ', '_')
    return an_article


def get_url(current_article, is_body=False):
    if is_body:
        suffix = current_article.find('a').get('href')
    else:
        suffix = parse_for_suffix(current_article)
    return f'https://www.nature.com{suffix}'


def get_news(url, this_type):
    soup = get_soup(url)
    articles = soup.find_all('article')
    for article in articles:
        article_type = article.find('span', class_='c-meta__type')
        if this_type in article_type:
            body_url = get_url(article, is_body=True)
            body_soup = get_soup(body_url)
            try:
                article_body = (body_soup.find('div', class_='article-item__body'))
                if not article_body:
                    article_body = (body_soup.find('div', class_='article__body cleared'))
                saved_articles.append(clean_name(article))
                with open(f'{clean_name(article)}.txt', 'wb') as the_article:
                    the_article.write(article_body.text.strip().encode())
            except AttributeError:
                continue


def get_soup(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        return BeautifulSoup(r.content, 'html.parser')


def parse_for_suffix(url):
    soup = get_soup(url)
    page_links = soup.find('ul', class_='c-pagination').find_all('li')
    for page_link in page_links:
        if page_link.find('span').text.lower() == 'next page':
            return page_link.find('a')['href']


def save_news(number_of_pages, types, url):
    the_page = url
    for num in range(0, number_of_pages):
        build_directory(num)
        get_news(the_page, types)
        os.chdir('..')
        the_page = get_url(the_page)


save_news(num_pages, type_of_articles, og_url)
