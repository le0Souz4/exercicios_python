"""
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual
deles é o maior.
"""

def maior(*num):
    cont = maior = 0  # Inicializa o contador e a variável que armazenará o maior valor
    print('Analisando...')  # Informa que o processo de análise dos números está começando

    # Itera sobre todos os valores passados como argumento para a função
    for valor in num:
        print(f'{valor} ', end='')  # Exibe cada número passado como parâmetro
        if cont == 0:
            maior = valor  # Inicializa o maior valor com o primeiro valor da lista
        else:
            if valor > maior:
                maior = valor  # Atualiza o maior valor, se o valor atual for maior

        cont += 1  # Incrementa o contador

    # Exibe o número total de valores analisados
    print(f"\nForam informados {cont} valores.")
    # Exibe o maior valor informado
    print(f"O maior valor digitado foi {maior}.")


# Testando a função com uma sequência de números
maior(1, 2, 3, 4, 5, 6)
# Chamando a função sem passar nenhum número
maior()
