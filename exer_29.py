'''
Crie um programa que leia um número inteiro e mostre
na tela se ele é PAR ou IMPAR
'''

num = int(input("por favor, digite um número: "))
if num % 2 == 0:
    print(f'o número {num} é par')
else:
    print(f'o número {num} é impar')