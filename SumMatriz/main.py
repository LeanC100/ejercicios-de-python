'''
    Suma entre matricez con numeros aleatorios
'''

import random

N = 3

matriz1 = [[random.randint(10, 70) for j in range(N)] for i in range(N)]

matriz2 = [[random.randint(10,70) for j in range(N)] for i in range(N)]

resultado = []

x= 0

for i in range(N):
    for j in range(N):
        resultado.append(matriz1[i][j] + matriz2[i][j])
        print(f'{matriz1[i][j]} + {matriz2[i][j]} = {resultado[x]}')
        x+=1

