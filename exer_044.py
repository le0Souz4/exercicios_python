"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""

import random

# Opções do jogo
opcoes = ['pedra', 'papel', 'tesoura']

# Exibindo as opções para o jogador
print("Escolha uma opção:")
print("[1] Pedra")
print("[2] Papel")
print("[3] Tesoura")

# Entrada do usuário
escolha_usuario = int(input("Digite o número correspondente à sua escolha: "))

if escolha_usuario == 1:
    escolha_usuario = 'pedra'
elif escolha_usuario == 2:
    escolha_usuario = 'papel'
elif escolha_usuario == 3:
    escolha_usuario = 'tesoura'
else:
    print("Opção inválida, tente novamente.")
    exit()

# Escolha do computador
escolha_computador = random.choice(opcoes)

# Exibindo as escolhas
print(f"\nVocê escolheu: {escolha_usuario}")
print(f"O computador escolheu: {escolha_computador}")

# Verificando o vencedor
if escolha_usuario == escolha_computador:
    print("Empate!")
elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
     (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
     (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
    print("Você venceu!")
else:
    print("O computador venceu!")
