"""
crie um programa que tenha uma tupla com várias palavras.
depois disso, você devemostrar, para cada palavra,
quais são suas vogais
"""

# criando uma tupla com algumas palavras
palavras = ('amigo', 'viajar', 'aprendizado', 'programação', 'futuro')

# fazendo as palavras da tupla serem mostradas em caixa alta
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end="")

    # este laço procurar em cada letra (índice) de cada palavra (lista)
    # se faz parte da lista de vogais 'aeiou'
    for letra in p:
        if letra in 'aeiou':
         print(letra, end=" ")

'''
edit1: o pulo do gato aqui é ter em mente que cada palavra dentro da tupla
é uma lista por si só
'''