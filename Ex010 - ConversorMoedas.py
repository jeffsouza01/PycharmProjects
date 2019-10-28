'''
Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
mostre quantos dólares ela pode comprar.
'''

din = float(input('Digite o valor que possui atualmente: R$ '))
#Convertendo os valores, sendo que pode usar uma váriavel ou diretamente pelo print
dolar = din / 3.89
euro = din / 4.33
print(f'Atualmente, você possui R$ {din:.2f} reais. \nPoderá ter U$ {dolar:.2f} doláres ou € {euro:.2f} Euros.')