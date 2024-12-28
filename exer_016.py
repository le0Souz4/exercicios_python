"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""
import math  # Importa o módulo 'math', que fornece funções matemáticas úteis.

# Solicita ao usuário que insira os comprimentos dos catetos.
cat_opo = float(input('Digite o comprimento do cateto oposto: '))
cat_adj = float(input('Agora digite o comprimento do cateto adjacente: '))

# Calcula a hipotenusa. 
# A linha comentada abaixo mostra uma abordagem manual para o cálculo, utilizando a fórmula do Teorema de Pitágoras:
# hipo = cat_opo**2 + cat_adj**2

# Utiliza a função `math.hypot()` para calcular diretamente a hipotenusa.
# `math.hypot(x, y)` é equivalente a calcular √(x² + y²), sendo mais eficiente e legível.
hipo = math.hypot(cat_opo, cat_adj)

# Exibe o resultado formatado com 2 casas decimais.
print(f'Por meio do Teorema de Pitágoras, o comprimento da hipotenusa será de {hipo:.2f}')
