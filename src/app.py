from database import Database
from logic import Logic

def is_valid_int(string):
    if not string.isdigit():
        new_string = input("Ошибка ввода! Введите целое число: ")
        return is_valid_int(new_string)
    return int(string)

def is_valid_float(string):
    try:
        return float(string.replace(",", "."))
    except ValueError:
        new_string = input("Ошибка ввода! Введите число: ")
        return is_valid_float(new_string)

def main():
    data = Database()
    data.create_table()

    db = Logic(data)

    print(f"Добро пожаловать в наш склад")
    print("""Основные функции склада:
        1) Добавить продукт на склад
        2) Получить список продуктов на складе
        3) Обновить количество продукта на складе
        4) Обновить цену продукта на складе в процессе
        5) Удалить продукт со склада
        6) Покинуть склад""")
    while True:
        pick = input("Введите номер функции: ")
        match pick:
            case "1":
                print("Введите имя, категорию, цену и количество товара (через Enter):")

                name, category, price, quantity = input().lower(), input().lower(), is_valid_float(input()), is_valid_int(input())
                db.add_product_to_data(name=name, category=category, price=price, quantity=quantity)

            case "2":
                db.get_products_from_data()

            case "3":
                print("Введите ID продукта и новое количество (через Enter): ")
                product_id, new_quantity = is_valid_int(input()), is_valid_int(input())
                db.update_product_quantity(product_id=product_id, new_quantity=new_quantity)

            case "4":
                print("Введите ID продукта и новую цену (через Enter): ")
                product_id, new_price = is_valid_int(input()), is_valid_float(input())
                db.update_product_price(product_id=product_id, new_price=new_price)

            case "5":
                product_id = is_valid_int(input("Введите ID продукта, который вы хотите удалить: "))
                db.delete_product_from_data(product_id=product_id)

            case "6":
                break

            case _:
                print("Неизвестная функция")

    print("До встречи! Было приятно поработать вместе")


if __name__ == "__main__":
    main()