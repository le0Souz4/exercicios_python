"""
Crie um programa que declare uma matriz de dimensões 3x3
e preencha com valores lidos pelo teclado. no final, mostre
a matriz na tela, com a formatação correta.
"""

# Inicializando a matriz como uma lista de listas vazias
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Preenchendo a matriz com valores inseridos pelo usuário
for linha in range(3):  # Itera pelas 3 linhas
    for coluna in range(3):  # Itera pelas 3 colunas
        matriz[linha][coluna] = int(input(f"Digite um valor para a posição [{linha}, {coluna}]: "))

# Exibindo a matriz formatada
print("\nMatriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"{valor:^5}", end=" ")  # Formatação centralizada em 5 espaços
    print()  # Quebra de linha ao final de cada linha da matriz

"""
l.e: --> crio uma lista do tipo matriz 3x3, ou seja, 3 linhas e 3 colunas (l: 8);
    --> para preencher a matriz uso dois laços for (l: 11, 12), um aninhado no outro, onde um
        vai fazer a iteração das linhas e outro das colunas (l: 13)
    --> no retorno, para a formatação da matriz foi usado outro laço for aninhado (l: 17, 18),
        onde são formadas as linhas, uma embaixo da outra com 5 espaçamentos (l: 19)
"""