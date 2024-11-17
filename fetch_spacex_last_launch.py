import requests

from utils_for_fetch_images import download_image_url




def fetch_spacex_last_launch(url_spacex: str):
    response = requests.get(url_spacex)
    urls_spacex_jpeg = response.json()["links"]["flickr"]['original']
    for url_number, url in enumerate(urls_spacex_jpeg):
        filename = f'spacex_{url_number}'
        download_image_url(filename, url)


if __name__ == '__main__':
    url_spacex = 'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'
    fetch_spacex_last_launch(url_spacex)