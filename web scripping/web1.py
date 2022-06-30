from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup(requests.get("https://www.w3resource.com/python-exercises/web-scraping/index.php").text, 'lxml')
articles=soup.find('div',id_="taboola-below-article-thumbnails-b")
print(articles)