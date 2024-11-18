"""
faça um programa que leia um número qualquer e mostre seu fatorial
fatorial -> n! = n x (n-1) x ... x 1
"""
# Lê o número
num = int(input("Digite um número: "))

# Verifica se o número é negativo
if num < 0:
    print("Não existe fatorial para números negativos.")
else:
    fatorial = 1
    contador = num

    # Calcula o fatorial usando while
    # a cada iteração o num do contador decresce em 1 e fazendo que
    # a var: fatorial multiplique o valor e armazene o anterior
    while contador > 0:
        print(f'{contador}', end=' ')
        print(f' x ' if contador > 1 else ' = ' ,end=' ') # esta é a primeira vez que vejo o if sendo usado dessa manner
        fatorial *= contador # é a mesma coisa que fatorial = fatorial * contador
        contador -= 1

    # Exibe o resultado
    print(f"\nO fatorial de {num} é {fatorial}.")

"""
este exercicio é muito mais facil do que se imagina, tive um pouco de dificuldade 
de imaginar como fazer a var: contador decrescer uma unidade
"""