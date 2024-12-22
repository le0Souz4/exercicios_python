"""
Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e
quantos gols ele marcou. O programa deverá ser capaz de mostrar
a ficha do jogador, mesmo que algum dado não tenha sido
informado corretamente.
"""


# Definindo a função ficha()
def ficha(nome='', gols=0) :
    # Verifica se o nome está vazio. Se estiver, coloca "Desconhecido" como nome.
    if nome == '' :
        nome = 'Desconhecido'

    # Verifica se o número de gols é inválido (como uma string ou valor negativo).
    # Se for inválido, assume que o jogador marcou 0 gols.
    if not isinstance(gols, int) or gols < 0 :
        gols = 0

    # Exibe a ficha do jogador com o nome e os gols
    print(f'Nome do jogador: {nome}')
    print(f'Gols marcados: {gols}')


# Exemplo de uso
# Caso o usuário não forneça o nome, ele será substituído por 'Desconhecido'.
ficha('Cristiano Ronaldo', 30)  # Jogador com nome e gols
ficha('Neymar')  # Jogador com nome, mas sem gols informados
ficha(gols=20)  # Jogador sem nome, mas com gols informados
ficha()  # Nenhum dado informado
