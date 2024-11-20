"""
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
 de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20)
 e mostrá-lo por extenso.
"""


numeros_por_extenso = (
    "zero", "um", "dois", "três", "quatro",
    "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "catorze",
    "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    numero_usuario = int(input("digite um número de 0 a 20:\n"))
    if numero_usuario > 20 or numero_usuario < 0: # o código do professor tambem trouxe a forma if 0 > numero_usuario > 20
        numero_usuario = int(input("por favor, digite um número entre 0 e 20"))
    print(f'você digitou {numeros_por_extenso[numero_usuario]}')
    decisao = input('deseja continuar? [S] // [N]\n').strip().upper()[0]
    if decisao == "N": # dica de melhoria de acordo com o Copilot para melhorar a legibilidade e funcionalidade do sistema
        break

#if decisao == 'S':
#    numero_usuario = int(input("digite um número de 0 a 20:\n"))
#    print(f'você digitou {numeros_por_extenso[ numero_usuario ]}')
#else:
#   break


"""
edit1: as tuplas podem ser exibidas das seguintes formas:

for comida in lanche:
    print(f'Eu vou comer {comida} ')
    demonstra uma forma simples de mostrar todos os itens da tupla

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
    essa forma mostra tanto o conteudo da tupla como a posição que ela ocupa, formando uma lista 
    por meio da função range() que começa do zero e o final irá ser o total de elementos da tupla,
    obtido por meio da função len()

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
    mesma coisa da forma anterior apenas mudando a forma como se consegue a posição dos elementos
    através da função enumerate() e alocando na var: pos
"""