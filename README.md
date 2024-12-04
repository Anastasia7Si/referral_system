# referral_system
Тестовое задание для Hammer Systems

Реферальная система.

## Автор

- **Анастасия Пушкарная** - [GitHub](https://github.com/Anastasia7Si)

## Технологии
- Python 3.11
- Django 5.1.3
- Django REST framework 3.15.2
- Nginx
- Docker
- Postgres
***

## Документация API
Документация API предоставляет подробное описание и схему запросов и ответов, которые можно использовать для взаимодействия с приложением.
Вот основные конечные точки API и как к ним обратиться:
- .../api/user_create/authorization/
- .../users/
- .../users/:id/


#### ***Адрес документации API***:
* Документация API доступна по адресу http://localhost/redoc либо http://localhost/swagger
* Здесь вы найдете подробные сведения о каждом эндпоинте, поддерживаемых методах и структуре запросов и ответов.
* Сслыка на Postman Collection [YandexDisk](https://disk.yandex.ru/d/BkIYaQOciffDsg)

## Реализовано: 

- Авторизация по номеру телефона.
- Просмотр профиля пользователя (со списком пользователей, использовавших его инвайт-код).
- Генерация инвайт-кода и присвоение инвайт-кода друга. 
- Автодокументация Redoc Swagger
- Запуск проекта в Docker-контейнере.

### Как запустить проект локально:
- Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:Anastasia7Si/referral_system.git
cd referral_system
```
- Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
- Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
- Cоздать .env файл и внести в него свои данные, также в проект необходимо настроить для работы с PostgreSQL например:
```
DJANGO_SECRET_KEY= 'django-insecure-example-seckret-key'
POSTGRES_PASSWORD=db_password
POSTGRES_USER=db_user
DB_ENGINE=django.db.backends.postgresql
DB_NAME=db_name
DB_PORT=db_port
DB_HOST=db_host_name
```
- Создание супер-пользователя:
```
python manage.py createsuperuser
```
- Выполнить миграции:
```
python manage.py makemigrations
python manage.py migrate
```
- Запустить проект (доступ по адресу http://127.0.0.1:8000/api/):
```
python manage.py runserver
```
- К проекту подключен Swagger и Redoc, в котором можно ознакомиться с эндпоинтами и методами, а также с примерами запросов, ответов и кода:
```
http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/redoc/
```

### Как запустить проект в контейнерах (доступ по http://localhost:80/api/)
- Документация достпуна по:
```
http://localhost/swagger/
http://localhost/redoc/
```
- Запустить сборку  проекта:
```
docker-compose up -d
```