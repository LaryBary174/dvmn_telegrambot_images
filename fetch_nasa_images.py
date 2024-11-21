import requests
import argparse
from environs import Env
from utils_for_fetch_images import download_image_url




def get_nasa_images_urls(api_key: str, count: int):
    url_nasa = f'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': api_key,
        'count': count
    }
    nasa_images = []
    responses = requests.get(url_nasa, params=payload)
    responses.raise_for_status()
    url_responses = responses.json()
    for response in url_responses:
        nasa_images.append(response['url'])
    return nasa_images

def fetch_nasa_images(api_key:str,count:int,folder:str,):
    nasa_images = get_nasa_images_urls(api_key,count)
    for url_number, url in enumerate(nasa_images):
        filename = f'nasa_apod_{url_number}'
        download_image_url(filename, url, path=folder)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', help='Введите количество фото для скачивания',default=5)
    parser.add_argument('-f','--folder', help='Название папки', default='images')
    return parser


if __name__ == '__main__':
    env = Env()
    env.read_env()

    args = create_parser().parse_args()
    api_key = env.str('NASA_API_KEY')
    count = args.count
    folder = args.folder
    fetch_nasa_images(api_key, count, folder)
