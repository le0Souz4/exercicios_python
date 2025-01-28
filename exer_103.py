
"""
Crie um programa que tenha a função leiaint(), que vai funcionar de forma
semelhante à função input() do python, só que fazendo a validação para aceitar
apenas um valor numérico
"""

def leiaint(n):
    # Esta função verifica se o valor passado como argumento (n) é do tipo inteiro.
    if type(n) == int:  # Verifica se o tipo de 'n' é um número inteiro.
        return 'valor aceito'  # Se for inteiro, retorna a mensagem 'valor aceito'.
    else:
        return 'tipo incorreto'  # Caso contrário, retorna a mensagem 'tipo incorreto'.

# Testando a função com diferentes tipos de entrada
valor1 = leiaint(9)  # Passa o número inteiro 9 como argumento para a função.
valor2 = leiaint('n')  # Passa a string 'n' como argumento para a função.

# Exibe os resultados formatados
print(f'{valor1} e {valor2}')  # Mostra o resultado das chamadas da função leiaint.
# Saída esperada: 'valor aceito e tipo incorreto'.




