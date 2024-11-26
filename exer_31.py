'''
Faça um programa que leia um ano qualquer e mostre se ele
é bissexto
'''

ano = int(input('por favor, insira o ano a ser analisado: \nR: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto')
else:
    print(f'o ano {ano} não é bissexto')