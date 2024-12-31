"""
Crie um programa que leia números inteiros. o programa só vai parar
quando o usuário digitar o valor 999, que vai ser a condição de parada.
no final, mostre quantos números foram digitados e qual foi a soma entre elas
(desconsiderando o flag).
flag = indicador de parada
"""

# Alocação de variáveis: todas começam com o valor 0.
# 'num' vai armazenar o número inserido, 'cont_total' vai contar os números digitados
# e 'cont_soma' vai acumular a soma dos números digitados.
num = cont_total = cont_soma = 0

# Inicio de um loop infinito
while True:
    # Solicita ao usuário que digite um número
    n = int(input('Digite um número: '))
    
    # Verifica se o número digitado é 999, caso seja, o programa irá parar
    if n == 999:
        break  # Interrompe o loop se o número for 999
    
    # Se o número não for 999, aumenta o contador total de números digitados
    cont_total += 1

    # Soma o número digitado à variável 'cont_soma'
    cont_soma += n

# Após sair do loop, exibe o total de números digitados e a soma de todos eles
print(f'Você digitou {cont_total} números e a soma de todos os números foi {cont_soma}')
