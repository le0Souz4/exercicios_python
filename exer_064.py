"""Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual 
foi o maior e o menor valores lidos. O programa deve perguntar ao 
usuário se ele quer ou não continuar a digitar valores."""

# Inicializa as variáveis de controle
soma = 0  # Para acumular a soma dos números
contador = 0  # Para contar quantos números foram digitados
continuar = 's'  # Controla a repetição do laço
maior = None  # Armazena o maior número, inicialmente indefinido
menor = None  # Armazena o menor número, inicialmente indefinido

# Início do laço que continua enquanto o usuário quiser
while continuar in 'sS':  # Aceita 's' ou 'S' como resposta para continuar
    num = int(input("Digite um número inteiro: "))  # Solicita um número ao usuário
    
    # Atualiza a soma e o contador
    soma += num
    contador += 1

    # Atualiza os valores do maior e menor número
    if maior is None or num > maior:  # Se for o primeiro número ou maior que o atual maior
        maior = num
    if menor is None or num < menor:  # Se for o primeiro número ou menor que o atual menor
        menor = num

    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja continuar? [S/N]: ").strip().lower()

# Após o laço, verifica se houve entrada de números
if contador > 0:
    media = soma / contador  # Calcula a média dos números digitados

    # Exibe os resultados
    print(f"\nVocê digitou {contador} números.")
    print(f"A média entre os valores é {media:.2f}.")
    print(f"O maior valor digitado foi {maior}.")
    print(f"O menor valor digitado foi {menor}.")
else:
    print("\nNenhum número foi digitado.")
