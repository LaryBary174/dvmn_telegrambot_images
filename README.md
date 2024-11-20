# Скачивание фотографий космоса и отправка в телеграмм #

Программа позволяет скачивать фотографии космоса с сайтов SpaceX и NASA, и публиковать их в телеграм канале с помощью
бота

## Установка ##

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки
зависимостей:

```
pip install -r requirements.txt
```

Интерпретатор 3.8 +

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` в корне проекта и
запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:

- `NASA_API_KEY` — Апи Кей для скачивания фотографий с сайта NASA, получаете по инструкции тут: https://api.nasa.gov/
- `TELEGRAM_TOKEN` — Токен для телеграмм бота получаете при создании телеграмм бота на канале в телеграм @BotFather
- `CHAT_TELEGRAM_ID` — ID телеграмм чата, где планируете постить фото

## Как пользоваться скриптами для скачивания фото ##

В консоли запускаем файл `fetch_images_earth_nasa.py` скрипт скачает фото нашей планеты   
Пример:

```
py .\fetch_images_earth_nasa.py
```

Скрипт из файла `fetch_nasa_images` скачает различные фото с сайта наса, можно указать необходимое`count` количество
фото, без данного параметра скачивает 5 фотографий
Пример:

```
py .\fetch_nasa_images.py -c 10
```

Скрипт из файла `fetch_spacex_last_launch` скачает фото с сайта SpaceX
Пример:

```
py .\fetch_spacex_last_launch.py      
```

## Телеграм БОТ

После того как скачены фотографии, скрипт в файле  `telegram_bot` будет опубликовывать в автономном режиме эти
фотографии
Запуск возможен без дополнительных параметров, но есть возможность устанавливать свой временной интервал публикации изображений
Стандартный интервал 3600 секунд
Пример:

```
py .\telegram_bot.py -t 60       
```

## Цель проекта ##

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [Devman](https://dvmn.org).
