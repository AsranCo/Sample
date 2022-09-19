##مدیریت داروخانه

class Drug:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price


class Pharmacy:
    def __init__(self, name):
        self.name = name
        self.drugs = []
        self.employees = []

    def total_value(self):
        total = int()
        for drug in self.drugs:
            total += drug.amount * drug.price
        return total

    def add_drug(self, drug):
        self.drugs.append(drug)

    def add_employee(self, first_name, last_name, age):
        self.employees.append({
            "first_name": first_name,
            "last_name": last_name,
            "age": age
        })

#--------------------------todo use enumerate !!!
    def employees_summary(self):
        x = "Employees:\n"
        for i, emp in enumerate(self.employees):
            x += f"The employee number {i+1} is {emp['first_name']} {emp['last_name']} who is {emp['age']} years old.\n"
        # for i in range(len(self.employees)):
        #     x = x + f"The employee number {i + 1} is {self.employees[i]['first_name']} {self.employees[i]['last_name']} who is {self.employees[i]['age']} years old." + "\n"
        return x
