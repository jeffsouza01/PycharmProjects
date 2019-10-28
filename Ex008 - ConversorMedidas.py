'''
Exercício Python 008: Escreva um programa que leia um valor em metros e
o exiba convertido em centímetros e milímetros.
'''

valor = float(input('Digite o valor em Metros: '))
vcent = valor * 100
mcent = valor * 1000
print(f'Você digitou {valor} Metros. \n Sendo o Valor convertido em Centimetros é {vcent} cm \n Valor convertido em Milimetros é {mcent} mm')