"""
Crie um programa que tenha uma função fatorial()
que receba dois parâmetros: o primeiro que indique
o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será
mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial(valor, show = False):
    # a função recebe dois parametros sendo valor o numera que será fatorado
    # e show como parametro opcional para controlar se a conta aparece ou não

    f = 1
    # iniciamos a variavel f com 1, ela será responsavel por armazenar o resultado

    for c in range(valor, 0, -1):
    # O laço for irá percorrer os números de valor até 0, decrescendo em 1

        if show:
        # se o parametro show for verdadeiro, este bloco será executado

            print(c, end = ' ')
            # imprime o numero seguido de um espaço

            if c > 1:
                print(' x ', end = " ")
            else:
                print(' = ', end = " ")
            # enquanto o valor de c for maior que 1, ele vai ser seguido de um x
            # denotando a multiplicação, e ao chegar ao fim (c = 1) será colocado
            # o sinal de igual

        f *= c
        # o valor de c será multiplicado ao valor de f que será incrementado a
        # cada volta do laço

    return f
    # retorna o valor final de f

print(fatorial(5, show=False))
# se colocar (show = True) o retorno será = 5 x 4 x 3 x 2 x 1 = 120
# senão = somente 120