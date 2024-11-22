"""
faça um programa que leia um angulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse angulo
"""

import math

ang = float(input(" digite o valor do angulo: "))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tng = math.tan(rad)

print(f'O ângulo digitado possui os seguintes valores:'
      f'\nseno: {sen:.3f}'
      f'\ncosseno: {cos:.3f}'
      f'\ntangente: {tng:.3f}')