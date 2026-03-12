class Logic:
    def __init__(self, data):
        self.db = data

    # Добавление продукта в БД
    def add_product_to_data(self, name, category, price, quantity):
        try:
            self.db.add_product(name, category, price, quantity)
            return True
        except Exception as e:
            print(f"[Logic] add_product_to_data error: {e}")
            return False

    # Получение списка продуктов из БД
    def get_products_from_data(self):
        try:
            return self.db.list_products()
        except Exception as e:
            print(f"[Logic] get_products_from_data error: {e}")
            return []

    # Обновление количества продукта в БД
    def update_product_quantity(self, product_id, new_quantity):
        if new_quantity < 0:
            print("[Logic] quantity не может быть отрицательным")
            return False
        try:
            self.db.update_quantity(product_id, new_quantity)
            return True
        except Exception as e:
            print(f"[Logic] update_product_quantity error: {e}")
            return False

    # Обновление цены продукта в БД
    def update_product_price(self, product_id, new_price):
        if new_price < 0:
            print("[Logic] price не может быть отрицательным")
            return False
        try:
            self.db.update_price(product_id=product_id, new_price=new_price)
            return True
        except Exception as e:
            print(f"[Lohic] update_product_price error: {e}")
            return False

    # Удаление продукта из БД
    def delete_product_from_data(self, product_id):
        try:
            self.db.delete_product(product_id)
            return True
        except Exception as e:
            print(f"[Logic] delete_product_from_data: {e}")