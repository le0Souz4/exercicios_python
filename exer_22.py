"""
faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados.
"""

# tratando o numero como string
num = input('Digite um número de 0 a 9999: ')
print(f'O número {num} possui: '
      f'\n{num[3]} unidade(s)'
      f'\n{num[2]} dezena(s)'
      f'\n{num[1]} centena(s) e'
      f'\n{num[0]} milhar(es)')

# tratando o número como int
num2 = int(input('Digite outro Número: '))
u = num2 // 1 % 10
d = num2 // 10 % 10
c = num2 // 100 % 10
m = num2 // 1000 % 10
print(f'O número {num} possui: '
      f'\n{u} unidade(s)'
      f'\n{d} dezena(s)'
      f'\n{c} centena(s) e'
      f'\n{m} milhar(es)')