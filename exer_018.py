"""
um professo quer sortear um dos seus quatros alunos para
apagar o quadro. faça um programa que ajude ele,
lendo o nome dos alunos e escrevendo na tela o nome do escolhido
"""
import random  # Importa o módulo 'random', usado para gerar escolhas ou números aleatórios.

# Define uma tupla com os nomes dos alunos.
alunos = ('pedro', 'joao', 'maria', 'leonardo')

# Usa a função 'random.choice()' para selecionar aleatoriamente um elemento da tupla 'alunos'.
dec = random.choice(alunos)

# Exibe o nome do aluno escolhido de forma formatada.
print(f'O aluno escolhido foi {dec}')
