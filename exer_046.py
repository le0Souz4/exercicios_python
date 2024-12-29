"""Faça um programa que mostre na tela todos
os numeros pares que estão no
intervalo entre 1 e 50"""

# Primeira forma: usando o range para criar uma sequência com números pares

# O laço 'for' percorre uma sequência de números gerada pela função 'range(0, 50, 2)'.
# O range(0, 50, 2) gera uma sequência que começa em 0, vai até 50 (não incluindo o 50), e de 2 em 2. Ou seja, ele gera números pares: 0, 2, 4, 6, ..., 48.
for c in range(0, 50, 2):
    # O 'print(c + 2, end=" ")' imprime o valor de 'c' somado a 2. Isso faz com que o programa pule o 0 e comece a imprimir a partir do 2.
    # O parâmetro 'end=" "' dentro da função print é usado para alterar o comportamento padrão do print.
    # Por padrão, o print adiciona uma quebra de linha (um '\n') após cada impressão. Ao usar 'end=" "', podemos fazer com que os valores sejam impressos na mesma linha, separados por um espaço.
    print(c + 2, end=' ')

# Após o laço, o print("fim") é executado para mostrar a palavra 'fim' após a contagem.
print("fim")

# Segunda forma: verificando se os números são pares com o uso de 'if'
# Agora, vamos fazer o mesmo processo, mas utilizando uma verificação condicional para garantir que estamos lidando com números pares.

for c in range(0, 50):  # Criamos uma sequência de 0 a 49 (não inclui 50)
    # O 'if c % 2 == 0' verifica se o número atual ('c') é divisível por 2, ou seja, se é um número par.
    # O operador '%' retorna o resto da divisão. Se 'c % 2 == 0', significa que o número 'c' é divisível por 2 e, portanto, é par.
    if c % 2 == 0:
        # Caso o número seja par, 'print(c + 2, end=" ")' imprime o número somado a 2.
        # Ou seja, esse código pula o número 0 e começa a imprimir a partir do 2.
        print(c + 2, end=' ')

# Após o laço, o print("fim") é executado novamente para mostrar a palavra 'fim' após a contagem.
print("fim")

