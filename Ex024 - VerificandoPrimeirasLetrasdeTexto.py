'''
Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
'''

cidade = str(input('Em que cidade você nasceu: ')).strip().split()
if cidade[0].upper() == 'SANTO':
    print('VERDADE')
else:
    print('MENTIRA')
