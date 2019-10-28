'''
Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite
'''

velocidade = float(input('Informe a velocidade do veículo: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado! Pois estava a {velocidade} Km/h.\n'
          f'Velocidade Máxima permitida: 80 km/h\n'
          f'Valor total da multa: R${multa:.2f}')
else:
    print(f'Você esta dentro da velocidade permitida. \n'
          f'Velocidade Máxima permitida: 80 km/h\n'
          f'Velocidade registrada: {velocidade} Km/h')
print('Tenha um bom dia! Dirija com segurança!')