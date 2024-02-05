Проект состоит из клиента на JavaScript и бэкенда на Django Rest Framework, обмен информацией через WebSocket.

Реализован базовый мессенжер со следующими функциями:

Отправка и получение сообщений;
Создание, редактирование и удаление групповых чатов и переписка в них (управление чатами по REST API, а переписка так же, как в обычных чатах, но с использованием на сервере идеологии «комнат»);
Редактирование личной информации пользователя (имя и аватар);
Просмотр списка других пользователей с переходом на отправку им сообщений.


Запуск проекта:
git clone https://github.com/marianazarov/E6.9.git
cd E6.9
pip install -r requirements.txt
python -m venv venv
venv\scripts\activate
pip install django
pip install djangorestframework
pip install daphne
pip install channels
pip install django-cors-headers
pip install easy-thumbnails
cd E6.9
python manage.py runserver
