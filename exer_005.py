""" crie um algoritimo que leia um numero
e mostre o seu dobro, triplo e raiz quadrada"""

# Solicita ao usuário que digite um número.
# A função input() captura o dado como texto, e a função int() converte esse texto para um número inteiro.
num1 = int(input('Digite um numero: '))

# Calcula o dobro do número digitado, multiplicando o número por 2.
dob = num1 * 2

# Calcula o triplo do número digitado, multiplicando o número por 3.
tri = num1 * 3

# Calcula a raiz quadrada do número digitado.
# A raiz quadrada é calculada elevando o número à potência de 1/2.
rzq = num1 ** (1/2)

# Exibe o resultado formatado para o usuário.
# A f-string permite inserir as variáveis diretamente no texto entre {}.
# O comando \n insere uma quebra de linha, organizando a exibição em múltiplas linhas.
# A formatação {:.2f} exibe a raiz quadrada com duas casas decimais.
print(f"o numero escolhido foi {num1},"
      f"\n Seu dobro é {dob}, seu triplo é {tri}"
      f"\n e sua raiz quadrada {rzq:.2f}")
