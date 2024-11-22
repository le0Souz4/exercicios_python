"""
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequencia. No final, mostre uma listagem de
preços, organizando os dados em forma tabular.
"""

# criando um cabeçalho
print('-' * 35)
print(f'{"PAPELARIA DO CENTRO":^35}') # formatando a string para que fique centralizada em um espaço com 35 caracteres
print('-' * 35)

# criação da tupla com os produtos e preços
produtos = ('lapis', 1.00,
            'caneta', 2.00,
            'borracha', 0.50,
            'caderno', 18.50,
            'estojo', 5.50)

# criando uma lista que pega as posições dos produtos
for posicao in range(0, len(produtos)):

    # pegando apenas o nome dos produtos
    # os nomes ocupam índices pares
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<30}', end="") # centralizando os nomes à esquerda em 30 caracteres, ocupando os em branco com pontos

    # já os preços ocupam índices impares
    else:
        print(f'R${produtos[posicao]:>5.2f}') # centralizando à direita

print('-' * 35)