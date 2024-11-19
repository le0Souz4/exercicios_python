"""
Faça um programa que mostre a tabuada de vários
números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo
"""

num_1 = 0

while True:
    num_1 = int(input("digite o número a ser multiplicado: "))
    if num_1 < 0:
        print("por favor, digite um número positivo")
    break

    # a seguinte forma é muito mais bonita usando uma list comprehension:
    resultados = [f"{num_1} x {i} = {num_1 * i}" for i in range(1, 11)]
    # a range presente cria um intervalo de numeros que vai de 1 até 10, o 11
    # é excluido, e a cada valor de i gerado é calculada uma multiplicação que será
    # alocada dentro da lista resultados

    print("\n" + "\n".join(resultados))
    # a função join está aqui para ajudar a concatenar as strings
    # normalmente é aplicada a iteráveis como listas e tuplas



# Esta forma é muito básica, que alem de ocupar muitas linhas é visualmente feio;
'''print(f"\n{num_1} x 1 = {num_1 * 1}"
      f"\n{num_1} x 2 = {num_1 * 2}"
      f"\n{num_1} x 3 = {num_1 * 3}"
      f"\n{num_1} x 4 = {num_1 * 4}"
      f"\n{num_1} x 5 = {num_1 * 5}"
      f"\n{num_1} x 6 = {num_1 * 6}"
      f"\n{num_1} x 7 = {num_1 * 7}"
      f"\n{num_1} x 8 = {num_1 * 8}"
      f'\n{num_1} x 9 = {num_1 * 9}'
      f'\n{num_1} x 10 = {num_1 * 10}')'''

"""
edit1: colocar a condicional if no final não fez com que o programa parasse, foi necessário colocar ele 
logo após o input
"""


