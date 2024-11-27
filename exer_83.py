"""
Faça um programa que leia o nome e o peso de várias pessoas,
guardando tudo em uma lista. No final mostre:
--> quantas pessoas foram cadastradas;
--> uma listagem com as pessoas mais pesadas;
--> uma listagem com as pessoas mais leves
"""

pessoa_peso = list() # lista principal
pessoa_peso_temp = list() # lista temporária

# laço principal para alocar os inputs dentro da lista temporária
while True:
    pessoa_peso_temp.append(input('insira o nome da pessoa: \nR: '))
    pessoa_peso_temp.append(float(input('agora insira o peso dela: \nR: ')))
    pessoa_peso.append(pessoa_peso_temp[:]) # A cópia ([:]) é importante para evitar que a lista
                                            # pessoa_peso_temp seja modificada ao limpar a lista no próximo ciclo,
                                            # o que causaria que todos os elementos na lista principal
                                            # apontassem para a mesma lista temporária
    pessoa_peso_temp.clear()
    dec = input('deseja continuar? [S] // [N] \nR: ').strip().upper()[0]
    if dec == 'N':
        break

# pegando apenas os pesos
pesos = [p[1] for p in pessoa_peso]
maior_peso = max(pesos)
menor_peso = min(pesos)
"""
l.e: a compreensão de lista se dá seguinte maneira: identificador[p] irá percorrer a lista pessoa_peso pegando 
    apenas os pesos, que estão indicados pelo índice [1], em seguida aloco o maior e o menor peso da lista, obtidos
     por meio das funções max() e min()
"""

# listas dos mais pesados e dos mais leves
mais_pesados = [p[0] for p in pessoa_peso if p[1] == maior_peso]
mais_leves = [p[0] for p in pessoa_peso if p[1] == menor_peso]
"""
l.e: temos duas compreensões de listas que por meio do identificador [p] irão percorrer a lista pessoa_peso 
    pegando apenas os nomes, por meio do indice[0], e irão colocar junto com o peso correspondente das listas
    maior_peso e menor_peso.
        por que: o verificador if procura na lista pessoa_peso se o peso presente é o mesmo que da variável maior_peso
"""


# retorno
print(f"\nTotal de pessoas cadastradas: {len(pessoa_peso)}")
print(f"O maior peso foi {maior_peso}kg. Pessoa(s) mais pesada(s): {', '.join(mais_pesados)}")
print(f"O menor peso foi {menor_peso}kg. Pessoa(s) mais leve(s): {', '.join(mais_leves)}")
# a função join() está presente para com que a integração de listas em uma string seja feita de forma correta

"""
L.e:
    --> foram criadas duas listas, uma principal e outra temporária (l:9,10);
    --> foi criado um laço infinito (l:13) que irá alocar os inputs de nome e peso dentro da lista
    temporária (l:14,15);
    --> a lista criada é então inserida dentro da lista principal formando uma lista composta (l: 16), 
    seguida pela limpeza do conteudo da lista temporária (l: 17) para alocar a proxima lista a ser criada, garantindo que
    a entrada de sublistas na lista principal esteja correta.
        por quê: se a lista não for limpa, vai ser criada uma lista imensa que atrapalhará na hora de identificarmos
        o nome e o peso da pessoa inserida
    --> então é criado um laço condicional (l: 18) para o usuário decidir se vai ou não continuar, se não, o laço é
    quebrado (l: 20)
    --> fora do laço principal, crio uma lista que vai armazenar a apenas o peso das pessoas (l: 23), e dessa lista
    pego o meior peso (l: 23) e o menor (l: 24)
    --> faço então duas listas que pegam os mais pesados e os mais leves (l: 28, 29)
    --> o retorno será o total de pessoas cadastradas (l: 32), o maior peso e a pessoa mais pesada registrados (l: 33),
    mesma coisa com o menor peso e a pessoa mais leve registrada (l: 34)
"""