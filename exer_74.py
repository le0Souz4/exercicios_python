"""
desenvolva um programa que leia quatro valores
pelo teclado e guarde-os em uma tupla. no final mostre:
-> quantas vezes apareceu o valor 9;
-> em que posição foi digitado o primeiro valor 3;
-> quais foram os números pares
"""

# alocação dos numeros na tupla por meio de uma list comprehension
# lembrando do type casting certo para não dar erro mais pra frente
numeros = tuple(int(input('Digite um número: ')) for _ in range(4))
print(numeros)

# verifica se há e quantas vezes o número 9 apareceu por meio da função count()
print(f'o numero 9 apareceu {numeros.count(9)} vez(es)')

# verifica se há e em qual posição foi colocado o numero 3
# lembrando de colocar o +1 para bater com a base
if 3 in numeros:
    posica_3 = numeros.index(3) + 1
    print(f'o numero 3 foi digitado pela primeira vez na {posica_3}° posição')
else:
    print('o numero 3 não foi digitado')

# por meio de outra list comprehension verifico se há numeros pares dentro da tupla
# cria-se uma lista para alocar os pares vindos de numeros
pares = [par for par in numeros if par % 2 == 0]
if pares:
    print(f'os numeros pares digitados foram: {pares}')
else:
    print('nenhum numero par foi digitado')

