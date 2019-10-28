'''
Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print(f'O valor digitado {numero} é PAR.')
else:
    print(f'O Valor digitado {numero} é IMPAR.')
