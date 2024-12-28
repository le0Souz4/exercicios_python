'''
Crie um programa que leia o nome de uma pessoa e diga se ela
tem 'silva' no nome
'''

# Solicita ao usuário que insira o nome
nome = input('Por favor, digite seu nome: ').lower()

# Verifica se a string "silva" está presente no nome digitado (independente da posição)
print('silva' in nome)
