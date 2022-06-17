import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

# создание объекта Engine БД
engine = sa.create_engine("sqlite:///product.db")

# создаем соединение с БД
conn = engine.connect()

# определения таблиц и связанных объектов (индекс, представление, триггеры)
# хранятся в метаданных. MetaData — это коллекция объектов Table и связанных
# с ними конструкции схем, которая также содержит привязку к Engine или
# Connection
meta = sa.MetaData()
meta.bind = engine

# Table представляют собой соответствующую таблицу в БД
product = sa.Table(
    "product",
    meta,
    sa.Column(
        "product_id",
        sa.Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True,
    ),
    sa.Column("product_name", sa.String),
)

# создание таблицы в БД
meta.create_all(engine)

# добавляем одно значение
conn.execute(sa.insert(product).values(product_name="Book"))

# добавляем несколько значений
conn.execute(
    sa.insert(product),
    [
        {"product_name": "Table"},
        {"product_name": "Apple"},
        {"product_name": "Pineapple"},
        {"product_name": "Pen"},
    ],
)

# выбрать все строки
p_list = conn.execute(sa.select(product))
for p in p_list:
    print(p[1])  # Book, Table, Apple, Pineapple, Pen
print("---")


# выборка с условием
p_list = conn.execute(sa.select(product).where(product.c.product_id >= 3))
for p in p_list:
    print(p[1])  # Apple, Pineapple, Pen
print("---")

# выбрать первый элемент
p = conn.execute(sa.select(product).where(product.c.product_id == 3)).first()
print(p[1])  # Apple
print("---")

# изменение строки по ID
conn.execute(
    sa.update(product).where(product.c.product_id == 3).values(product_name="Notebook")
)
p = conn.execute(sa.select(product).where(product.c.product_id == 3)).first()
print(p[1])  # Notebook
print("---")

# удаление строки по ID
conn.execute(sa.delete(product).where(product.c.product_id == 3))
p = conn.execute(sa.select(product).where(product.c.product_id == 3)).first()
print(p)  # None
print("---")
