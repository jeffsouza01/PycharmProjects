'''
Exercício Python 012: Faça um algoritmo que leia o preço de um produto e
mostre seu novo preço, com 5% de desconto.
'''

produto = float(input('Digite o preço do produto: R$'))
nProduto = produto - (produto * 5) / 100
print(f'O valor do produto é R${produto:.2f}. Totalizando R${nProduto:.2f} com desconto aplicado de 5%.')
