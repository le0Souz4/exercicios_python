"""
Crie um programa que gerencie o aproveitamento de um jogador de
futebol, o programa vai ler a quantidade de gols feitos em cada
partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato
"""

campeonato = dict()
campeonato['nome'] = input('digite o nome do jogador: ')
campeonato['partidas_jogadas'] = int(input(f'quantas partidas {campeonato['nome']} jogou? \nR:'))
partidas = list()
for jogo in range(campeonato['partidas_jogadas']):
    gols_partida = int(input(f'quantos gols {campeonato['nome']} fez no {jogo + 1}° jogo? '))
    partidas.append(gols_partida)
total_gols = sum(partidas)
campeonato['total_campeonato'] = total_gols
print(f'o jogador {campeonato['nome']} jogou {campeonato['partidas_jogadas']}'
      f' partidas \ne fez um total de {campeonato['total_campeonato']} gols no campeonato')
for i, v in enumerate(partidas):
    print(f'no {i + 1}° jogo ele fez {v} gols')