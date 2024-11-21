import argparse

import requests

from utils_for_fetch_images import download_image_url


def fetch_spacex_last_launch(folder: str):
    spacex_url = 'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'
    response = requests.get(spacex_url)
    response.raise_for_status()
    spacex_jpeg_urls = response.json()["links"]["flickr"]['original']
    for url_number, url in enumerate(spacex_jpeg_urls):
        filename = f'spacex_{url_number}'
        download_image_url(filename, url, path=folder)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', help='Название папки', default='images')
    return parser


if __name__ == '__main__':

    args = create_parser().parse_args()
    folder = args.folder
    fetch_spacex_last_launch(folder)
