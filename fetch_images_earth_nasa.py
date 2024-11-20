import requests

from environs import Env

from utils_for_fetch_images import format_datetime, download_image_url

env = Env()
env.read_env()


def fetch_images_earth_nasa(url_nasa: str, api_key: str):
    images_urls = []
    params = {
        'api_key': api_key,
    }
    responses = requests.get(url_nasa, params=params).json()
    responses.raise_for_status()
    for response in responses:
        epic_date = format_datetime(response['date'])
        epic_1b = response['image']
        nasa_planet_image_url = f'https://api.nasa.gov/EPIC/archive/natural/{epic_date}/png/{epic_1b}.png'
        images_urls.append(nasa_planet_image_url)

    for url_number, url in enumerate(images_urls):
        filename = f'nasa_epic_{url_number}'
        download_image_url(filename, url, params)


if __name__ == '__main__':
    nasa_url = f'https://api.nasa.gov/EPIC/api/natural/images'
    api_key = env.str('NASA_API_KEY')
    fetch_images_earth_nasa(nasa_url, api_key)
