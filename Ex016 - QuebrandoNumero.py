'''
Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e
mostre na tela a sua porção Inteira.
'''
import  math
valor = float(input('Digite um número: '))
#print(f'O valor digitado foi {valor}. Sua porção inteira é {int(valor)}.')
#Utilizando o metodo math
print(f'O valor digitado foi {valor}. Sua porção inteira é {math.trunc(valor)}.')
