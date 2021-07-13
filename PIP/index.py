from camelcase import CamelCase
import os


c = CamelCase()

print('     Normal to CamelCase \n')

s = input('Enter the text: \n')

os.system('cls')
print('Text normal: ',s)

print('Text Camelcase: ', c.hump(s))
