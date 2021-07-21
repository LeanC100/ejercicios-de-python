import math

class Rhombus():

    def calculate_area(self):
        D = input('Enter the major side :')
        d = input('Enter the minor side :')
        try:
            D = int(D)
            d = int(d)
        except ValueError:
            input('Invalid value')

        return (D *d) / 2

    def calculate_parameter(self):
        a = input('Enter the side :')
        try:
            a = int(a)
        except ValueError:
            input('Invalid value')

        return 4 * a

