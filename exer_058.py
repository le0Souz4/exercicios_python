""" crie um programa que leia dois valores e mostre
um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
"""

# Solicita ao usuário dois números inteiros iniciais
num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))

# Inicializa a variável que será usada para a decisão no menu
dec = 0

# Laço de repetição que se mantém ativo até o usuário optar por sair do programa (opção 5)
while dec != 5:
    # Exibe o menu de opções
    print("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    """)

    # Solicita que o usuário escolha uma das opções do menu
    dec = int(input("Escolha uma opção: "))

    # Verifica qual opção foi escolhida
    if dec == 1:  # Caso a opção seja SOMAR
        print(f"A soma entre {num_1} e {num_2} é {num_1 + num_2}.")
    elif dec == 2:  # Caso a opção seja MULTIPLICAR
        print(f"A multiplicação entre {num_1} e {num_2} é {num_1 * num_2}.")
    elif dec == 3:  # Caso a opção seja MAIOR
        if num_1 > num_2:  # Verifica qual dos números é maior
            print(f"O maior número é {num_1}.")
        elif num_2 > num_1:
            print(f"O maior número é {num_2}.")
        else:  # Caso os números sejam iguais
            print("Os números são iguais.")
    elif dec == 4:  # Caso a opção seja NOVOS NÚMEROS
        # Solicita ao usuário dois novos números
        num_1 = int(input("Digite o novo primeiro número: "))
        num_2 = int(input("Digite o novo segundo número: "))
    elif dec == 5:  # Caso a opção seja SAIR
        # Exibe mensagem e encerra o laço
        print("Saindo do programa...")
        break
    else:  # Caso o usuário insira uma opção inválida
        print("Por favor, escolha uma opção válida!")

# Exibe mensagem final ao término do programa
print("Fim do programa.")
