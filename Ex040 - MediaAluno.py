'''
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print('=-=' * 10)
if media >= 7:
    print(f'Parabéns, Foi APROVADO! \n'
          f'Sua média foi: {media}')
elif media >= 5:
    print(f'Se esforçe mais, Ficou de RECUPERAÇÂO. \n'
          f'Sua média foi {media}.')
else:
    print(f'Infelizmente foi REPROVADO! \n'
          f'Sua média foi {media}.')
