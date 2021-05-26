import requests
from bs4 import BeautifulSoup
from pprint import pprint


# определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get(f'https://habr.com/ru/all/')
if not response.ok:
    raise ValueError('no response')

text = response.text
soup = BeautifulSoup(text, features='html.parser')


def search_posts():
    """ search_posts -> Ищет свежие посты по ключевым словам в названии, хабах и тексте поста"""
    post_text = []
    result = []
    articles = soup.find_all('article')
    for article in articles:
        post_title = [pt.text for pt in article.find_all('a', class_='post__title_link')]
        hubs = {h.text for h in article.find_all('a', class_='hub-link')}
        post_hrefs = article.find('a', class_='post__title_link').attrs.get('href')
        response_1 = requests.get(post_hrefs)
        if not response_1.ok:
            raise ValueError('no response')
        text_1 = response_1.text
        soup_1 = BeautifulSoup(text_1, features='html.parser')
        get_text = str(soup_1.find('div', id='post-content-body'))
        post_text.append(get_text)
        # post_text = [pt.text for pt in article.find_all('div', class_='post__text')]
        for words in KEYWORDS:
            keywords = words
        for words in post_title:
            post_title_words = words
        for words in post_text:
            post_text_words = words
        if keywords in post_title_words or set(KEYWORDS) & hubs or keywords in post_text_words:
            date = article.find('span', class_='post__time').text
            title = article.find('a', class_='post__title_link').text
            href = article.find('a', class_='post__title_link').attrs.get('href')
            result.append(f'{date}, {title}, {href}')
    return result


pprint(search_posts())





