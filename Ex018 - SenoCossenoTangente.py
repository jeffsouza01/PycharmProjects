'''
Exercício Python 018: Faça um programa que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

import math

angulo = float(input('Digite o valor do angulo: '))
seno = math.sin(angulo)
coseno = math.cos(angulo)
tang = math.tan(angulo)
print(f'O ângulo de {angulo}º tem o SENO de {seno:.2f}. \n'
      f'O ângulo de {angulo}º tem o COSSENO de {coseno:.2f}\n'
      f'O ângulo de {angulo}º tem a TANGENTE de {tang:.2f}\n')
