'''
Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

frase = str(input('Digite uma frase: ')).upper().strip()
contador = frase.count("A")
print(f'Nesta frase a letra A aparece {contador} vezes.')
print(f'A primeira letra A aparece na posição {frase.find("A") + 1}.')
print(f'A ultima letra A aparece na posição {frase.rfind("A") + 1}.')
