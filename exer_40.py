"""a confederação nacional de natação precisa de
um programa que leia o ano de nascimento de um atleta
e mostre sua categoria de acordo com a idade"""

import datetime

print("=" * 40)
print("BEM VINDO A CONFEDERAÇÃO NACIONAL DE NATAÇÃO")
print("=" * 40)

ano_nasc = int(input("informe o ano de nascimento de seu atleta: "))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc
print(f"a idade de seu atleta é, {idade} anos")

if idade <= 9:
    print("seu atleta competirá na modalidade MIRIM")
elif idade <= 14:
    print("seu atleta competirá na modalidade INFANTIL")
elif idade <= 19:
    print("seu atleta competirá na modalidade JUNIOR")
elif idade <= 25:
    print("seu atleta competirá na modalidade SENIOR")
else:
    print("seu atleta competirá na modalidade MASTER")