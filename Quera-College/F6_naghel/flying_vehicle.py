from vehicle import Vehicle


class FlyingVehicle(Vehicle):
    def __init__(self, fuel, number_of_fins, name, price, number_of_seats, max_speed, **kwargs):
        super().__init__(name, price, number_of_seats, max_speed)
        self.fuel = fuel
        self.number_of_fins = number_of_fins
        self.kwargs = kwargs
