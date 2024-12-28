"""
o mesmo professor do exer_18 quer sortear a ordem de apresentação
de trabalhos dos alunos. Faça um programa que leia o nome
dos quatro alunos e mostre a ordem sorteada
"""
import random  # Importa o módulo 'random', utilizado para operações aleatórias.

# Solicita o nome de quatro alunos ao usuário.
aluno1 = input("Digite o nome do 1° aluno: ")
aluno2 = input("Digite o nome do 2° aluno: ")
aluno3 = input("Digite o nome do 3° aluno: ")
aluno4 = input("Digite o nome do 4° aluno: ")

# Cria uma lista contendo os nomes fornecidos.
lista = [aluno1, aluno2, aluno3, aluno4]

# Usa a função 'random.shuffle()' para embaralhar os elementos da lista de forma aleatória.
random.shuffle(lista)

# Exibe a ordem aleatória dos alunos em uma mensagem formatada.
print(f'A ordem de apresentações vai ser: {lista}')
