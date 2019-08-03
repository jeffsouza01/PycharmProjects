'''
Exercício Python 006: Crie um algoritmo que leia um número e
mostre o seu dobro, triplo e raiz quadrada.
'''
import math
num = int(input('Digite um número: '))
#Utilizando váriaveis para soma dos valores, sendo possível inserir diretamente no Print.
dobro = num * 2
tri = num * 3
raiz = num ** (1/2)
print(f'O dobro de {num} é igual a {dobro}.')
print(f'O triplo de {num} é igual a {tri}.')
print(f'A Raiz Quadrada de {num} é igual a {raiz:.2f}')
#Segundo método utilizando a biblioteca MATH para raiz quadrada
print(f'A Raiz Quadrada de {num} é igual a {math.sqrt(num):.2f}')
#Terceiro método utilizando a função de Power (potencia) para raiz quadrada
print(f'A Raiz Quadrada de {num} é igual a {pow(num, (1/2)):.2f}')