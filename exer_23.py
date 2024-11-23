'''
Crie um programa que leia o nome de uma cidade
diga se ela começa ou não com o nome "Santo"
'''

cid = input('Em que cidade você nasceu? ').strip().lower()
print(cid[:5] == 'santo')