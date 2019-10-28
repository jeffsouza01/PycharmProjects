'''
Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e
R$0,45 parta viagens mais longas.
'''

viagem = float(input('Informe qual será a distância de sua viagem: '))
# if viagem > 200:
#     valor = viagem * 0.45
# else:
#     valor = viagem * 0.50
# Utilizando if simplificado
valor = viagem * 0.45 if viagem > 200 else viagem * 0.50
print(f'Sua viagem será de {viagem:.1f} Km.\n'
      f'O preço da sua passagem será de R${valor:.2f}')
