import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# создание объекта Engine БД
engine = sa.create_engine("sqlite:///product.db")

# создаем сессию
Session = sessionmaker(bind=engine)

session = Session()

# определения таблиц и связанных объектов (индекс, представление, триггеры)
# хранятся в метаданных. MetaData — это коллекция объектов Table и связанных
# с ними конструкции схем, которая также содержит привязку к Engine или
# Connection
# meta = sa.MetaData()
Base = declarative_base()


# объявляем таблицу
class Product(Base):
    __tablename__ = "product"

    id = sa.Column(
        "product_id",
        sa.Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True,
    )
    name = sa.Column("product_name", sa.String)


# создаем все таблицы в БД
Base.metadata.create_all(engine)

# добавляем новый объект
session.add(Product(name="Apple"))
# добавляем сразу несколько
session.add_all(
    [
        Product(name="Book"),
        Product(name="Pen"),
        Product(name="Pineapple"),
        Product(name="Table"),
    ]
)
# фиксируем изменения
session.commit()

# получить все строки из БД
for p in session.query(Product).all():
    print(p.name)  # Apple, Book, Pen, Pineapple, Table
print("---")

# получить первый
p = session.query(Product).where(Product.id >= 3).first()
print(p.name)  # Pen
print("---")

# получить по ID
p = session.query(Product).get(3)
print(p.name)  # Pen
print("---")

# изменение строки в БД
session.query(Product).where(Product.id == 3).update(
    {Product.name: "Notebook"},
    synchronize_session=False,
)
session.commit()

p = session.query(Product).where(Product.id == 3).first()
print(p.name)  # Notebook
print("---")

# удаление строки в БД
session.query(Product).where(Product.id == 3).delete()
session.commit()

p = session.query(Product).where(Product.id == 3).first()
print(p)  # None
print("---")

