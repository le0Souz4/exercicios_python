"""
Faça um programa que jogue par ou impar com o computador.
o jogo só será interrompido quando o jogador perder, mostrando o total
de vitórias consecutivas que ele conquistou no final do jogo
"""

import random  # Importa o módulo random para gerar números aleatórios

# Inicializa o contador de vitórias
cont = 0

while True:  # Loop principal do jogo que continuará enquanto o jogador acertar

    # Solicita ao usuário que escolha entre Par ou Ímpar
    dec_user = input("Escolha Par ou Ímpar (P/I): ").strip().lower()[0]  # Remove espaços extras e converte para minúsculas, pegando apenas a primeira letra

    # Valida a entrada do usuário, garantindo que seja uma escolha válida (P ou I)
    if dec_user not in ['p', 'i']:
        dec_user = input("Entrada inválida! Escolha Par ou Ímpar (P/I): ").strip().lower()  # Repetir a solicitação até que a escolha seja válida

    # Solicita ao usuário que digite um número inteiro
    num_user = int(input("Digite um número: "))

    # O computador escolhe um número aleatório entre 1 e 10
    num_pc = random.randint(1, 10)

    # Soma os números do usuário e do computador
    soma = num_user + num_pc

    # Determina se a soma é par ou ímpar. Se o resto da divisão por 2 for 0, é par, caso contrário, é ímpar
    resultado = 'p' if soma % 2 == 0 else 'i'

    # Verifica se o jogador acertou o resultado (se o jogador escolheu corretamente entre Par ou Ímpar)
    if resultado == dec_user:
        cont += 1  # Se o jogador acertou, aumenta o contador de vitórias
        print(f"Você escolheu {num_user} e o computador escolheu {num_pc}. A soma é {soma}. Você ganhou!")
        print('Vamos jogar novamente!')
    else:
        # Caso o jogador erre, o jogo termina
        print(f"Você escolheu {num_user} e o computador escolheu {num_pc}. A soma é {soma}. Você perdeu!")
        break  # Encerra o loop se o jogador perder

# Exibe o total de vitórias consecutivas que o jogador teve
print(f"Você venceu {cont} vezes consecutivas.")
