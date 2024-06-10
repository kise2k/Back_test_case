import requests

from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from api.models import Ad
from api.constants import (
    MIN_CONST_FOR_COUNT_ADS,
    MIN_CONST_FOR_VIEWS,
    CONST_NAME_LINK,
    CONST_NAME_AUTHOR,
    CONST_NAME_TITLE
)


class Command(BaseCommand):
    help = (
        'Парсинг объявлений с сайта и запись их в базу данных, парсер не'
        'может получить доступ к полю author потому что его нет на'
        'главной странице поиска.'
        )

    def handle(self, *args, **kwargs):
        url = CONST_NAME_LINK
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        ads = soup.find_all('div', class_='bull-item bull-item_inline')

        for ad in ads[:MIN_CONST_FOR_COUNT_ADS]:
            title_tag = ad.find('a', class_='bulletinLink bull-item__self-link auto-shy')
            views_tag = ad.find('span', class_='views nano-eye-text')
            address_tag = ad.find('div', class_='bull-item__bull-info-container')

            title = title_tag.get_text(
                strip=True
            ) if title_tag else CONST_NAME_TITLE
            views = int(
                views_tag.get_text(strip=True)
            ) if views_tag else MIN_CONST_FOR_VIEWS
            address_tag = address_tag.get_text(
                strip=True
            ) if address_tag else CONST_NAME_AUTHOR

            Ad.objects.create(
                title=title,
                author=address_tag,
                views=views,
                position=ads.index(ad) + 1
            )

        self.stdout.write(self.style.SUCCESS(
            'Данные успешно спарсены и сохранены в базу данных'
        ))
