"""
faça um programa que leia um angulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse angulo
"""
import math  # Importa o módulo 'math', que fornece funções matemáticas úteis.

# Solicita ao usuário que insira um ângulo em graus.
ang = float(input("Digite o valor do ângulo: "))

# Converte o ângulo de graus para radianos.
# A maioria das funções trigonométricas do módulo 'math' trabalha com ângulos em radianos.
rad = math.radians(ang)

# Calcula o seno do ângulo convertido em radianos.
sen = math.sin(rad)

# Calcula o cosseno do ângulo convertido em radianos.
cos = math.cos(rad)

# Calcula a tangente do ângulo convertido em radianos.
tng = math.tan(rad)

# Exibe os valores calculados, formatados com 3 casas decimais.
print(f'O ângulo digitado possui os seguintes valores:'
      f'\nseno: {sen:.3f}'  # Exibe o seno formatado.
      f'\ncosseno: {cos:.3f}'  # Exibe o cosseno formatado.
      f'\ntangente: {tng:.3f}')  # Exibe a tangente formatada.
