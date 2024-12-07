"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

import math

# iniciando uma matriz 3x3 com todos os valores zerados
matriz= [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # lembrando que a primeira linha equivale ao indice 0, a segunda ao 1 e a terceira ao 2

# preenchendo a matriz
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))

# exibindo a matriz formatada
print('aqui está sua matriz 3x3: ')
for linha in matriz:
    for num in linha:
        print(f'{num:^5}', end='') # formantado a linha com espaçamento de 5 unidades
    print() # quebra de linha

# somando os valores pares
pares = []
for linha in matriz:
    for valor in linha: # aqui o laço vai iterando em todas as linhas procurando valores pares
        if valor % 2 == 0:
            pares.append(valor) # adiciono o valor a lista de pares
print(f'A soma dos valores pares equivale a {sum(pares)}')

# somando os valores da terceira coluna
coluna3 = []
for linha in matriz:
    coluna3.append(linha[2]) # pegando os valores da 3° coluna que equivale à lista de indice 2
print(f'A soma dos valores da 3° coluna equivalem a {sum(coluna3)}')

# pegando o maior valor da segunda linha
maior2 = max(matriz[1])
print(f'O maior valor da segunda linha é {maior2}')

"""
l.e: --> foi criada uma matriz 3x3 com valores vazios (l: 11);
    --> em seguida foi feita uma função para preencher os valores (l: 14);
    --> mostro a matriz formatada (l: 18);
    --> então crio uma lista para alocar os valores pares da matriz (f: 26) e somo 
        os valores por meio da função .sum() (l: 31);
    --> crio outra lista para alocar os valores da 3 coluna (l: 34) que vou obtendo
        por meio do laço for (l: 35)
    --> então uso a função max() para pegar o maior valor da segunda linha (l: 40)
"""
