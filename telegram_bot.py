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
    """Создаем список путей к изображениям в указанной папке"""
    folder_path = Path(folder)
    images = [str(image) for image in folder_path.iterdir() if image.is_file()]
    return images


def send_images(bot, chat_id, image_path):
    """Отправляем картинку в телеграмм"""
    with open(image_path, 'rb') as image:
        bot.send_document(chat_id=chat_id, document=image)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time', help='Введите время задержки в секундах', default=3600)
    parser.add_argument('-f', '--folder', help='Путь к папке с изображениями', default='images')
    return parser


def main():
    bot = telegram.Bot(token=env.str('TELEGRAM_TOKEN'))
    chat_id = env.str('TELEGRAM_CHAT_ID')
    args = create_parser().parse_args()
    images = get_images(args.folder)
    time_interval = args.time

    sent_images = set()
    while True:
        try:
            if len(sent_images) == len(images):
                sent_images.clear()

            remaining_images = list(set(images) - sent_images)
            if remaining_images:
                image_to_send = random.choice(remaining_images)
                try:
                    send_images(bot, chat_id, image_to_send)
                    sent_images.add(image_to_send)
                except telegram.error.TelegramError:
                    print('Не удалось загрузить изображение')

            time.sleep(int(time_interval))
        except telegram.error.TelegramError:
            print('Ошибка')
        except telegram.error.NetworkError:
            print('Ошибка подключения')
            time.sleep(10)


if __name__ == '__main__':
    main()
