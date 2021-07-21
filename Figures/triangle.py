import math

class Triangle():

    def calculate_area(self):
        h = input('Enter the side :')
        b = input('Enter the side :')
        try:
            h = int(h)
            b = int(b)
        except ValueError:
            input('Invalid value')

        return  (b*h) * 2

    def calculate_parameter(self):
        l = input('Enter the side :')
        m = input('Enter the side :')
        n = input('Enter the side :')
        try:
            l = int(l)
            m = int(m)
            n = int(n)
        except ValueError:
            input('Invalid value')

        return l + m + n

