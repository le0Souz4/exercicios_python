"""
Crie um módulo chamado moeda.py que tenha as
funções incorporadas aumentar(), diminuir(), dobro() e
metade(). Faça também um programa que importe esse módulo
e use algumas dessas funções.
"""

import moeda

numero = float(input('digite um número:'))
dec = input('deseja calcular porcentagem? ').strip().upper()[0]
if dec == 'S':
    porcentagem = int(input('digite a porcentagem: '))

resp1 = moeda.aumentar(numero, porcentagem)
resp2 = moeda.diminuir(numero, porcentagem)
resp3 = moeda.dobro(numero)
resp4 = moeda.metade(numero)

print(f'aumentando fica: {resp1}\n'
      f'diminuindo fica: {resp2}\n'
      f'dobrando fica: {resp3}, e\n'
      f'dividindo pela metade fica: {resp4}')