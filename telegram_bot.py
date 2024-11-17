import argparse
import os
import random
import time
from pathlib import Path

import telegram
from environs import Env

env = Env()
env.read_env()



def get_images(folder):
    """Создаем список путей к изображениями в указанной папке"""
    folder_path = Path(folder)
    images = [str(image) for image in folder_path.iterdir() if image.is_file()]
    return images


def send_images(bot, chat_id, image_path):
    """Отправляем картинку в телеграмм"""
    try:
        with open(image_path, 'rb') as image:
            bot.send_document(chat_id=chat_id, document=image)
    except Exception as e:
        print(f"Не удалось отправить изображение {image_path}. Ошибка: {e}")

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time', help='Введите время задержки в секундах')
    return parser

def main():
    bot = telegram.Bot(token=env.str('TELEGRAM_TOKEN'))
    chat_id = env.str('CHAT_TELEGRAM_ID')
    images = get_images('images')
    args = create_parser().parse_args()
    TIME_INTERVAL = args.time

    sent_images = set()
    while True:
        if len(sent_images) == len(images):
            sent_images.clear()

        remaining_images = list(set(images) - sent_images)
        if remaining_images:
            image_to_send = random.choice(remaining_images)
            send_images(bot, chat_id, image_to_send)
            sent_images.add(image_to_send)

        time.sleep(int(TIME_INTERVAL))



if __name__ == '__main__':
    main()
