"""
Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha separados
os valores pares e ímpares. No final, mostre os valores pares e ímpares
em ordem crescente.
"""

# esse é o código que eu fiz mas que no final acabei quebrando a exigencia
# de mantes apenas uma lista
numeros = list()

for c in range(1,8):
    numeros.append(int(input(f'Por favor insira o {c + 1}° número: \nR: ')))

pares = [p for p in numeros if p % 2 == 0]
impares = [p for p in numeros if p % 2 != 0]

pares.sort()
impares.sort()

print(f"os numeros digitados foram: {numeros}"
      f"\nos números pares foram {pares}"
      f"\ne os números ímpares foram {impares}")
#
#
#
#
#
#
# o código certo, que vai de encontro com o enunciado é o seguinte:
numeros = [[], []]

# Loop para entrada dos 7 valores numéricos
for _ in range(7):  # Iteramos 7 vezes
    valor = int(input("Digite um valor numérico: \nR: "))
    # Adicionamos o valor à sublista de pares ou ímpares conforme sua condição
    if valor % 2 == 0:
        numeros[0].append(valor)  # Sublista [0] para pares
    else:
        numeros[1].append(valor)  # Sublista [1] para ímpares

# Ordenamos as sublistas
numeros[0].sort()  # Ordena os pares
numeros[1].sort()  # Ordena os ímpares

# Exibimos os resultados
print(f"Os valores pares digitados foram: {numeros[0]}")
print(f"Os valores ímpares digitados foram: {numeros[1]}")

"""
l.e: --> criada uma lista que já possuia 2 sublistas vazias (l: 31);
    --> em seguida é criado um laço for que será iterado 7 vezes (l: 34);
    --> é alocado o valor do input em uma variável valor (l: 35) e logo em
    seguida é criado um laço condicional que irá alocar corretamente os inputs, 
    sendo os valores pares (l: 38) alocados no indice [0], e os valores impares no
    indice [1](l: 40);
    --> a sublistas são ordenadas com a função .sort() (l: 43, 44), lembrando que numeros[0] 
    representa os numeros pares, e numeros[1] os números impares;
    --> os valores são mostrados (l: 47, 48)
"""