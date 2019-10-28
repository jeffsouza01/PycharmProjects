'''
Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

simb = '>'
simb2 = '<'
print(f'{15 * simb} Aluguel de Carros {simb2 * 15}\n')
distanciaPercorrida = float(input('Informa qual foi a distancia percorrida em quilômetros: '))
diasAlugados = int(input('Informe a quantidade de dias que foi alugado: '))
custoTotal = (distanciaPercorrida * 0.15) + (diasAlugados * 60)
print(f'O carro alugado percorreu {distanciaPercorrida} KM de distância. \nFoi alugado durante {diasAlugados} dias.')
print(f'Total a ser pago: R$ {custoTotal:.2f}')