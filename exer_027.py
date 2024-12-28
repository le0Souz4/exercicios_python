""" escreva um programa que faça o computador "pensar" em um
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
foi o número escolhido. O programa deverá escrever na tela se o
usuário venceu ou perdeu"""

# Importando a função randint da biblioteca random para gerar números aleatórios
from random import randint

# O usuário digita um número entre 0 e 5
num_user = int(input('Digite um número entre 0 e 5: '))

# A máquina escolhe aleatoriamente um número entre 0 e 5
num_pc = randint(0, 5)

# Exibindo o número escolhido pela máquina
print(f'O número escolhido pela máquina foi {num_pc}')

# Verificando se o número digitado pelo usuário é igual ao número gerado pela máquina
if num_user == num_pc:
    # Se o usuário acertar, exibe uma mensagem de sucesso
    print('Parabéns, você acertou!')
else:
    # Se o usuário errar, exibe uma mensagem de erro
    print('Perdeu, tente novamente!')
