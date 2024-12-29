"""faça um programa que leia o ano de nascimento de um jovem
e informe de acordo com sua idade, se ele ainda vai se alistar no
serviço militar. Se é a hora de se alistar ou se já passou do tempo
de alistamento.
seu programa tambem deverá mostrar o tempo que falta ou que
passou do prazo"""

# Importa a biblioteca datetime para obter o ano atual
import datetime

# Imprime uma linha de boas-vindas ao sistema
print("=" * 40)
print("BEM VINDO A CENTRAL DE ALISTAMENTO")
print("=" * 40)

# Solicita que o usuário informe seu gênero
print("Por favor, responda às seguintes perguntas:")
gen = input("Qual seu gênero? (masc) // (fem)\n")

# Verifica se o gênero informado é masculino
if gen == "masc":
    # Solicita o ano de nascimento do usuário caso ele tenha respondido "masc"
    ano_nascimento = int(input("Informe seu ano de nascimento: \n"))

    # Obtém o ano atual usando a função today() da biblioteca datetime
    ano_atual = datetime.date.today().year

    # Calcula a idade do usuário subtraindo o ano de nascimento do ano atual
    idade = ano_atual - ano_nascimento

    # Exibe a idade calculada para o usuário
    print(f"Sua idade atual é {idade} anos")

    # Verifica se a idade é maior, menor ou igual a 18 anos
    if idade > 18:
        # Caso o usuário tenha mais de 18 anos, calcula quanto tempo ele está atrasado para o alistamento
        atraso = idade - 18
        print(f"Você precisa se alistar\nVocê está atrasado em {atraso} anos")
    elif idade < 18:
        # Caso o usuário tenha menos de 18 anos, calcula quanto tempo ele está adiantado para o alistamento
        adiantado = 18 - idade
        print(f"Você está adiantado, aliste-se daqui a {adiantado} anos")
    else:
        # Caso o usuário tenha exatamente 18 anos, informa que ele está no momento do alistamento
        print("Está no momento de você se alistar!")
else:
    # Se o gênero não for masculino (feminino), informa que não há obrigatoriedade de alistamento
    print("Você não possui obrigatoriedade de alistamento.")
