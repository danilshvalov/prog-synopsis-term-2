import abc
import math
from enum import Enum, auto


class CallType(Enum):
    """
    Тип звонка: мобильный или городской
    """

    Mobile = auto()
    City = auto()


class Tariff(abc.ABC):
    """
    Абстрактный класс тарифа, буквально интерфейс тарифа.

    Все тарифы должны быть унаследованы от этого класса.
    """

    @abc.abstractmethod
    def get_call_price(self, time, call_type):
        pass


class RegularTariff(Tariff):
    """
    Повременный тариф. Реализация простая: умножаем время на стоимость
    в зависимости от типа звонка.
    """

    def __init__(self, mobile_price=1, city_price=5):
        self.mobile_price = mobile_price
        self.city_price = city_price

    def get_call_price(self, time, call_type):
        if call_type == CallType.Mobile:
            return time * self.mobile_price
        else:
            return time * self.city_price


class BigTalkTariff(Tariff):
    """
    Тариф После10МинутВ2РазаДешевле. При создании этого тарифа возникает дилемма:
    унаследовать ли этот класс от `RegularTariff`. Я решил, что это неудачный
    вариант, поскольку в таком случае растет связность этих классов. В данном
    случае дублирование лучше, чем сомнительное наследование
    """

    def __init__(self, mobile_price=1, city_price=5):
        self.mobile_price = mobile_price
        self.city_price = city_price

    def get_call_price(self, time, call_type):
        if call_type == CallType.Mobile:
            return time * self.mobile_price

        if time <= 10:
            return time * self.city_price
        else:
            return self.city_price * 10 + math.ceil((time - 10) * self.city_price / 2)


class SmallTalkTariff(Tariff):
    """
    Тариф ПлатиМеньшеДо5Минут. Здесь рассуждения те же, что и в `BigTalkTariff`
    """

    def __init__(self, mobile_price=1, city_price=5):
        self.mobile_price = mobile_price
        self.city_price = city_price

    def get_call_price(self, time, call_type):
        if call_type == CallType.Mobile:
            price = self.mobile_price
        else:
            price = self.city_price

        if time <= 5:
            return time * price // 2
        else:
            return math.ceil(5 * price / 2) + (time - 5) * price * 2


class Customer:
    """
    Класс клиента. Для упрощения реализации будем считать, что все данные
    валидны, а баланс не отрицателен.
    """

    def __init__(self, name, tariff):
        self.name = name
        self.tariff = tariff
        self.balance = 0

    def record_payment(self, payment):
        self.balance += payment

    def record_call(self, time, call_type):
        self.balance -= self.tariff.get_call_price(time, call_type)


c1 = Customer("Ivan", RegularTariff())
c2 = Customer("Peter", BigTalkTariff())
c3 = Customer("Dmitriy", SmallTalkTariff())

c1.record_payment(1000)
c2.record_payment(1000)
c3.record_payment(1000)

c1.record_call(20, CallType.City)
print(c1.balance)  # 1000 - 20 * 5 = 900
c1.record_call(20, CallType.Mobile)
print(c1.balance)  # 900 - 20 = 880

c2.record_call(20, CallType.City)
print(c2.balance)  # 1000 - 10 * 5 - 5 * 5 = 925
c2.record_call(20, CallType.Mobile)
print(c2.balance)  # 925 - 20 = 905

c3.record_call(20, CallType.City)
print(c3.balance)  # 1000 - math.ceil(5 * 2.5) + 15 * 10 = 837
c3.record_call(20, CallType.Mobile)
print(c3.balance)  # 837 - math.ceil(5 * 0.5) + 15 * 2 = 804
