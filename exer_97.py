Segue o código transcrito da imagem:

"""
Faça um programa que tenha uma função chamada contador()  
que receba três parâmetros:  
>> inicio;  
>> fim;  
>> passo;  
seu programa tem que realizar três contagens através da função criada:  
>> de 1 até 10, de 1 em 1;  
>> de 10 até 0, de 2 em 2;  
>> uma contagem personalizada  
"""

def contador(inicio, fim, passo):  # Criação da função contador com parâmetros
    # Verificar caso o passo seja 0, se for, o programa será interrompido
    if passo == 0:
        print("O passo não pode ser zero.")
        return

    # Print apresentando o valor dos parâmetros
    print(f"Contagem de {inicio} até {fim}, de {passo} em {passo}:")

    # Verificar se o contador será crescente ou decrescente
    if passo > 0:
        for i in range(inicio, fim + 1, passo):  # A função range criará a sequência
            print(i, end=" ")                  # de números utilizando os parâmetros
    else:
        for i in range(inicio, fim - 1, passo):
            print(i, end=" ")
    print()

contador(1, 10, 1)
contador(10, 0, -2)

# Criando o contador personalizado
inicio = int(input("inicio: "))
fim = int(input("fim: "))
passo = int(input("passo: "))

# Crio variáveis para alocar os valores e em seguida passo como parâmetros da função
contador(inicio, fim, passo)

