"""
faça um programa que leia um número qualquer e mostre seu fatorial
fatorial -> n! = n x (n-1) x ... x 1
"""

# Solicita ao usuário que digite um número
num = int(input("Digite um número: "))

# Verifica se o número é negativo, já que não existe fatorial para números negativos
if num < 0:
    print("Não existe fatorial para números negativos.")
else:
    # Inicializa as variáveis:
    # - `fatorial` será usada para armazenar o resultado do cálculo, iniciando com 1 (neutro multiplicativo)
    # - `contador` começa com o valor de `num` e será decrementado durante o cálculo
    fatorial = 1
    contador = num

    # Calcula o fatorial usando um laço `while`
    # A condição `contador > 0` garante que o laço será executado enquanto o contador não atingir zero
    while contador > 0:
        # Exibe o valor atual do contador (parte do cálculo do fatorial)
        print(f'{contador}', end=' ')
        
        # Exibe o símbolo "x" entre os números, mas coloca "=" no final da sequência
        print(f' x ' if contador > 1 else ' = ', end=' ')
        
        # Atualiza a variável `fatorial` multiplicando pelo valor atual do contador
        fatorial *= contador  # Equivalente a: fatorial = fatorial * contador
        
        # Decrementa o contador em 1 para seguir com o próximo valor
        contador -= 1

    # Exibe o resultado do fatorial após o término do laço
    print(f"\nO fatorial de {num} é {fatorial}.")
