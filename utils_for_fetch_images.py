import os.path
import datetime
from urllib.parse import urlparse

import requests


def download_image_url(filename: str, url: str):
    """Загружаем картинку с url """
    path_to_jpeg = f'images/{filename}{file_extension(url)}'
    response = requests.get(url)
    with open(path_to_jpeg, 'wb') as f:
        f.write(response.content)


def file_extension(url: str):
    """ Определяем формат"""
    parsed_url = urlparse(url)

    return os.path.splitext(parsed_url.path)[1]


def format_datetime(date: str):
    """ Меняем формат даты для запроса на сайт Nasa"""
    date_formated = datetime.datetime.fromisoformat(date)
    formatted_date = date_formated.strftime('%Y/%m/%d')
    return formatted_date
