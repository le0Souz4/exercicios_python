"""monte um programa que leia dois numeros inteiros
e compare-os, monstrando na tela as seguintes
mensagens:
-o primeiro valor é maior/menor
-o segundo valor é maior/menor
-os valores são iguais"""

# Solicita ao usuário o primeiro número inteiro
num_1 = int(input("Digite um número inteiro: "))

# Solicita ao usuário o segundo número inteiro
num_2 = int(input("Digite outro número inteiro: "))

# Compara os dois números e verifica qual é maior ou se são iguais
if num_1 > num_2:
    # Caso o primeiro número seja maior que o segundo
    print(f"O número {num_1} é maior que {num_2}")
elif num_2 > num_1:
    # Caso o segundo número seja maior que o primeiro
    print(f"O número {num_1} é menor que {num_2}")
else:
    # Caso os números sejam iguais
    print("Os números são iguais!")
