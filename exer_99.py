"""
Faça um programa que tenha uma lista chamada
números e duas funções chamadas sorteia() e
somaPar(). A primeira função vai sortear 5 números
e vai colocá-los dentro da lista e a segunda
função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior.
"""

from random import randint

numeros = list()

def sorteia():
    while len(numeros) < 5:
        numeros.append(randint(1,10))
    print(numeros)

def soma_par():
    soma = 0
    for i in numeros:
        if i % 2 == 0:
           soma += i
    print(soma)


sorteia()
soma_par()

