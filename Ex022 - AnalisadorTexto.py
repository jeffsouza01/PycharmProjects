'''Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).'''

nome = str(input('Digite seu nome completo: ')).strip()
print(f'O seu nome completo é : {nome.title()}')
print(f'Seu nome em maiusculo: {nome.upper()}\n'
      f'Seu nome em minusculo: {nome.lower()}\n'
      f'Seu nome completo tem {len(nome) - nome.count(" ")} letras.')
nomeSeparado = nome.split()
print(f'Seu primeiro nome é {nomeSeparado[0]} e tem {len(nomeSeparado[0])} letras.')
