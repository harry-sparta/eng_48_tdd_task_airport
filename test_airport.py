import pytest
from flight_trip import *

## 1.) Passenger --------------------------------------------------------------------------
    ## 1.1) Creating a Passenger
def test_create_passenger():
    assert Passenger('Bob','T00001').name == 'Bob'

    ## 1.2) Create a Passenger with 'Joana Thomson' with Passport number 'B343123'
def test_create_passenger_name_pnum():
    passenger_test_1 = Passenger('Joana Thomson', 'B343123')
    assert passenger_test_1.name == 'Joana Thomson' and passenger_test_1.pass_num == 'B343123'

    ## 1.3) Create a Passenger with 'Birt Kuman' with Passport number 'B13927'
    passenger_test_2 = Passenger('Birt Kuman', 'B13927')
    assert passenger_test_2.name == 'Birt Kuman' and passenger_test_2.pass_num == 'B13927'


    ## 1.4) Returns an error if user try to create Passenger with no name or Passport number
def test_create_passenger_error():
    with pytest.raises(TypeError):
        Passenger()

## 2.) Plane -------------------------------------------------------------------------------
    ## 2.1) Creating a Plane with plane number 'BA036'
def test_create_plane():
    assert Plane('BA036').plane_num == 'BA036'


## 3.) Flight trips ------------------------------------------------------------------------
    ## 2.1) Create a flight with no specific information
def test_create_flight():
    assert flight_trip('BA011', 'London', 'Edibourgh') != None

    ## 2.2) Add a plane with number 'BA011 to flight trip
def test_add_plane():
    assert flight_trip('BA022','Lisbon', 'London').plane_num == 'BA022'

    ## 2.3) Add a destination
def test_add_destination():
    assert flight_trip('BA009','Tokyo', 'London').destination == 'Tokyo'

    ## 2.4) Add an origin
def test_add_origin():
    assert flight_trip('BA009','Tokyo', 'Berlin').origin == 'Berlin'

    ## 2.5) Add a Passenger to a list of passengers
# passenger = []  # test_set_up - list of passengers
def test_add_passenger_to_list():
    passenger_list = flight_trip('BA099', 'Glasgow', 'Norwich')
    passenger_list.add_passenger('Jo', 'B99999')
    assert passenger_list.passenger_list[0].name == 'Jo'

    ## 2.6) Check if Passenger list is a list of objects that are Passengers
def test_added_passenger_list_type():
    passenger_list_test = flight_trip('BA099', 'Glasgow', 'Norwich')
    passenger_list_test.add_passenger('Jo', 'B99999')
    assert 'class' in str(type(passenger_list_test.passenger_list[0]))




