"""
Crie um programa que leia números inteiros. o programa só vai parar
quando o usuário digitar o valor 999, que vai ser a condição de parada.
no final, mostre quantos números foram digitados e qual foi a soma entre elas
(desconsiderando o flag).
flag = indicador de parada
"""

# Alocação dinâmica onde todas as variáveis começam nulas
num = cont_total = cont_soma = 0

# Inicio do loop infinito
while True:
    n = int(input('digite um número: '))
    # Flag que indica o fim
    if n == 999:
        break
    # conta quantos números foram escritos
    cont_total += 1

    # soma o total dos números digitados
    cont_soma += n

print(f'você digitou {cont_total} números e a soma de todos os números foi {cont_soma}')

"""
edit1: tentei declarar os valores iniciais como None, mas deu problema quando foi necessário o usuário colocar o input 
"""

"""
edit2: de acordo com o Copilot, declarar as variáveis dessa forma num = cont_total = cont_soma = 0, é uma prática pouco usual
e pode atrapalhar tanto a mim quanto a outros programadores
"""