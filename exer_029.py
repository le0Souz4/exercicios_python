'''
Crie um programa que leia um número inteiro e mostre
na tela se ele é PAR ou IMPAR
'''

# Solicita ao usuário que digite um número inteiro
num = int(input("Por favor, digite um número: "))

# Verifica se o número é par
if num % 2 == 0:
    # Se o número for par (resto da divisão por 2 é 0), exibe a mensagem informando que é par
    print(f'O número {num} é par')
else:
    # Caso contrário (resto da divisão por 2 é diferente de 0), exibe a mensagem informando que é ímpar
    print(f'O número {num} é ímpar')
