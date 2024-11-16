"""Faça um programa que calcule a soma entre todos os
número impares que são multiplos de tres e
que se encontram no intervalo de 1 até 500"""

soma = 0 # Inicializo a variável soma com valor nulo que será preenchido depois
contador = 0 # Inicia com 0 que será preenchido depois

for count in range(1, 500, 2): #começo a partir do 1 e vou até 499 indo de impar em impar
    if count % 3 == 0: # (se o número dentro da range tiver o resto da divisão 0 ele será mostrado
        soma += count # Registra todos os números dentro da variavel soma
        contador += 1 # Registra todos os números dentro da variavel contador
        print(count, end=' ') # Mostra todos os números divisiveis por 3
print(f"\nSão {contador} valores no total")
print("A soma de todos os numeros é:",soma)