'''
Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e
do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''

import math

catOposto = float(input('Digite o comprimento do cateto oposto: '))
catAdjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = math.hypot(catOposto, catAdjacente)
#Segundo metodo utilizando calculo
hipotenusa2 = (catAdjacente ** 2 + catOposto ** 2) ** (1/2)
print(f'A Hipotenusa vai medir {hipotenusa:.2f}.')
