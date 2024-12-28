
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

def contador(inicio, fim, passo):  # Criação da função 'contador' com 3 parâmetros
    # Verificar caso o passo seja 0, se for, o programa será interrompido
    if passo == 0:
        print("O passo não pode ser zero.")
        return  # Retorna imediatamente e não executa mais nada se o passo for 0

    # Print apresentando o valor dos parâmetros
    print(f"Contagem de {inicio} até {fim}, de {passo} em {passo}:")

    # Verificar se o contador será crescente ou decrescente
    if passo > 0:
        # Se o passo for positivo, a contagem será crescente
        for i in range(inicio, fim + 1, passo):  # A função range cria a sequência de números
            print(i, end=" ")                  # Imprime os números com o mesmo espaço entre eles
    else:
        # Se o passo for negativo, a contagem será decrescente
        for i in range(inicio, fim - 1, passo):
            print(i, end=" ")  # Imprime os números, no caso de uma contagem regressiva

    # Após imprimir os números, a função faz uma nova linha para melhorar a leitura
    print()

# Exemplo de contagem crescente (de 1 até 10, de 1 em 1)
contador(1, 10, 1)

# Exemplo de contagem decrescente (de 10 até 0, de 2 em 2)
contador(10, 0, -2)

# Criando o contador personalizado com entradas do usuário
inicio = int(input("inicio: "))  # Solicita o valor de 'inicio'
fim = int(input("fim: "))        # Solicita o valor de 'fim'
passo = int(input("passo: "))    # Solicita o valor de 'passo'

# Chama a função contador passando os valores fornecidos pelo usuário
contador(inicio, fim, passo)

