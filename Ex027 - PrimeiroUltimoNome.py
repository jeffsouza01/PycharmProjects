'''
Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
'''

nomec = str(input('Digite seu nome completo: ')).strip()
print(f'Muito prazer em te conhecer, {nomec}!')
nomeDividido = nomec.split()
primeiroNome = nomeDividido[0]
ultimoNome = nomeDividido[len(nomeDividido) - 1]
print(f'Seu primeiro nome: {primeiroNome}\n'
      f'Seu ultimo nome: {ultimoNome}')
