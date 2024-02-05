Проект состоит из клиента на JavaScript и бэкенда на Django Rest Framework, обмен информацией через WebSocket.

Реализован базовый мессенжер со следующими функциями:

Отправка и получение сообщений;
Создание, редактирование и удаление групповых чатов и переписка в них (управление чатами по REST API, а переписка так же, как в обычных чатах, но с использованием на сервере идеологии «комнат»);
Редактирование личной информации пользователя (имя и аватар);
Просмотр списка других пользователей с переходом на отправку им сообщений.


Запуск проекта:
1. git clone https://github.com/marianazarov/E6.9.git
2. cd E6.9
3. pip install -r requirements.txt
4. Открываем в PC
5. python -m venv venv
6. venv\scripts\activate
7. pip install django
8. pip install djangorestframework
9. pip install daphne
10. pip install channels
11. pip install django-cors-headers
12. pip install easy-thumbnails
13. cd E6.9
14. python manage.py runserver
