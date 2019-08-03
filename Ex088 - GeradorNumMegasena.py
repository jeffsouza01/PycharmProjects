'''
Exercício Python: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
from random import randint
from time import sleep 
aposta = []
temp = list()
num = 0

print('-=' * 20)
print('{:^40}'.format("MEGA SENA"))
print('-=' * 20)

qaposta = int(input('Gostaria de quantas apostas? '))
cont = 0

# inicio do laço referente a quantidade a ser digitada
for v in range(qaposta):
  while True:
    num = randint(1, 60) 
    if num not in temp: # adiconando valores não repetidos 
      temp.append(num)
      cont += 1
    if cont >= 6:
      break
  aposta.append(temp[:])
  temp.clear()
  cont = 0
  
print()
print('-' * 11, 'Sorteando {} Jogos'.format(qaposta), '-' * 11)
for pos, l in enumerate(aposta):
  l.sort()
  print('Jogo {}: {}'.format(pos+1, l))
  sleep(1)
print('-=' * 6, '<- BOA SORTE! ->', '=-' * 6)
