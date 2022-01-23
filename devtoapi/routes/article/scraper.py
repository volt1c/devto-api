from bs4 import BeautifulSoup

from devtoapi.utils.JSO import JSO


def scrap(html: str) -> dict:
    soup = BeautifulSoup(html, features="html.parser")
    article = JSO()

    article_header = soup.find('header', id='main-title')
    article_body = soup.find('div', id='article-body')

    article.title = article_header.find('h1').text.replace('\n', '').strip()

    tags = article_header.find('div', class_='spec__tags').findChildren('a')
    article.tags = []
    for tag in tags:
        tag.find('span').extract()
        article.tags.append(tag.get_text())

    header_author = article_header.find('a', class_='crayons-link')
    author = JSO()
    author.name = header_author.text
    author.username = header_author['href'][1:]
    article.author = author.__dict__

    article.publish_date = article_header.find('time')['datetime']

    article.content = article_body.text

    return article.__dict__
