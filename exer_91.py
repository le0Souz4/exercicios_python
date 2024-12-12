"""
Crie um programa que leia nome, ano de nascimento e
carteira de trabalho e cadastre-o (junto à idade) em um dicionário
Se por acaso a CTPS for diferente de zero, o dicionário receberá tambem
o ano de contratação e o salário.
Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se
aposentar.
"""

from datetime import date, datetime

from dateutil.utils import today

funcionario = {}

funcionario['nome'] = input("nome: ")
funcionario['nascimento'] = int(input("ano de nascimento: "))
funcionario['CTPS'] = int(input("CTPS: "))
ano_atual = datetime.now().year
idade = ano_atual - funcionario['nascimento']

if funcionario['CTPS'] != 0:
    funcionario['contratação'] = int(input("ano de contratação: "))
    funcionario['salario'] = float(input("salário: "))
    aposentadoria = funcionario['nascimento'] + 65
else:
    print(f"primeiro emprego de {funcionario['nome']} ")
    aposentadoria = funcionario['nascimento'] + 65

print(f"FUNCIONÁRIO CADASTRADO COM SUCESSO: ")
for k, v in funcionario.items():
    print(f"{k}: {v}")
print(f'seu funcionário vai se aposentar em {aposentadoria} com 65 anos')







