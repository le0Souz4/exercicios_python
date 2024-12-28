'''
Faça um programa que leia uma frase pelo teclado
e mostre quantas vezes aparece a letra "A", em que posição ela
aparece a primeira vez e em que posição ela aparece a ultima vez
'''

# Solicita ao usuário que digite uma frase, removendo espaços desnecessários e convertendo tudo para minúsculas
frase = input('Por favor, digite uma frase: ').strip().lower()

# Conta quantas vezes a letra "a" aparece
qtd_a = frase.count('a')

# Encontra a posição da primeira ocorrência da letra "a"
primeira_pos = frase.find('a') + 1

# Encontra a posição da última ocorrência da letra "a"
ultima_pos = frase.rfind('a') + 1

# Exibe os resultados formatados
print(f'A letra "A" aparece {qtd_a} vezes;'
      f'\nEla aparece pela primeira vez na posição {primeira_pos}, e'
      f'\naparece por último na posição {ultima_pos}')
