# Flight trip class file
from passenger import *
from plane import *

class flight_trip():
    # Attributes
    try:
        def __init__(self, plane_num, destination, origin):
            self.plane_num = plane_num
            self.destination = destination
            self.origin = origin
            self.passenger_list = []
            pass
    except:
        pass

    # Methods
    try:
        def add_passenger(self, name, pass_num):
            return self.passenger_list.append(Passenger(name, pass_num))
    except:
        pass

