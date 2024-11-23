"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.
"""

nome = input("Digite seu nome completo: ").strip()
nome_up = nome.upper()
nome_low = nome.lower()
nome_letras = len(nome) - nome.count(' ')
prim_nome = nome.find(' ')
print(f'Seu nome em maiúsculas fica {nome_up},'
      f'\nSeu nome em minúsculas fica {nome_low}'
      f'\nSeu nome ao todo tem {nome_letras} letras,'
      f'\nE seu primeiro nome tem {prim_nome} letras')

