"""Crie um programa que leia vários números inteiros pelo 
teclado. O programa só vai parar quando o usuário digitar 
o valor 999, que é a condição de parada. No final, mostre 
quantos números foram digitados e qual foi a soma entre eles 
(desconsiderando o flag)."""

# Inicializa as variáveis de controle
soma = 0  # Armazena a soma dos números digitados
contador = 0  # Conta quantos números foram digitados

# Loop infinito que será controlado pela condição de parada
while True:
    num = int(input("Digite um número inteiro (999 para parar): "))  # Solicita um número ao usuário

    # Verifica se o número digitado é o valor de parada (flag)
    if num == 999:
        break  # Sai do laço se a condição de parada for atendida

    soma += num  # Adiciona o número digitado à soma
    contador += 1  # Incrementa o contador

# Exibe os resultados finais
print(f"\nVocê digitou {contador} números.")
print(f"A soma dos números digitados é {soma}.")
