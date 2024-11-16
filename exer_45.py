"""Faça um programa que mostre na tela uma
contagem regressiva para o estouro de fogos
de artificio, indo de 10 até 0, com um pausa de
1 segundo entre elas"""

import time

for c in range (10, -1, -1):
    print(c)
    time.sleep(1)
print("feliz ano novo, partiu aglomerar?")
