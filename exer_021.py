"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.
"""
# Solicita ao usuário que insira seu nome completo e remove espaços extras no início e no fim com o método .strip().
nome = input("Digite seu nome completo: ").strip()

# Converte o nome para maiúsculas e armazena na variável 'nome_up'.
nome_up = nome.upper()

# Converte o nome para minúsculas e armazena na variável 'nome_low'.
nome_low = nome.lower()

# Calcula o total de letras do nome, subtraindo os espaços (utilizando .count(' ') para contar os espaços).
nome_letras = len(nome) - nome.count(' ')

# Encontra o índice do primeiro espaço, que indica o tamanho do primeiro nome.
prim_nome = nome.find(' ')

# Exibe os resultados formatados.
print(f'Seu nome em maiúsculas fica {nome_up},'
      f'\nSeu nome em minúsculas fica {nome_low}'
      f'\nSeu nome ao todo tem {nome_letras} letras,'
      f'\nE seu primeiro nome tem {prim_nome} letras')
