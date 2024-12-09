"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

# Criando um dicioário vazio
boletim = {}

# Preenchendo o dicionário com os valores
boletim["nome"] = input(f"aluno: \nR: ")
boletim["nota1"] = float(input("digite a primeira nota: \nR: "))
boletim["nota2"] = float(input("digite a segunda nota: \nR: "))
boletim["média"] = (boletim["nota1"] + boletim["nota2"]) / 2

# Condicional que irá verificar a situação do aluno
if boletim["média"] > 6:
    boletim["situação"] = "APROVADO"
else:
    boletim[ "situação" ] = "REPROVADO"

# Retorno dos resultados
print(f'o aluno {boletim["nome"]} obteve média {boletim["média"]}, portanto está {boletim["situação"]}')
