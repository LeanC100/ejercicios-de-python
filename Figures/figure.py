from circle import Circle
from rectangle import Rectangle
from rhombus import Rhombus
from square import Square
from triangle import Triangle

import os


class Figrure():


    def area(self):
        op_select = self.sub_menu()
        result =op_select.calculate_area()
        print(f'The result is: {result:.2f}')
        input('\n     back')
        
    def parameter(self):
        op_select = self.sub_menu()
        result = op_select.calculate_parameter()
        print(f'The result is: {result:.2f}')
        input('\n     back')
    
    def sub_menu(self):
        CIRCLE = 1
        SQUARE = 2
        TRIANGLE = 3
        RECTANGLE = 4
        RHOMBUS = 5
        BACK = 0

        CONTINUE=True

        while CONTINUE:
            os.system('cls')
            print('     Calculate area and perimeter geometric figures \n')
            print(f'''Select a figure:
        {CIRCLE}- Circle
        {SQUARE}- Square
        {TRIANGLE}- Triangle
        {RECTANGLE}- RectangLe
        {RHOMBUS}- Rhombus
        {BACK}- exit ''')
            op = input('Select a option: ')
            try:
                op = int(op)
            except ValueError:
                op = -1
            os.system('cls')
            if op == CIRCLE:
                return Circle()
            elif op == SQUARE:
                return Square()
            elif op == TRIANGLE:
                return Triangle()
            elif op == RECTANGLE:
                return Rectangle()
            elif op == RHOMBUS:
                return Rhombus()
            elif op == BACK:
                CONTINUE=False
            else:
                print('Option no valid')
                print('Please, Select other option')
            print('')

    def menu(self):
        AREA=1
        PARAMETER=2
        EXIT=0
        
        CONTINUE=True

        while CONTINUE:
            os.system('cls')
            print('     Calculate area and parameter geometric figures \n')
            print(f'''Select a option:
            {AREA}- Area
            {PARAMETER}- Parameter
            {EXIT}- exit ''')
            op = input('Select a option: ')
            try:
                op = int(op)
            except ValueError:
                op = -1
            if op == AREA:
                self.area()
            elif op == PARAMETER:
                self.parameter()
            elif op == EXIT:
                CONTINUE=False
            else:
                print('Option no valid')
                print('Please, Select other option')
            print('')
