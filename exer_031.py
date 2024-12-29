'''
Faça um programa que leia um ano qualquer e mostre se ele
é bissexto
'''

# Solicita ao usuário que insira o ano a ser analisado e o converte para um número inteiro
ano = int(input('Por favor, insira o ano a ser analisado: \nR: '))

# Verifica se o ano é bissexto usando as condições:
# 1. Deve ser divisível por 4 e não divisível por 100, OU
# 2. Deve ser divisível por 400
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    # Se a condição acima for verdadeira, o ano é bissexto
    print(f'O ano {ano} é bissexto')
else:
    # Caso contrário, o ano não é bissexto
    print(f'O ano {ano} não é bissexto')
