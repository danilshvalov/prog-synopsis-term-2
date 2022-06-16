class Person:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        assert age >= 0
        self.__age = age


p = Person(12)
print(p.get_age()) # 12
p.set_age(15)
print(p.get_age()) # 15
