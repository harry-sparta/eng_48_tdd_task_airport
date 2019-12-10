# Passenger class file
class Passenger():
    try:
        def __init__(self, name, pass_num):
            self.name = name
            self.pass_num = pass_num
    except TypeError as error_type_syntax:
        print('Check if you have 2 arguments to create a passenger')
        print(error_type_syntax)
        raise error_type_syntax
    finally:
        # print('code executed') # if required
            pass
