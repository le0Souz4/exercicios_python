"""
Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios. Guarde esses resultados em
um dicionário em Python. No final, coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from operator import itemgetter

resultados = {"jogador1": randint(1, 6),
    "jogador2": randint(1, 6),
    "jogador3": randint(1, 6),
    "jogador4": randint(1, 6)}

rank = ()
rank = sorted(resultados.items(), key=itemgetter(1), reverse= True)
print(f'=-'* 15)
for i, v in enumerate(rank):
    print(f"{i + 1}° lugar: {v[0]} com {v[1]}: ")
print("-=" * 15)