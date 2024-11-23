"""
um professo quer sortear um dos seus quatros alunos para
apagar o quadro. faça um programa que ajude ele,
lendo o nome dos alunos e escrevendo na tela o nome do escolhido
"""

import random

alunos = ('pedro', 'joao', 'maria', 'leonardo')
dec = random.choice(alunos)

print(f'o aluno escolhido foi {dec}')