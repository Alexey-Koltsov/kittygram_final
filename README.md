#Описание проекта «Kittygram final»

Проект Kittygram final предназначен для публикации зарегистрированными пользователями информации о котиках, их фотографии, достижения. 
Добавлять котиков может только зарегистрированный пользователь.
Просматривать информацию о котиках могут только аутентифицированные пользователи.


#Стек использованных технологий

- Python3
- Django Framework
- Django Rest Framework
- Gunicorn
- Nginx
- Docker
- Docker compose
- GitHub Actions
- PostgreSQL


#Как запустить проект

##Клонировать репозиторий и перейти в него в командной строке
```
git clone git@github.com:Alexey-Koltsov/kittygram_final.git
```

##Собрать образы и залить их на Docker Hub.

В терминале в корне проекта Kittygram_final последовательно выполните команды 
из листинга; замените **username** на ваш логин на Docker Hub.

В директории frontend...
```
cd frontend
```
```
docker build -t username/kittygram_frontend .
```
То же в директории backend...
```
cd ../backend
```
```
docker build -t username/kittygram_backend .
```
...то же и в nginx
```
cd ../nginx
```
```
docker build -t username/kittygram_gateway .
```


##Загружаем образы на Docker Hub

Отправьте собранные образы фронтенда, бэкенда и Nginx на Docker Hub:

```
docker push username/kittygram_frontend
```
```
docker push username/kittygram_backend
```
```
docker push username/kittygram_gateway
```


##Устанавливаем Docker Compose на сервер

Поочерёдно выполните на сервере команды для установки Docker и Docker Compose для Linux. 
```
sudo apt update
```
```
sudo apt install curl
```
```
curl -fSL https://get.docker.com -o get-docker.sh
```
```
sudo sh ./get-docker.sh
```
```
sudo apt install docker-compose-plugin
```


##Запускаем Docker Compose на сервере

Создайте на сервере директорию kittygram/.
```
mkdir kittygram
```

Скопируйте файл .env на сервер, в директорию kittygram/.
```
scp -i C:/Dev/vm_access/yc-koltsov2022 .env \
    yc-user@158.160.77.6:/home/yc-user/kittygram/.env
```



##Перенаправляем все запросы в докер

На сервере в редакторе nano откройте конфиг Nginx:
```
sudo nano /etc/nginx/sites-enabled/default
```

Измените настройки location в секции server:
```
    location / {
        proxy_pass http://127.0.0.1:9000;
    }
```

Добавьте секреты в GitHub Actions

Ваш пароль на DockerHub:
```
DOCKER_PASSWORD
```

Ваш username на DockerHub:
```
DOCKER_USERNAME
```

IP-адрес вашего сервера:
```
HOST
```

Ваше имя пользователя на сервере:
```
USER
```

Ваш закрытый SSH-ключ от хоста:
```
SSH_KEY
```

Passphrase для закрытого SSH-ключа:
```
SSH_PASSPHRASE
```

ID своего телеграм-аккаунта:
```
TELEGRAM_TO
```

Токен вашего бота:
```
TELEGRAM_TOKEN
```



#AUTH
Регистрация пользователей и выдача токенов

##Регистрация нового пользователя

Права доступа: Доступно без токена. Поле **username** должно быть уникальным и поле **password** должно
быть уникальным.

POST /users/
```
{
    "username":"string",
    "password": "string"
}
```
Пример ответа:
```
{
    "email": "",
    "username": "string",
    "id": 3
}
```


##Получение JWT-токена

Получение JWT-токена в обмен на username и confirmation code. Права доступа: Доступно без токена.

```
POST /token/login/
```
```
{
  "username": "string",
  "password": "string"
}
```
Пример ответа:
```
{
  "auth_token": "string"
}
```

##Достижения

Получение списка всех достижений

Получить список всех достижений. Права доступа: Аутентифицированные пользователи.
```
GET achievements/
```
Пример ответа:
```
[
    {
        "id": 1,
        "achievement_name": "string"
    },
    {
        "id": 2,
        "achievement_name": "string"
    }
]
```

Получение одного достижения. Права доступа: Аутентифицированные пользователи.

GET achievements/1/
Пример ответа:
```
{
    "id": 1,
    "achievement_name": "string"
}
```


Добавить новое достижение. Права доступа: Аутентифицированные пользователи.
```
POST achievements/
```
Пример запроса:
```
{
    "achievement_name": "string"
}
```
Пример ответа:
```
{
    "id": 2,
    "achievement_name": "string"
}
```

##Добавление котика

Добавить нового котика. Права доступа: Аутентифицированные пользователи.
```
POST cats/
```
Пример запроса:
```
{
    "name": "string",
    "color": "string",
    "birth_year": 2019,
    "achievements": [
        {
            "id": 2,
            "achievement_name": "string"
        }
    ]
}
```
Пример ответа:
```
{
    "id": 2,
    "name": "string",
    "color": "string",
    "birth_year": 2019,
    "achievements": [
        {
            "id": 2,
            "achievement_name": "string"
        }
    ],
    "owner": 1,
    "age": 5,
    "image": "string",
    "image_url": "string"
}
```


##Получение списка котиков

Получение списка котиков. Права доступа: Аутентифицированные пользователи.
```
GET cats/
```

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "string",
            "color": "string",
            "birth_year": 2023,
            "achievements": [
                {
                    "id": 1,
                    "achievement_name": "string"
                }
            ],
            "owner": 1,
            "age": 1,
            "image": "string",
            "image_url": "string"
        },
        {
            "id": 2,
            "name": "string",
            "color": "string",
            "birth_year": 2019,
            "achievements": [
                {
                    "id": 2,
                    "achievement_name": "string"
                }
            ],
            "owner": 1,
            "age": 5,
            "image": "string",
            "image_url": "string"
        }
    ]
}


##Получение информации о котике

Получить информацию о котике по id. Права доступа: Аутентифицированные пользователи.
```
GET cats/{id}/
```
Пример ответа:
```
{
    "id": 2,
    "name": "string",
    "color": "string",
    "birth_year": 2019,
    "achievements": [
        {
            "id": 2,
            "achievement_name": "string"
        }
    ],
    "owner": 1,
    "age": 5,
    "image": "string",
    "image_url": "string"
}
```

##Частично изменить информацию о котике

Частично изменить информацию о котике по id. Права доступа: Аутентифицированные пользователи.

```
PATCH cats/{id}/
```
Пример запроса:
{
    "name": "Котя",
    "birth_year": 2023,
    "achievements": [
        {
            "id": 2,
            "achievement_name": "Самый уставший кот"
        }
    ],
    "owner": 3
}

Пример ответа:

{
    "id": 2,
    "name": "Котя",
    "color": "darkgray",
    "birth_year": 2023,
    "achievements": [
        {
            "id": 2,
            "achievement_name": "Самый уставший кот"
        }
    ],
    "owner": 1,
    "age": 1,
    "image": "http://127.0.0.1:9000/media/cats/images/temp_pHp3Jpl.jpeg",
    "image_url": "/media/cats/images/temp_pHp3Jpl.jpeg"
}


##Удаление информации о котике

Удаление информации о котике по id. Права доступа: Аутентифицированные пользователи.

```
DELETE cats/{id}/
```

#Автор: Кольцов Алексей.
