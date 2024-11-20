import os.path
import datetime
from urllib.parse import urlparse

import requests


def download_image_url(filename: str, url: str, params:dict = None):
    """Загружаем картинку с url, принимает параметры если необходимо """
    image_folder = os.path.join('images')
    os.makedirs(image_folder, exist_ok=True)
    path_to_jpeg = os.path.join(image_folder, f'{filename}{expand_file(url)}')
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    with open(path_to_jpeg, 'wb') as f:
        f.write(response.content)


def expand_file(url: str):
    """ Определяем формат"""
    parsed_url = urlparse(url)

    return os.path.splitext(parsed_url.path)[1]


def format_datetime(date: str):
    """ Меняем формат даты для запроса на сайт Nasa"""
    formate_date = datetime.datetime.fromisoformat(date)
    formated_date = formate_date.strftime('%Y/%m/%d')
    return formated_date
