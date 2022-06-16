class Employee:
    def __init__(self, idx, salary):
        self.__id = idx
        self.__salary = salary

    def get_id(self):
        return self.__id

    def get_salary(self):
        return self.__salary

    def set_id(self, idx):
        self.__id = idx

    def set_salary(self, salary):
        self.__salary = salary


staff = []

for i in range(3):
    print(f"Введите информацию о сотруднике #{i + 1}")
    idx = int(input("Введите номер сотрудника: "))
    salary = int(input("Введите оклад сотрудника: "))
    staff.append(Employee(idx, salary))

for emp in staff:
    print(f'Сотрудник "{emp.get_id()}" получает {emp.get_salary()}')
