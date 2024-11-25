""" escreva um programa que faça o computador "pensar" em um
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
foi o número escolhido. O programa deverá escrever na tela se o
usuário venceu ou perdeu"""
from random import randint

num_user = int(input('digite um número entre 0 e 5: '))
num_pc = randint(0, 5)
print(f'o numero escolhido pela máquina foi {num_pc}')
if num_user == num_pc:
    print('parabens, você acertou!')
else:
    print('perdeu, tente novamente!')


