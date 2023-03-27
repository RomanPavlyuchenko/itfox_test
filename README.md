README
=====================

Этот README содержит шаги, необходимые запуска веб-приложения, и описание проекта.


---------------------

##  Команды для запуска проекта

```
$ git clone https://github.com/RomanPavlyuchenko/itfox_test.git
$ cd itfox_test
$ mv .env.pub .env
$ docker-compose up
```

---------------------

## Описание
Проект запущен на сервере и доступен по адресу <http://romanpavliuchenko.ru>  
Список эндпоинтов: [Postman Collection](https://elements.getpostman.com/redirect?entityId=10861528-9bf9e586-3ea7-4abb-bbb6-9b426ff3582b&entityType=collection)
 
 [Ссылка на админку](http://romanpavliuchenko.ru/admin)   
- Логин: admin@example.com
- Пароль: admin

---------------------
## Эндпоинты
[Postman Collection](https://elements.getpostman.com/redirect?entityId=10861528-9ad47959-66ff-46d0-9f4d-52d77ffa1691&entityType=collection)
- POST [auth](http://romanpavliuchenko.ru/api/auth/api-token-auth/) (передаем имя пользователя и пароль, получаем токен если пользователь с таким паролем есть и ошибку, если такого пользователя нет)
- GET [news](http://romanpavliuchenko.ru/api/news/news/) (получаем список новостей с пагинацией)
- POST [news](http://romanpavliuchenko.ru/api/news/news/) (создаем новость, проверка на авторизацию)
- PUT [news](http://romanpavliuchenko.ru/api/news/news/) (обновляем новость, проерка на атворизацию, проверка на наличие прав)
- DELETE [news](http://romanpavliuchenko.ru/apinews/news/1/)
- GET [comments](http://romanpavliuchenko.ru/api/news/news/1/comments/) (получение списка комментариев новости с пагинацией)
- POST [comments](http://romanpavliuchenko.ru/api/comments/comments/) (создание нового комментария, проверка на авторизацию)
- DELETE [comments](http://romanpavliuchenko.ru/api/comments/comments/1/) 

---------------------

## Что сделано из ТЗ
### Обязательные задачи
- У каждого пользователя может быть две роли – пользователь и админ; админ может зайти в админ-панель, пользователь – нет;
- создан кастомный класс для авторизации, наследуемый от BaseAuthentication - IsAdminOrAuthor, который, при удалении или изменении новостей или коментариев, проверяет, является ли request.user создателем изменяемого обекта или админом;
- каждый пользователь может создать новость. Все пользователи могут получать списки всех новостей с пагинацией. Пользователи могут удалять и изменять свои новости. Админ может удалять и изменять любую новость;
- добавлен механизм лайков и комментариев новостей – лайкать и комментировать может любой пользователь, автор может удалять комментарии к своим новостям, админ может удалять любые комментарии;
- при получении списка новостей и одной конкретной новости показывается количество лайков и комментариев;
- добавлен список последних 10 комментариев при получении списка новостей и одной новости;
- настроена админка Django, в которой добавлена возможность добавлять модераторов, у которых есть права на изменение новостей и комментариев через админку;
- аутентификация настроена с помощю simple_jwt.

## Задачи из "желательно"
- контейнеризация с помощью docker-compose;
- виртуальное окружение создано посредством poetry;
- использован wsgi сервер Gunicorn;
- "демонстрация понимание механизма миграций моделей" (62d5c81b commit);
- использование .env файла для хранения информации о подключении к базе данных, секретного ключа;
- файл README.md с описанием скриптов для разворачивания окружения и запуска сервера, в котором это все и написано.