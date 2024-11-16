"""desenvolva um programa que leia seis numeros
inteiros e mostre a soma apenas daqueles que forem
pares, se o valor digitado for impar, desconsidere-o"""

soma_par = 0 # Inicializo a variável soma com valor nulo que será preenchido depois
soma_imp = 0 # Inicializo a variável soma com valor nulo que será preenchido depois

for count in range(1,7):
    numero = int(input(f'Digite o {count}° numero: ')) # O programa irá solicitar um número 6x
    if numero % 2 == 0:
        soma_par += numero # Se o número for par entra nesse laço
    elif numero % 2 != 0:
        soma_imp += numero # Se impar, nesse
print("A soma de todos os numeros PARES é:", soma_par)
print("A soma de todos os numeros IMPARES é:", soma_imp)

