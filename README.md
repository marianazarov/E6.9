Проект состоит из клиента на JavaScript и бэкенда на Django Rest Framework, обмен информацией через WebSocket.

Реализован базовый мессенжер со следующими функциями:

Отправка и получение сообщений;
Создание, редактирование и удаление групповых чатов и переписка в них (управление чатами по REST API, а переписка так же, как в обычных чатах, но с использованием на сервере идеологии «комнат»);
Редактирование личной информации пользователя (имя и аватар);
Просмотр списка других пользователей с переходом на отправку им сообщений.


Запуск проекта:
1. git clone https://github.com/marianazarov/E6.9.git
2. python -m venv venv
3. venv\scripts\activate
4. pip install -r requirements.txt
5. pip install django
6. pip install djangorestframework
7. pip install daphne
8. pip install channels
9. pip install django-cors-headers
10. pip install easy-thumbnails
11. cd E6.9
12. python manage.py runserver
