"""
faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados.
"""
# Solicita ao usuário que insira um número e trata-o como uma string
num = input('Digite um número de 0 a 9999: ')

# Exibe cada dígito separadamente, utilizando os índices da string.
print(f'O número {num} possui: '
      f'\n{num[3]} unidade(s)'  # O último dígito representa as unidades
      f'\n{num[2]} dezena(s)'   # O penúltimo dígito representa as dezenas
      f'\n{num[1]} centena(s) e'  # O terceiro dígito representa as centenas
      f'\n{num[0]} milhar(es)')  # O primeiro dígito representa os milhares

# Solicita ao usuário que insira um número e o converte para inteiro.
num2 = int(input('Digite outro Número: '))

# Calcula cada casa decimal utilizando divisões e o operador módulo.
u = num2 // 1 % 10  # Unidade: divide por 1 e obtém o resto da divisão por 10
d = num2 // 10 % 10  # Dezena: remove a unidade e obtém o resto por 10
c = num2 // 100 % 10  # Centena: remove as dezenas e obtém o resto por 10
m = num2 // 1000 % 10  # Milhar: remove as centenas e obtém o resto por 10

# Exibe o número e os valores calculados.
print(f'O número {num2} possui: '
      f'\n{u} unidade(s)'
      f'\n{d} dezena(s)'
      f'\n{c} centena(s) e'
      f'\n{m} milhar(es)')
