'''Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e
mostre na tela cada um dos dígitos separados.'''

numero = int(input('Informe um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'Analisando o número {numero}...\n'
      f'Unidade: {u}\n'
      f'Dezena: {d}\n'
      f'Centena: {c}\n'
      f'Milhar: {m}\n')
