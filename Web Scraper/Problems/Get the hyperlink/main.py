import requests

from bs4 import BeautifulSoup

chapter = int(input()) - 1
r = requests.get(input())
soup = BeautifulSoup(r.content, 'html.parser')
hyperlinky = soup.find_all('a')
print(hyperlinky[chapter].get('href'))
