# praktikum_new_diplom
[![Django-app workflow](https://github.com/TretyakovAnton/foodgram-project-react/workflows/docker-image.yml/badge.svg)](https://github.com/TretyakovAnton/foodgram-project-react/workflows/docker-image.yml)

Проект "Продуктовый помощник»: сайт, на котором пользователи будут публиковать 
рецепты, добавлять чужие рецепты в избранное и подписываться на публикации 
других авторов. Сервис «Список покупок» позволит пользователям создавать 
список продуктов, которые нужно купить для приготовления выбранных блюд."

## Технологический стек
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=008080)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=56C0C0&color=008080)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=56C0C0&color=008080)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/products/docker-hub)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat&logo=GitHub%20actions&logoColor=56C0C0&color=008080)](https://github.com/features/actions)

Использование Continuous Integration и Continuous Deployment.
При пуше в ветку main автоматически отрабатывают сценарии:
1. Автоматический запуск тестов,
2. Обновление образов на Docker Hub,
3. Автоматический деплой на боевой сервер,
4. Отправка сообщения в телеграмм-бот в случае успеха.

## Запуск проекта:

Сначала нужно клонировать репозиторий и перейти в корневую папку:
```
git clone git@github.com:TretyakovAnton/foodgram-project-react.git
cd foodgram-project-react
```
Затем нужно перейти в папку yamdb_final/infra и создать в ней файл .env с 
переменными окружения, необходимыми для работы приложения.
```
cd infra/
touch .env
sudo nano .env
```

Пример содержимого файла:
```
SECRET_KEY=key
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

## Запуск проекта на сервере:
Установите Docker и Docker-compose:
```
sudo apt install docker.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
Проверьте корректность установки Docker-compose:
```
sudo  docker-compose --version
```

Скопируйте подготовленные файлы docker-compose.yaml и nginx/default.conf из вашего проекта на сервер




## Подготовка репозитория на GitHub

Для использования Continuous Integration и Continuous Deployment необходимо в репозитории на GitHub прописать Secrets - переменные доступа к вашим сервисам.
Переменые прописаны в workflows/docker-image.yml
```
DOCKER_PASSWORD, DOCKER_USERNAME - для загрузки и скачивания образа с DockerHub 
USER, HOST, PASSPHRASE, SSH_KEY - для подключения к удаленному серверу 
TELEGRAM_TO, TELEGRAM_TOKEN - для отправки сообщений в Telegram
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

## После каждого обновления репозитория (`git push`) будет происходить:
1. Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8)
2. Сборка и доставка докер-образов на Docker Hub.
3. Автоматический деплой.
4. Отправка уведомления в Telegram.


Затем нужно внутри контейнера web выполнить миграции, создать 
суперпользователя и собрать статику:
```
sudo docker-compose exec backend python manage.py migrate
sudo docker-compose exec backend python manage.py createsuperuser
sudo docker-compose exec backend python manage.py collectstatic --no-input 
sudo docker-compose exec backend python manage.py loaddata datadump.json
```



## Остановка контейнеров

Для остановки работы приложения можно набрать в терминале команду Ctrl+C 
либо открыть второй терминал и воспользоваться командой
```
docker-compose stop 
```
Также можно запустить контейнеры без их создания заново командой
```
docker-compose start 
```
# Ссылка на проект:
http://51.250.106.203/

## Примеры запросов:
### Пользователи.
1. Get-запрос получить список пользователей на эндпоинт /api/users/
Пример ответа:
```
{
  "count": 123,
  "next": "http://foodgram.example.org/api/users/?page=4",
  "previous": "http://foodgram.example.org/api/users/?page=2",
  "results": [
    {
      "email": "user@example.com",
      "id": 0,
      "username": "string",
      "first_name": "Вася",
      "last_name": "Пупкин",
      "is_subscribed": false
    }
  ]
}
```

2. POST-запрос регистрация пользователя /api/users/
Пример POST-запроса:
```
{
  "email": "vpupkin@yandex.ru",
  "username": "vasya.pupkin",
  "first_name": "Вася",
  "last_name": "Пупкин",
  "password": "Qwerty123"
}
```

Пример ответа:
```
{
  "email": "vpupkin@yandex.ru",
  "id": 0,
  "username": "vasya.pupkin",
  "first_name": "Вася",
  "last_name": "Пупкин"
}
```

3. Get-запрос получить данный профиля пользователя /api/users/{id}/
Пример ответа:
```
{
  "email": "user@example.com",
  "id": 0,
  "username": "string",
  "first_name": "Вася",
  "last_name": "Пупкин",
  "is_subscribed": false
}
```

4. Get-запрос получить данный текущего пользователя /api/users/me/
Пример ответа:
```
{
  "email": "user@example.com",
  "id": 0,
  "username": "string",
  "first_name": "Вася",
  "last_name": "Пупкин",
  "is_subscribed": false
}
```

5. Post-запрос изменения пароля /api/users/set_password/
Пример Post-запроса:
```
{
  "new_password": "string",
  "current_password": "string"
}
```

6. Post-запрос получения пароля /api/auth/token/login/
Пример Post-запроса:
```
{
  "password": "string",
  "email": "string"
}
```
Пример ответа:
```
{
  "auth_token": "string"
}
```
7. Post-запрос удаление токена /api/auth/token/logout/


### Теги.
1. Get-запрос получить список тегов или тега /api/tags/ или /api/tags/{id}/
Пример ответа:
```
[
  {
    "id": 0,
    "name": "Завтрак",
    "color": "#E26C2D",
    "slug": "breakfast"
  }
]
```

### Рецепты.
1. Get-запрос получить список рецептов или рецепта /api/recipes/ или /api/recipes/{id}/
Пример ответа:
```
{
  "ingredients": [
    {
      "id": 1123,
      "amount": 10
    }
  ],
  "tags": [
    1,
    2
  ],
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
  "name": "string",
  "text": "string",
  "cooking_time": 1
}
```

2. Post-запрос создание рецепта /api/recipes/
Пример запроса:
```
{
  "ingredients": [
    {
      "id": 1123,
      "amount": 10
    }
  ],
  "tags": [
    1,
    2
  ],
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
  "name": "string",
  "text": "string",
  "cooking_time": 1
}
```
Пример ответа:
```
{
  "id": 0,
  "tags": [
    {
      "id": 0,
      "name": "Завтрак",
      "color": "#E26C2D",
      "slug": "breakfast"
    }
  ],
  "author": {
    "email": "user@example.com",
    "id": 0,
    "username": "string",
    "first_name": "Вася",
    "last_name": "Пупкин",
    "is_subscribed": false
  },
  "ingredients": [
    {
      "id": 0,
      "name": "Картофель отварной",
      "measurement_unit": "г",
      "amount": 1
    }
  ],
  "is_favorited": true,
  "is_in_shopping_cart": true,
  "name": "string",
  "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
  "text": "string",
  "cooking_time": 1
}
```

3. Patch-запрос изменение рецета /api/recipes/{id}/
Пример запроса:
```
{
  "ingredients": [
    {
      "id": 1123,
      "amount": 10
    }
  ],
  "tags": [
    1,
    2
  ],
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
  "name": "string",
  "text": "string",
  "cooking_time": 1
}
```
Пример ответа:
```
{
  "id": 0,
  "tags": [
    {
      "id": 0,
      "name": "Завтрак",
      "color": "#E26C2D",
      "slug": "breakfast"
    }
  ],
  "author": {
    "email": "user@example.com",
    "id": 0,
    "username": "string",
    "first_name": "Вася",
    "last_name": "Пупкин",
    "is_subscribed": false
  },
  "ingredients": [
    {
      "id": 0,
      "name": "Картофель отварной",
      "measurement_unit": "г",
      "amount": 1
    }
  ],
  "is_favorited": true,
  "is_in_shopping_cart": true,
  "name": "string",
  "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
  "text": "string",
  "cooking_time": 1
}
```

4. Delete-запрос удаление рецепта /api/recipes/{id}/

### Список покупок.
1. Get-запрос скачать список покупок /api/recipes/download_shopping_cart/

2. Post-запрос добавить рецепт в список покупок /api/recipes/{id}/shopping_cart/
Пример ответа:
```
{
  "id": 0,
  "name": "string",
  "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
  "cooking_time": 1
}
```

3. Delete-запрос удаление рецепта из списка покупок /api/recipes/{id}/shopping_cart/

### Избранное.
1. Post-запрос добавить рецепт в избранное /api/recipes/{id}/favorite/
Пример ответа:
```
{
  "id": 0,
  "name": "string",
  "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
  "cooking_time": 1
}
```

3. Delete-запрос удаление рецепта из избранного /api/recipes/{id}/shopping_cart/

### Подписки.
1. Get-запрос скачать список подписок /api/users/subscriptions/
Пример ответа:
```
{
  "count": 123,
  "next": "http://foodgram.example.org/api/users/subscriptions/?page=4",
  "previous": "http://foodgram.example.org/api/users/subscriptions/?page=2",
  "results": [
    {
      "email": "user@example.com",
      "id": 0,
      "username": "string",
      "first_name": "Вася",
      "last_name": "Пупкин",
      "is_subscribed": true,
      "recipes": [
        {
          "id": 0,
          "name": "string",
          "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
          "cooking_time": 1
        }
      ],
      "recipes_count": 0
    }
  ]
}
```
2. Post-запрос подписаться на пользователя /api/users/{id}/subscribe/
Пример ответа:
```
{
  "email": "user@example.com",
  "id": 0,
  "username": "string",
  "first_name": "Вася",
  "last_name": "Пупкин",
  "is_subscribed": true,
  "recipes": [
    {
      "id": 0,
      "name": "string",
      "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
      "cooking_time": 1
    }
  ],
  "recipes_count": 0
}
```

3. Delete-запрос отписаться от пользователя /api/users/{id}/subscribe/

### Ингридиенты.
1. Get-запрос получить список ингридиентов или ингридиента /api/ingredients/ или /api/ingredients/{id}/
Пример ответа:
```
{
  "id": 0,
  "name": "Капуста",
  "measurement_unit": "кг"
}
```
