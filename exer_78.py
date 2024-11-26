"""
Crie um programa onde cada usuário possa digitar vários valores
numéricos e cadastre-os em uma lista.
caso o número já exista lá dentro, ele não será adicionado.
No final, seráo exibidos todos os valores únicos digitados,
em ordem crescente.
"""

# criando uma variável para armazenar a lista e um contador
valores = list()
cont = 1

# criando um laço infinito que irá pedir os valores do usuário
while True:
    valor = int(input(f"por favor, digite o {cont}° valor: "))

    # laço condicional que verifica se o valor já foi digitado
    if valor in valores:
        print("valor já digitado")
    else:
        valores.append(valor)
        cont += 1

    # laço que verifica se o usuário quer continuar
    dec = input('deseja continuar? [S] // [N] \n').strip().upper()
    if dec == 'N':
     break

# Ordena a lista
valores.sort()
print("Os valores únicos e em ordem crescente são:"
      f"\n{valores}")