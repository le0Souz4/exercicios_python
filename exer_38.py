"""faça um programa que leia o ano de nascimento de um jovem
e informe de acordo com sua idade, se ele ainda vai se alistar no
serviço militar. Se é a hora de se alistar ou se já passou do tempo
de alistamento.
seu programa tambem deverá mostrar o tempo que falta ou que
passou do prazo"""
import datetime

print("=" * 40)
print("BEM VINDO A CENTRAL DE ALISTAMENTO")
print("=" * 40)

print("Por favor, responda às seguintes perguntas:")
gen = input("Qual seu gênero? (masc) // (fem)\n")
if gen == "masc":
    ano_nascimento = int(input("Informe seu ano de nascimento: \n"))
    ano_atual = datetime.date.today().year
    idade = ano_atual - ano_nascimento
    print(f"Sua idade atual é {idade} anos")

    if idade > 18:
        atraso = idade - 18
        print(f"Você precisa se alistar\nVocê está atrasado em {atraso} anos")
    elif idade < 18:
        adiantado = 18 - idade
        print(f"Você está adiantado, aliste-se daqui a {adiantado} anos")
    else:
        print("Está no momento de você se alistar!")
else:
    print("Você não possui obrigatoriedade de alistamento.")
