# API проекта [Yatube](https://github.com/xodiumx/yatube_project)
![](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
### В данном API реализовано:
- Создание постов с картинкой,
- комментирование постов,
- подписка на авторов постов,
- регистрация пользователей,
- получение токена JWT,
- документация к API - redoc и swagger,
- другие функции.
_______________________________________________________
### Как развернуть проект
- Клонируйте данный репозиторий на свой компьютер
```
git clone https://github.com/xodiumx/api_yatube_drf
```
- Cоздать и активировать виртуальное окружение:
```
py -3.10 -m venv venv
```
- Активировать venv
```
source venv/Scripts/activate или source env/bin/activate для mac
```
- Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
- Выполнить миграции:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
- Запустить проект из директории где находится файл manage.py:
```
python manage.py runserver
```

### В проекте доступны следующие эндпоинты
```
(GET, POST) - запросы
/api/v1/posts/ 
```
```
(GET, POST) - запросы
/api/v1/posts/{post_id}/comments/
```
```
(GET) - запросы
/api/v1/groups/
```
```
(GET, POST) - запросы
/api/v1/follow/
```
```
Все запросы можно посмотреть в документации
http://127.0.0.1:8000/swagger/
```

### Пример запроса и ответа
```
запрос:

POST http://127.0.0.1:8000/api/v1/posts/
Content-Type: application/json

{
  "text": "новый пост",
  "image": "data:image/png;base64,iVBORw0KGgo..."
}

ответ:

{
  "id": 5,
  "author": "maks",
  "text": "Пост с картинкой",
  "group": null,
  "image": "http://127.0.0.1:8000/media/posts/temp.png",
  "pub_date": "2022-12-07T09:03:20.809075Z"
}
```
__________________________________________
## Author - [Alekseev Maksim](https://t.me/maxalxeev)
