""" crie um programa que leia dois valores e mostre
um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
"""
num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
dec = 0

# Aqui estabeleço que o loop será infinito
# De acordo com o Copilot esse inicio poderia ser escrito de outra forma "while true"
# O que tiraria a necessidade de daclarar a variável dec acima
while dec != 5:
    print("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    """)

    dec = int(input("Escolha uma opção: "))

    if dec == 1:
            print(f"A soma entre {num_1} e {num_2} é {num_1 + num_2}.")
    elif dec == 2:
            print(f"A multiplicação entre {num_1} e {num_2} é {num_1 * num_2}.")
    elif dec == 3:
        if num_1 > num_2:
                print(f"O maior número é {num_1}.")
        elif num_2 > num_1:
                print(f"O maior número é {num_2}.")
        else:
                print("Os números são iguais.")
    elif dec == 4:
            num_1 = int(input("Digite o novo primeiro número: "))
            num_2 = int(input("Digite o novo segundo número: "))
    elif dec == 5:
            print("Saindo do programa...")
            break
    else:
            print("Por favor, escolha uma opção válida!")

print("Fim do programa.")

"""
tive uma certa dificuldade com relação a quarta opção,
não consegui pensar em nada que se encaixasse nessa situação
para que fizesse o sistema voltar do inicio
"""

"""
edit1: percebi que colocar a alocação da variável DEC dentro do loop faz total diferença
"""