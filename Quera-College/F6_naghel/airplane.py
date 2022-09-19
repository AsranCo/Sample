# Your imports goes here
from ground_vehicle import GroundVehicle
from flying_vehicle import FlyingVehicle


class Airplane(FlyingVehicle, GroundVehicle):
    def __init__(self, airline, number_of_crew, captain, fuel, number_of_fins, name, price, number_of_seats, max_speed,
                 **kwargs):
        super().__init__(fuel, number_of_fins, name, price, number_of_seats, max_speed, **kwargs)
        self.airline = airline
        self.number_of_crew = number_of_crew
        self.captain = captain
        self.kwargs = kwargs


class B707(Airplane):
    def __init__(self, airline, number_of_crew, captain, fuel, number_of_fins, name, price, number_of_seats, max_speed,
                 **kwargs):
        super().__init__(airline, number_of_crew, captain, fuel, number_of_fins, name, price, number_of_seats,
                         max_speed, **kwargs)
