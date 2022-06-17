import peewee as pw


conn = pw.SqliteDatabase("product.db")  # создание соединения с БД
cursor = conn.cursor()  # курсор для выполнения запросов


# базовая модель (это, так сказать, база)
class BaseModel(pw.Model):
    class Meta:
        database = conn


# описание модели (таблицы) товара, поля — столбцы таблицы
class Product(BaseModel):
    # можно изменять название полей в БД
    id = pw.AutoField(column_name="product_id")
    name = pw.TextField(column_name="product_name")

    class Meta:
        table_name = "product"


# создаем саму таблицу
Product.create_table()

# различные способы создания записи в БД
Product(name="Book").save()
Product.create(name="Table")
Product.insert({"name": "Apple"}).execute()
Product.insert_many([{"name": "Pen"}, {"name": "Pineapple"}]).execute()

# выбор всех товаров
products = Product.select().execute()
for p in products:
    print(p.name)  # Book, Table, Apple, Pen, Pineapple
print("---")

# выбрать первые 3
products = Product.select().limit(3).execute()
for p in products:
    print(p.name)  # Book, Table, Apple
print("---")

# выбрать товар с ID = 1
p = Product.select().where(Product.id == 1).first()
print(p.name)  # Book
print("---")

# SQL запрос
cursor.execute("SELECT * FROM product WHERE product_id >= 3")
products = cursor.fetchall()
for p in products:
    print(p[1])  # Apple, Pen, Pineapple
print("---")


# изменение товара
Product.update(name="Audio").where(Product.id == 1).execute()
p = Product.select().where(Product.id == 1).first()
print(p.name)  # Audio

# удаление товара
Product.delete().where(Product.id == 1).execute()
p = Product.select().where(Product.id == 1).first()
print(p)  # None

conn.close()  # закрыть соединение с БД
