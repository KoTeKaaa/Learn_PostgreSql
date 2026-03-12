import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        dbname = os.getenv("dbname")
        user = os.getenv("user")
        password = os.getenv("password")
        host = os.getenv("host")
        port = os.getenv("port")

        try:
            self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

        except Exception as e:
            print(f"Ошибка при подключении к БД: {e}")
            raise

    # Создание склада
    def create_table(self):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute(""" CREATE TABLE IF NOT EXISTS products (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    category VARCHAR(50),
                    price NUMERIC(10, 2) CHECK (price > 0),
                    quantity INTEGER DEFAULT 0,
                    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );""")

            print("Склад создан!")

        except Exception as e:
            print(f"Ошибка при создании склада: {e}")

    # Добавление продукта на склад
    def add_product(self, name, category, price, quantity):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("INSERT INTO products (name, category, price, quantity) VALUES(%s, %s, %s, %s)",
                             (name, category, price, quantity))

                    print("Продукт добавлен на склад!")

        except Exception as e:
            print(f"Ошибка при добавлении продукта на склад: {e}")
            raise

    # Вывод списка продуктов на складе
    def list_products(self):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("SELECT id, name, category, price, quantity FROM products")

                    rows = cur.fetchall()
                    print("Содержимое склада:")
                    for row in rows:
                        print(f"ID: {row[0]} | Продукт: {row[1]} | Категория: {row[2]} | Цена: {row[3]} | Количество: {row[4]}")

        except Exception as e:
            print(f"Ошибка вывода содержимого склада: {e}")
            raise

    # Обновление количества продукта
    def update_quantity(self, product_id, new_quantity):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("UPDATE products SET quantity = %s WHERE id = %s", (new_quantity, product_id))

                    print(f"Продукт с ID: {product_id} обновлен, новое количество = {new_quantity}")

        except Exception as e:
            print(f"Ошибка обновления количества: {e}")
            raise

    # Обновление цены продукта
    def update_price(self, product_id, new_price):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("UPDATE products SET price = %s WHERE id = %s", (new_price, product_id))

                print(f"Продукт с ID: {product_id} обновлен, новая цена = {new_price}")

        except Exception as e:
            print(f"Ошибка обновления цены: {e}")
            raise

    # Удаление продукта со склада
    def delete_product(self, product_id):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("DELETE FROM products WHERE id = %s", (product_id,))

                    print(f"Продукт c ID: {product_id} удален")

        except Exception as e:
            print(f"Ошибка при удалении: {e}")
            raise