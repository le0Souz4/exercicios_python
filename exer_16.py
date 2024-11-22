"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""

import math

cat_opo = float(input('digite o comprimento do cateto oposto: '))
cat_adj = float(input('agora digite o comprimento do cateto adjacente: '))

# este seria o jeito mais dificil de se fazer
# hipo = cat_opo**2 + cat_adj**2

hipo = math.hypot(cat_opo, cat_adj)

print(f'por meio do teorema de pitágoras, o comprimento da hipotenusa será de {hipo:.2f}')
