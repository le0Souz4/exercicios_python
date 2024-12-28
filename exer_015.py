"""
Crie um programa que leia um número Real qualquer 
pelo teclado e mostre na tela a sua porção Inteira.
"""
import math  # Importa o módulo 'math', que fornece funções matemáticas avançadas.

# Solicita ao usuário que insira um número real (com casas decimais).
num = float(input("Por favor, digite um número real: "))

# Exibe a parte inteira do número fornecido, usando a função `math.trunc` para descartar a parte decimal.
# O `math.trunc` retorna o número sem arredondar, apenas removendo a parte fracionária.
print(f'A porção inteira de {num} é {math.trunc(num)}')
