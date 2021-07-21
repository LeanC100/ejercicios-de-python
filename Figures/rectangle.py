import math

class Rectangle():

    def calculate_area(self):
        b = input('Enter the first side :')
        h = input('Enter the first side :')
        try:
            h = int(h)
            b = int(b)
        except ValueError:
            input('invalid value')

        return b * h

    def calculate_parameter(self):
        b = input('Enter the first side :')
        h = input('Enter the first side :')
        try:
            h = int(h)
            b = int(b)
        except ValueError:
            input('Invalid value')
        
        return 2*h + 2*b

