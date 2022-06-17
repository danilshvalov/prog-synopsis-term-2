import sqlite3


conn = sqlite3.connect("animals.db")  # БД сохраняется на диск
# или
conn = sqlite3.connect(":memory:")  # БД создается в ОЗУ

cursor = conn.cursor()  # курсор требуется для выполнения SQL запросов

cursor.execute("<SQL-query>")  # выполнение <SQL-query>

cursor.executescript(
    """
<SQL-query-1>;
<SQL-query-2>;
...
<SQL-query-n>;
"""
)  # выполнение нескольких запросов

data = [(0, 5), (1, 3), (2, 3)]
cursor.executemany(
    "INSERT INTO product VALUES(?, ?)", data
)  # вставка нескольких строк в БД


price = 5
cursor.execute(
    "SELECT * FROM product WHERE price <= ?", price
)  # price подставится на место знака вопроса


cursor.execute(
    "SELECT * FROM product WHERE price < :price", {"price": price}
)  # price подставится на место :price

query = cursor.execute("SELECT * FROM product")
all_products = query.fetchall()  # получить все товары
one_product = query.fetchone()  # получить только один
five_products = query.fetchmany(5)  # получить 5 товаров

conn.commit()  # зафиксировать изменения
