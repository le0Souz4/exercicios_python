"""
Faça um programa que leia 5 valores numéricos e
guarde-os em uma lista. no final mostre qual foi o maior e
o menor valor digitado e suas respectivas posições
na lista
"""

# Criando uma variável para alocar a lista que vai ser criada
numeros = list()

# fazendo um laço que irá ser feito 5 vezes alocando cada input em um indice da lista
for cont in range(0,5):
    numeros.append(int(input(f"por favor, digite o {cont + 1}° valor: ")))

# alocando os valores maximos e minimos em variáveis
maior = max(numeros)
menor = min(numeros)

# Criando laços para verificar qual a posição do maior valor
print(f'você digitou os seguintes numeros {numeros}')
print(f'o maior valor foi {maior}, na posição:', end=" ")
for i, v in enumerate(numeros):
    if v == maior:
        print(i, end="... ")

# Criando laços para verificar qual a posição do menor valor
print(f'\ne o menor valor digitado foi {menor} na posição:', end=" ")
for i, v in enumerate(numeros):
    if v == menor:
        print(i, end="... ")