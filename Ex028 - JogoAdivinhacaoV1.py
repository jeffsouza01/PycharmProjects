'''
Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random

vis = "*" * 10
print(f'\033[0;33m {"-=-" * 20} \033[m') #Utilização em cores com \33[m
print(f'{vis} \33[34m Jogo do Advinha v1.0 \33[m {vis} '.center(60))
print(f'\033[0;33m{"-=-" * 20} \033[m')
numeroPC = random.randint(0, 5)
print('O Computador pensou em um número entre 0 à 5.')
print(f'\033[0;33m{"-=-" * 20} \033[m')
numeroUser = int(input('Tente descobrir qual foi o número: '))
print(f'Você digitou o número {numeroUser} e o computador {numeroPC}.')
if numeroUser == numeroPC:
    print('\33[1;36m Parabéns, Você acertou! \33[m')
else:
    print('\33[1;31m Que pena... Você errou!\33[m')
