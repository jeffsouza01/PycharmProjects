'''
Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e
mostre seu novo salário, com 15% de aumento.
'''

salario = float(input('Digite o valor do seu salário: R$ '))
nSalario = salario + (salario * 15) / 100 #calculo para descontar a porcentagem
print(f'O valor atual do seu salário é R${salario:.2f}.\n Seu novo salário será de R${nSalario:.2f}.')
