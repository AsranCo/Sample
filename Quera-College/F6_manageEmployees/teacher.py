import math

from person import Person, Consts


class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.age = age
        self.job = "teacher"

    def get_price(self):
        price = Consts.BASE_PRICE.get("teacher") - (self.age - Consts.MIN_AGE) * Consts.AGE_MUL
        return price

    def calc_life_cost(self):
        costs = Consts.BASE_PRICE.get("teacher") + (self.age - Consts.MIN_AGE) * Consts.AGE_MUL
        return costs

    def calc_income(self):
        income = Consts.BASE_PRICE.get("teacher") - (self.age - Consts.MIN_AGE) * Consts.AGE_MUL
        return income
