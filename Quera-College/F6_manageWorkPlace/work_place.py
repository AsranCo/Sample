class WorkPlaceIsFull(...):
    pass


class Consts:
    # You can change these numbers to your custom prices
    BASE_PRICE = {'mine': 300, 'school': 100, 'company': 200}
    BASE_PLACE_COST = 1000
    LEVEL_MUL = 10


class WorkPlace:

    def __init__(self, name):
        pass

    def get_price(self):
        pass

    def calc_costs(self):
        pass

    def upgrade(self):
        pass

    def hire(self, person):
        pass

    def get_expertise(self):
        pass

    def calc(self):
        pass

    @staticmethod
    def calc_all():
        pass
