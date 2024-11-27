'''
edit1: ao fazer uma cópia de listas é importante lembrar que
list1 = list2, ao ser dado esse comando vai ser criada uma ponte
entre as duas listas, ou seja, o que for mudado em uma, vai ser mudado
em outra.
para fazer uma cópia que não seja mutável caso a primeira seja
modificada é necessário fazer o seguinte:
list1 = list2[:], usando o fatiamento de strings conseguimos pegar
todos os dados

edit2: dado uma lista pessoas = [['pedro', 19], ['maria', 22], ['joao', 17], ['carlos, 35']]
for p in galera:
    print(p) --> vai informar todos os nomes e idades presentes na lista
    print(p[0]) --> vai informar somente os nomes
    print(p[1]) --> vai informar somente as idades

edit3: mas como fazer para construir listas compostas a partir de inputs?
galera = list() --> lista principal
dados = list() --> lista temporária
for cont in range (0,3):
    dados.append(str(input('nome: ')))
    dados.append(int(input('idade: '))
    galera.append(dados[:])
    dado.clear()

    l.e = criei um laço que vai perguntar 3x qual o nome e a idade
    a serem alocadas dentro da lista dados, após isso os inputs dentro da lista
    dados são copiados para a lista galera e então a lista dados é apagada, ficando
    a lista galera com os dados originais

edit3: estruturas condicionais tambem estão presentes nas variaveis compostas
tenho uma lista (galera = [['maria', 22], ['pedro', 50], ['joao', 11]
e eu quero mostrar só quem é maior de idade:
for p in galera:
    if p[1] >= 18:
        print(f'p[0] é maior de idade')
    else:
        print(f'p[0] é menor de idade')

    l.e: criei um laço com um verificador (p) que irá percorrer a lista galera,
    o verificador irá pegar o item [1] de cada sublista, nesse caso, a idade, e
    verificará se tem o valor maior ou igual a 18. então como retorno, o verificador
    irá pegar o item de posição[0], nessa caso o nome.
'''