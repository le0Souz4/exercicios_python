"""
Crie um poprograma que leia o nome, sexo, idade de várias pessoas
guardando os dados de cada pessoa em um dicionário e cada dicionário em
uma lista.
no final mostre:
a >> quantas pessoas foram cadastradas;
b >> a média da idade;
c >> uma lista com as mulheres;
d >> uma lsita de pessoas com idade acima da média
"""
from math import trunc

cidade = list()
pessoa = dict()

while True:
    pessoa['nome'] = input("nome: ")
    pessoa['sexo'] = input("genero: ").strip().upper()[0]
    pessoa['idade'] = int(input("idade: "))
    cidade.append(pessoa.copy())
    pessoa.clear()
    dec = input("continua? ").strip().upper()[0]
    if dec == 'N':
        break

quantas_pessoas = len(cidade)

idades = list(pessoa['idade'] for pessoa in cidade)
media_idade = trunc(sum(idades) / len(idades))


print(f"Voce cadastrou um total de {len(cidade)} pessoas, aqui vão alguns dados: \n"
      f"a média das idades cadastradas foi: {media_idade} anos"
      "\nas mulheres cadastradas foram:")
for pessoa in cidade:
    if pessoa['sexo'] == "F":
        print(f"\n{pessoa['nome']} com {pessoa['idade']} anos")
print(f"as pessoas com idade acima da média são:")
for pessoa in cidade:
    if pessoa['idade'] > media_idade:
        print(f'\n {pessoa['nome']} com {pessoa['idade']} anos')