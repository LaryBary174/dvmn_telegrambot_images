import requests
import argparse
from environs import Env
from utils_for_fetch_images import download_image_url

env = Env()
env.read_env()


def fetch_nasa_images(url_nasa: str, api_key: str, count: int):
    payload = {
        'api_key': api_key,
        'count': count
    }
    nasa_images = []
    responses = requests.get(url_nasa, params=payload).json()
    responses.raise_for_status()
    for response in responses:
        nasa_images.append(response['url'])

    for url_number, url in enumerate(nasa_images):
        filename = f'nasa_apod_{url_number}'
        download_image_url(filename, url)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', help='Введите количество фото для скачивания',default=5)
    return parser


if __name__ == '__main__':
    url_nasa = f'https://api.nasa.gov/planetary/apod'
    args = create_parser().parse_args()
    api_key = env.str('NASA_API_KEY')
    count = args.count
    fetch_nasa_images(url_nasa,api_key, count)
