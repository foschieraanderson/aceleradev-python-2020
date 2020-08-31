from abc import ABC, abstractclassmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):

    WORKLOAD = 8
    PERCENTAGE_BONUS = 0.15

    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self.salary = salary
        self.__department = department

    @abstractclassmethod
    def calc_bonus(self):
        pass

    @classmethod
    def get_hours(cls):
        return cls.WORKLOAD

    def get_department(self):
        return self.__department.name

    def set_department(self, departament_name):
        self.__department.name = departament_name


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * Employee.PERCENTAGE_BONUS


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * Employee.PERCENTAGE_BONUS

    def get_sales(self):
        return self.__sales

    def put_sales(self, sale):
        self.__sales += sale