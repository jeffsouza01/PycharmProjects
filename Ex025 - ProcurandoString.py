'''
Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

nome = str(input('Digite seu nome: ')).upper().split()
print('O Seu nome tem Silva? ', 'SILVA' in nome)
