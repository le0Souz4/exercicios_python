"""
 Faça um programa que leia um número 
 inteiro e diga se ele é ou não um número primo.
 """

# Solicita ao usuário que insira um número inteiro.
numero = int(input("Digite um número inteiro para verificar se é primo: "))

# Inicializa um contador para contar quantas vezes o número é divisível.
divisores = 0

# Laço para verificar todos os números de 1 até o número informado.
for i in range(1, numero + 1):
    if numero % i == 0:  # Verifica se o número é divisível por i.
        divisores += 1  # Incrementa o contador de divisores.
        print(f"\033[32m{i}\033[m", end=" ")  # Exibe os divisores em verde.
    else:
        print(f"\033[31m{i}\033[m", end=" ")  # Exibe os não divisores em vermelho.

# Após o laço, verifica se o número é primo com base na quantidade de divisores.
print(f"\nO número {numero} foi divisível {divisores} vezes.")

if divisores == 2:  # Um número primo tem exatamente 2 divisores: 1 e ele mesmo.
    print("Por isso, ele é um número primo.")
else:
    print("Por isso, ele NÃO é um número primo.")

