"""
Crie um programa onde o usuário possa digitar cinco valores
numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort.()). No final mostre a lista
ordenada na tela
"""

# Inicializa a lista vazia para armazenar os números ordenados
numeros = []

# Cria um laço que será iterado 5 vezes
for i in range(5):
    valor = int(input(f"Digite o {i + 1}º número: "))

    # Verifica a posição correta para inserir o valor
    posicao = 0

    # este laço verifica as posições da lista para encontrar a posição correta
    while posicao < len(numeros): # a condição garante que o programa não acesse posições fora do tamanho
        if valor <= numeros[posicao]: # o numero digitado vai ser comparado com os que já estão na lista
            break
            # se o valor for menor ou igual ao número da posição atual, o laço será interrompido
            # pois a posição correta foi encontrada

        posicao += 1 # o indice é incrementado para verificar a proxima posição da lista
    numeros.insert(posicao, valor)  # Insere o número na posição correta
    print(f"Valor {valor} adicionado na posição {posicao}.")

# Exibe a lista ordenada
print("\nOs valores digitados, em ordem, são:")
print(numeros)
