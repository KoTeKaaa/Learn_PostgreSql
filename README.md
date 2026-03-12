# Learn PostgreSQL

Небольшой учебный CLI-проект на Python для работы со складом товаров через PostgreSQL.

## Что умеет

- добавлять продукт на склад;
- выводить список продуктов;
- обновлять количество товара;
- обновлять цену товара;
- удалять товар по `id`.

## Структура проекта

- `app.py` — точка входа и консольное меню;
- `database.py` — подключение к PostgreSQL и SQL-запросы;
- `logic.py` — слой логики между интерфейсом и базой данных;
- `.env.example` — пример переменных окружения.

## Что нужно для запуска

- Python 3.13+;
- PostgreSQL;
- пакеты:
  - `psycopg2-binary`
  - `python-dotenv`

Установка зависимостей:

```powershell
pip install psycopg2-binary python-dotenv
```

## Настройка окружения

Создай файл `.env` в корне проекта по примеру `.env.example`:

```env
dbname=your_db_name
user=your_db_user
password=your_db_password
host=localhost
port=5432
```

## Запуск

```powershell
python app.py
```

При старте приложение само создаёт таблицу `products`, если её ещё нет.

## Примечание

Проект учебный и подходит для практики:

- SQL-запросов;
- работы с PostgreSQL из Python;
- разделения кода на `Database`, `Logic` и CLI.

В будущем проект можно завернуть в Docker для более простого запуска на другом компьютере.