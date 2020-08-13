![CI](https://github.com/shelter-team/rest-backend/workflows/CI/badge.svg)

FastAPI REST skeleton

## Инструкция для разработки:
1) Склонировать проект себе.
2) Создать .env в корне проекта заполнить аналогично `environments/.env.example`.
3) Подгрузить переменные окружение `pipenv shell` или указать для процесса через плагин.
4) Запустить `postgres` из файла `docker/docker-compose-dev.yml`. `docker-compose -f docker/docker-compose-dev.yaml up`.
5) Запустить приложение `uvicorn src.main:app --reload`.
6) Перед каждым пушем делаем `make lint`.


## Инструкция по Aerich и механизмам миграций:
1) В корне проекта находится `aerich.ini` в этом файле уже описаны нужные настройки для миграций.
2) При додбавлении новой модели в новом модуле вы должны указать её в `settings.database.TORTOISE_ORM.apps` по аналогии
с существующими моделями.
3) Создать миграции пример: `aerich --app users init-db` <- сгенерировать миграции для `TORTOISE_ORM.apps.users`.
4) Если модуль с моделями уже существует и вам нужно внести изменения в существующие модели 
   `aerich --app users migrate`.
5) Провести миграции `aerich --app users upgrade`.
6) При возникновении ошибок попробуйте указать PYTHONPATH=. (корень проекта) для консоли.

#### Параметры приложения:

|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`DEBUG`| Режим отладки |`True`|


#### Параметры подключения к PostgreSQL:

|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`POSTGRES_DB`| Имя БД | `shelter` |
|`POSTGRES_USER`| Пользователь БД | `shelter` |
|`POSTGRES_PASSWORD`| Пароль пользователя БД | `shelter` |
|`POSTGRES_HOST`| Адрес СУБД | `localhost` |
|`POSTGRES_PORT`| Порт СУБД | `5432` |
