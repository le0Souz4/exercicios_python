'''
Crie um programa que leia o nome de uma cidade
diga se ela começa ou não com o nome "Santo"
'''

# Solicita ao usuário o nome de uma cidade e remove espaços extras nas extremidades
cid = input('Em que cidade você nasceu? ').strip().lower()

# Verifica se os primeiros 5 caracteres do nome da cidade correspondem a "santo"
print(cid[:5] == 'santo')
