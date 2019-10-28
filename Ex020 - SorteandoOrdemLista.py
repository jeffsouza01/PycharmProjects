'''
Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação
de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

import random

listaAlunos = []

for i in range(0, 4):
    alunos = input(f'Digite o nome do {i + 1}º aluno: ')
    listaAlunos.append(alunos)
print(listaAlunos)
random.shuffle(listaAlunos)
print(f'A ordem de apresentação dos alunos sera: {listaAlunos}')
