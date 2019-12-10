# Flight trip class file
from passenger import *
from plane import *


class FlightTrip():
    # Attributes
    try:
        def __init__(self, plane_num="TBC", destination="TBC", origin="TBC"):
            self.plane_num = plane_num
            self.destination = destination
            self.origin = origin
            self.passenger_list = []
            pass
    except:
        pass

    # Methods
    try:
        def add_plane(self, plane_num):
            self.plane_num = plane_num
    except:
        pass

    try:
        def add_destination(self, destination):
            self.destination = destination
    except:
        pass

    try:
        def add_origin(self, origin):
            self.origin = origin
    except:
        pass

    try:
        def add_passenger(self, name, pass_num):
            return self.passenger_list.append(Passenger(name, pass_num))
    except:
        pass

