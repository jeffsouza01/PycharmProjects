'''
Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e
mostre na tela a sua tabuada.
'''

num = int(input('Digite o número que deseja saber a tabuada: '))
print(8*'***')
for i in range(1, 10):
    print(f'{num} x {i} = {num*i}')
print(8*'***')
