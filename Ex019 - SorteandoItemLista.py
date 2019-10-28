'''
Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''
import random

listaAlunos = []

for i in range(0, 4):
    aluno = input(f'Digite o nome do {i+ 1}º aluno: ')
    listaAlunos.append(aluno)

print(f'O Aluno sorteado foi {random.choice(listaAlunos)}.')
