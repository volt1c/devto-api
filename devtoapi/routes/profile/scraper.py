from email import header
from bs4 import BeautifulSoup

from devtoapi.utils.JSO import JSO


def scrap(html: str) -> dict:
    soup = BeautifulSoup(html, features="html.parser")
    profile = JSO()

    header = soup.find('header', class_='profile-header')
    profile_details = header.find('div', class_='profile-header__details')

    profile.name = profile_details.find('h1').text

    profile.img = header.find('img')['src']

    profile.bio = profile_details.find('p').text

    profile.time = profile_details.find('time')['datetime']

    profile.links = []
    for link in profile_details.find_all('a'):
        link_dict = {"name": link.text.split()[0], "link": link['href']}
        profile.links.append(link_dict)

    return profile.__dict__
