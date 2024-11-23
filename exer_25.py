'''
Faça um programa que leia uma frase pelo teclado
e mostre quantas vezes aparece a letra "A", em que posição ela
aparece a primeira vez e em que posição ela aparece a ultima vez
'''
from itertools import count

frase = input('por favor, digite uma frase: ').strip().lower()
print(f'A letra "A" aparece {frase.count('a')} vezes;'
      f'\nEla aparece pela primeira vez na posição {frase.find('a')+1}, e'
      f'\naparece por ultimo na poisção {frase.rfind('a')+1}')

