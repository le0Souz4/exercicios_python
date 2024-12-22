"""faça um programa que leia um numero inteiro e mostrea
na tela a sua tabuada"""

# Solicita ao usuário que digite um número para calcular sua tabuada.
# A função input() captura o valor como texto, e int() converte para um número inteiro.
num = int(input("Digite um numero: "))

# Exibe a mensagem inicial indicando que será calculada a tabuada do número digitado.
# A f-string permite inserir o número diretamente na mensagem.
print(f"A tabuada de {num} é:")

# Exibe o cálculo da tabuada de 1 a 10.
# Cada linha multiplica o número digitado por um valor fixo (de 1 a 10) e exibe o resultado.
# O uso de f-strings ajuda a formatar os cálculos diretamente no texto.
print(
    f"{num} * 1 = ", num * 1,
    f"\n{num} * 2 = ", num * 2,
    f"\n{num} * 3 = ", num * 3,
    f"\n{num} * 4 = ", num * 4,
    f"\n{num} * 5 = ", num * 5,
    f"\n{num} * 6 = ", num * 6,
    f"\n{num} * 7 = ", num * 7,
    f"\n{num} * 8 = ", num * 8,
    f"\n{num} * 9 = ", num * 9,
    f"\n{num} * 10 = ", num * 10,
)

# Observação: Mais pra frente, esse exercício poderá ser resolvido de maneira mais eficiente,
# utilizando laços de repetição (como o for ou o while), que evitam a repetição do código.
