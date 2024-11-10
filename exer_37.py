"""monte um programa que leia dois numeros inteiros
e compare-os, monstrando na tela as seguintes
mensagens:
-o primeiro valor é maior/menor
-o segundo valor é maior/menor
-os valores são iguais"""
num_1 = int(input("Digite um numero inteiro: "))
num_2 = int(input("Digite outro numero inteiro: "))
if num_1 > num_2:
    print(f"o numero {num_1} é maior que {num_2}")
elif num_2 > num_1:
    print(f"o numero {num_1} é menor que {num_2}")
else:
    print("os numeros são iguais!")

