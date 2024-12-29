"""
Faça um programa que leia três números e
 mostre qual é o maior e qual é o menor.
"""

# Solicita ao usuário que digite três números inteiros
num1 = int(input("Digite o primeiro número: \n"))
num2 = int(input("Digite o segundo número: \n"))
num3 = int(input("Digite o terceiro número: \n"))

# Inicialmente, assume-se que o menor número é o primeiro
menor = num1

# Verifica se o segundo número é menor do que os outros dois
if num2 < num1 and num2 < num3:
    menor = num2

# Verifica se o terceiro número é menor do que os outros dois
if num3 < num1 and num3 < num2:
    menor = num3

# Exibe os resultados
print(f"O menor valor foi {menor}")
print(f"E o maior valor foi {maior}")
