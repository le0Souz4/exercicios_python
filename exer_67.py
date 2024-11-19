"""
Faça um programa que jogue par ou impar com o computador.
o jogo só será interrompido quando o jogador perder, mostrando o total
de vitórias consecutivas que ele conquistou no final do jogo
"""
import random

#variável isolada
cont = 0

while True:

    # variável alocada dentro do laço
    dec_user = input("Escolha Par ou Ímpar (P/I): ").strip().lower()[0] # Peço pro usuário escolher, aproveito para usar as funções para tirar espaços e deixar minusculo

    # De acordo com o Copilot, aqui deveria ser inserido outro laço while, mas não vi
    # necessidade então mudei para a condicional if (não houve nenhuma mudança significativa)
    if dec_user not in ['p', 'i']:
        dec_user = input("Entrada inválida! Escolha Par ou Ímpar (P/I): ").strip().lower() # Se a entrada não condizer com as opções, aparece o aviso e o laço recomeça

    num_user = int(input("Digite um número: ")) # número do usuário

    num_pc = random.randint(1, 10) # Número do computador, usando o módulo aleatório

    soma = num_user + num_pc # Soma o numero do usuário e do computador

    resultado = 'p' if soma % 2 == 0 else 'i' # Verifica se o resultado é par

    # Verifica se o jogador acertou
    if resultado == dec_user:
        cont += 1  # Jogador venceu então aumenta o contador de vitórias
        print(f"Você escolheu {num_user} e o computador escolheu {num_pc}. A soma é {soma}. Você ganhou!")
        print('Vamos jogar novamente!')
    else:
        # Jogador errou então o jogo termina
        print(f"Você escolheu {num_user} e o computador escolheu {num_pc}. A soma é {soma}. Você perdeu!")
        break

# Exibe o total de vitórias consecutivas
print(f"Você venceu {cont} vezes consecutivas.")

"""
edit1: surgiram muitas duvidas acerca da alocação de variáveis, 
se era necessaário colocar antes ou depois do laço.
de acordo com o Copilot, isolar as variáveis é vantajoso quando o valor
das variáveis precisa ser preservado;
agora, se a cada iteração, o valor da variável for refeito, não há necessidade
em isola-lo, podendo coloca-lo diretamente no laço.
"""