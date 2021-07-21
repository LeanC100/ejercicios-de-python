import math

class Square():

    def calculate_area(self):
        l = input('Enter the side :')
        try:
            l = int(l)
        except ValueError:
            input('Invalid value')

        return l * l 

    def calculate_parameter(self):
        a = input('Enter the side :')
        try:
            a = int(a)
        except ValueError:
            input('Invalid value')

        return 4 * a
