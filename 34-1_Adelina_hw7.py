import sqlite3


conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      product_title VARCHAR(200) NOT NULL,
                      price NUMERIC(10, 2) DEFAULT 0.0 NOT NULL,
                      quantity INTEGER DEFAULT 0 NOT NULL
                      )''')

conn.commit()


def add_products():
    try:
        products = [
            ("Шампунь", 349.99, 100),
            ("Зубная паста", 249.99, 200),
            ("Мыло", 29.99, 200),
            ("Жидкое мыло", 129.99, 30),
            ("Пенка для умывания", 999.99, 40),
            ("Зубная щетка", 99.99, 150),
            ("Крем для рук", 1299.99, 60),
            ("Увлажняющая сыворотка для лица", 1499.99, 20),
            ("Крем для лица", 3299.99, 80),
            ("Бальзам для волос", 599.99, 70),
            ("Кондиционер для волос", 499.99, 80),
            ("Гель для укладки волос", 79.99, 20),
            ("Масло для губ", 4499.99, 10),
            ("Тонер для лица", 1399.99, 40),
            ("Блеск для губ", 5499.99, 30)
        ]
        cursor.executemany("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", products)
        conn.commit()
    except sqlite3.Error as e:
        print("Ошибка при добавлении товаров:", e)


def change_quantity_by_id(product_id, new_quantity):
    try:
        cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
        conn.commit()
    except sqlite3.Error as e:
        print("Ошибка при изменении количества товара:", e)


def change_price_by_id(product_id, new_price):
    try:
        cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
        conn.commit()
    except sqlite3.Error as e:
        print("Ошибка при изменении цены товара:", e)


def delete_product_by_id(product_id):
    try:
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
    except sqlite3.Error as e:
        print("Ошибка при удалении товара:", e)


def select_all_products():
    try:
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        for product in products:
            print(product)
    except sqlite3.Error as e:
        print("Ошибка при выборе всех товаров:", e)


def select_cheap_and_abundant_products():
    try:
        cursor.execute("SELECT * FROM products WHERE price < 100.0 AND quantity > 5")
        products = cursor.fetchall()
        for product in products:
            print(product)
    except sqlite3.Error as e:
        print("Ошибка при выборе дешевых товаров, имеющихся в большом количестве:", e)


def search_products_by_title(keyword):
    try:
        cursor.execute("SELECT * FROM products WHERE product_title LIKE ?", ('%' + keyword + '%',))
        products = cursor.fetchall()
        for product in products:
            print(product)
    except sqlite3.Error as e:
        print("Ошибка при поиске товаров по названию:", e)


add_products()
change_quantity_by_id(1, 55)
change_price_by_id(2, 229.99)
delete_product_by_id(3)
select_all_products()
select_cheap_and_abundant_products()
search_products_by_title("Крем")

conn.close()
