import argparse

import requests

from environs import Env

from utils_for_fetch_images import format_datetime, download_image_url


def get_epic_images_urls(api_key: str):
    nasa_url = f'https://api.nasa.gov/EPIC/api/natural/images'
    images_urls = []
    params = {
        'api_key': api_key,
    }
    responses = requests.get(nasa_url, params=params)
    responses.raise_for_status()
    url_responses = responses.json()
    for response in url_responses:
        epic_date = format_datetime(response['date'])
        epic_1b = response['image']
        nasa_planet_image_url = f'https://api.nasa.gov/EPIC/archive/natural/{epic_date}/png/{epic_1b}.png'
        images_urls.append(nasa_planet_image_url)

    return images_urls

def fetch_images_earth_nasa(api_key: str, folder: str):
    params = {
        'api_key': api_key,
    }
    images_urls = get_epic_images_urls(api_key)
    for url_number, url in enumerate(images_urls):
        filename = f'nasa_epic_{url_number}'
        download_image_url(filename, url,params,path=folder)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', help='Название папки', default='images')
    return parser


if __name__ == '__main__':
    env = Env()
    env.read_env()

    args = create_parser().parse_args()
    api_key = env.str('NASA_API_KEY')
    folder = args.folder
    fetch_images_earth_nasa(api_key, folder)
