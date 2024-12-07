"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.
"""
import random
import time

# Entrada do usuário
quantos_jogos = int(input('Quantos jogos você quer gerar? '))

# Lista principal que armazenar todos os jogos
todos_os_jogos = []

# Gerando os jogos
for _ in range(quantos_jogos): # Loop for que faz a quantidade de iterações de acordo com o valor digitado
    numeros_do_jogo = [] # Lista secundária que armazena os valores dos jogos individuais
    while len(numeros_do_jogo) < 6:
        valor = random.randint(1, 60) # enquanto a quantidade de valores dentro da lista for menor que 6 vai continuar colocando
        if valor not in numeros_do_jogo:
            numeros_do_jogo.append(valor) # se o valor já estiver na lista, ele não será inserido
    numeros_do_jogo.sort()  # Ordena os números do jogo
    todos_os_jogos.append(numeros_do_jogo) # quando a lista secundária estiver completa, é inserida na lista principal

# Exibindo os jogos
print(f"\nForam gerados {quantos_jogos} jogos:")
for i, jogo in enumerate(todos_os_jogos, start=1):
    print(f"Jogo {i}: {jogo}")
    time.sleep(1)


