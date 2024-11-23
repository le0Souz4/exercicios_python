"""
o mesmo professor do exer_18 quer sortear a ordem de apresentação
de trabalhos dos alunos. Faça um programa que leia o nome
dos quatro alunos e mostre a ordem sorteada
"""

import random

aluno1 = input("digite o nome do 1° aluno: ")
aluno2 = input("digite o nome do 2° aluno: ")
aluno3 = input("digite o nome do 3° aluno: ")
aluno4 = input("digite o nome do 4° aluno: ")
lista = [aluno1,aluno2, aluno3, aluno4]
random.shuffle(lista)
print(f'a ordem de apresentações vai ser: {lista}')