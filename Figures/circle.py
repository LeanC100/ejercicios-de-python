import math

class Circle():

    def calculate_area(self):
        r = input('Enter the radius:')
        try:
            r = int(r)
        except ValueError:
            input('invalid value')

        return math.pi * (r * r)

    def calculate_parameter(self):
        r = input('Enter the radius:')
        try:
            r = int(r)
        except ValueError:
            input('invalid value')

        return 2 * math.pi * r

