import requests

from environs import Env

from utils_for_fetch_images import format_datetime, download_image_url

env = Env()
env.read_env()

url_nasa = f'https://api.nasa.gov/EPIC/api/natural/images?api_key={env.str("NASA_API_KEY")}'


def fetch_images_earth_nasa(url_nasa: str):
    urls_images = []
    response = requests.get(url_nasa).json()
    for i in response:
        epic_date = format_datetime(i['date'])
        epic_1b = i['image']
        url_nasa_planet_image = f'https://api.nasa.gov/EPIC/archive/natural/{epic_date}/png/{epic_1b}.png?api_key={env.str("NASA_API_KEY")}'
        urls_images.append(url_nasa_planet_image)

    for url_number, url in enumerate(urls_images):
        filename = f'nasa_epic_{url_number}'
        download_image_url(filename, url)


if __name__ == '__main__':
    url_nasa = f'https://api.nasa.gov/EPIC/api/natural/images?api_key={env.str("NASA_API_KEY")}'
    fetch_images_earth_nasa(url_nasa)
