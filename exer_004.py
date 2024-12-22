"""Faça um programa que leia um numero inteiro
e mostre na tela seu sucessor e seu antecessor"""

# Solicita ao usuário que digite um número.
# A função input() recebe o valor como texto, e a função int() converte esse texto para um número inteiro.
num = int(input("Digite um numero: "))

# Calcula o antecessor do número. Para isso, subtrai 1 do número digitado.
ant = num - 1

# Calcula o sucessor do número. Para isso, soma 1 ao número digitado.
suc = num + 1

# Exibe uma mensagem ao usuário mostrando o número digitado,
# seu antecessor (o número que vem antes) e seu sucessor (o número que vem depois).
# A f-string permite inserir valores de variáveis diretamente dentro do texto usando {}.
print(f"o numero digitado foi {num}, seu sucessor é {suc} e seu antecessor {ant}")

# O mesmo exercício pode ser feito de uma maneira mais simples e compacta:
# Aqui, o cálculo do sucessor e do antecessor é feito diretamente dentro da exibição (print), sem variáveis extras.

# Solicita ao usuário que digite outro número.
num2 = int(input("Digite outro numero: "))

# Exibe o número digitado, seu sucessor e seu antecessor diretamente no print,
# sem a necessidade de criar variáveis separadas para o antecessor e sucessor.
print(f"o numero escolhido foi {num2}, seu sucessor é {num2+1} e seu antecessor {num2-1}")
