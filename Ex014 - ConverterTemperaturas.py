'''
Exercício Python 014: Escreva um programa que converta uma temperatura
digitando em graus Celsius e converta para graus Fahrenheit.
'''

temp = float(input("Digite a temperatura em graus Celsius para conversão: "))
tempFar = (temp * 1.8) + 32
print(f'Temperatura de {temp}ºC graus Celsius. \nConvertido para {tempFar}ºF graus Fahrenheit.')