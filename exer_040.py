"""a confederação nacional de natação precisa de
um programa que leia o ano de nascimento de um atleta
e mostre sua categoria de acordo com a idade"""

import datetime

# Cabeçalho de boas-vindas
print("=" * 40)
print("BEM VINDO A CONFEDERAÇÃO NACIONAL DE NATAÇÃO")
print("=" * 40)

# Solicitar o ano de nascimento do atleta
ano_nasc = int(input("Informe o ano de nascimento de seu atleta: "))
ano_atual = datetime.date.today().year

# Calcular a idade do atleta
idade = ano_atual - ano_nasc
print(f"A idade de seu atleta é {idade} anos.")

# Determinar a categoria de acordo com a idade
if idade <= 9:
    print("Seu atleta competirá na modalidade MIRIM.")
elif idade <= 14:
    print("Seu atleta competirá na modalidade INFANTIL.")
elif idade <= 19:
    print("Seu atleta competirá na modalidade JUNIOR.")
elif idade <= 25:
    print("Seu atleta competirá na modalidade SENIOR.")
else:
    print("Seu atleta competirá na modalidade MASTER.")
