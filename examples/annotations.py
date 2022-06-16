class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        assert age >= 0
        self.__age = age

p = Person(12)
print(p.age) # 12
p.age = 15
print(p.age) # 15
