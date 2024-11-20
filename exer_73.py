"""
Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla. Depois disso, mostre a listagem de números gerados
 e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

# geração de uma tupla com numeros aleatorios usando uma tuple comprehension
# o _ funciona como uma entrada nula, já que o valor não importa
numeros = tuple(randint(1, 100) for _ in range(5))

# mostra os números gerados
print(f"Números gerados: {numeros}")

# verifica qual o menor e o maior
menor = min(numeros)
maior = max(numeros)

# exibe os números
print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")