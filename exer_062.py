"""Escreva um programa que leia um número N 
inteiro qualquer e mostre na tela os N primeiros 
elementos de uma Sequência de Fibonacci"""

# Solicita ao usuário o número de elementos que deseja exibir
n = int(input("Digite o número de elementos da Sequência de Fibonacci que você deseja ver: "))

# Inicializa os dois primeiros termos da sequência
t1 = 0  # Primeiro termo
t2 = 1  # Segundo termo

# Verifica se o número de elementos é válido
if n <= 0:
    print("Por favor, insira um número maior que zero.")
else:
    print(f"Sequência de Fibonacci com {n} termos:")
    print(t1, end=" -> ")  # Exibe o primeiro termo

    # Gera e exibe os demais termos da sequência
    contador = 1  # Contador de termos exibidos
    while contador < n:  # Executa até atingir o número de termos desejado
        print(t2, end=" -> ")  # Exibe o próximo termo
        t1, t2 = t2, t1 + t2  # Atualiza os termos: o próximo é a soma dos dois anteriores
        contador += 1  # Incrementa o contador

    print("FIM")  # Indica o final da sequência
