"""Faça um programa que calcule a soma entre todos os
número impares que são multiplos de tres e
que se encontram no intervalo de 1 até 500"""

# Inicializo as variáveis para controlar a soma e a contagem
soma = 0  # A variável soma começa com valor 0. Ela será usada para armazenar a soma dos números divisíveis por 3.
contador = 0  # A variável contador começa com valor 0. Ela contará quantos números satisfazem as condições do programa.

# O laço 'for' irá percorrer uma sequência de números. O range(1, 500, 2) começa em 1, vai até 499 (não incluindo o 500),
# e percorre apenas números ímpares, pois o passo de 2 faz isso.
for count in range(1, 500, 2):
    # Verifico se o número atual (count) é divisível por 3. O operador '%' retorna o resto da divisão.
    # Se o resto for 0, significa que o número é divisível por 3.
    if count % 3 == 0:  
        # Se o número for divisível por 3, ele será somado à variável 'soma'.
        soma += count  # Soma o valor de 'count' à variável 'soma'.
        
        # A variável contador é incrementada para contar quantos números divisíveis por 3 foram encontrados.
        contador += 1  # Incrementa o contador em 1 a cada número divisível por 3 encontrado.

        # O 'print(count, end=' ')' imprime os números divisíveis por 3 na mesma linha, separados por espaços.
        print(count, end=' ')  # Mostra o número 'count' na tela.

# Após o laço, o programa imprime a quantidade de números divisíveis por 3 que foram encontrados e somados.
print(f"\nSão {contador} valores no total")  # Exibe quantos números divisíveis por 3 foram encontrados.
print("A soma de todos os numeros é:", soma)  # Exibe a soma de todos os números divisíveis por 3.
