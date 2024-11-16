"""Faça um programa que mostre na tela todos
os numeros pares que estão no
intervalo entre 1 e 50"""
#forma simplificada
for c in range(0, 50, 2):
    print(c + 2, end=' ')
    # O parametro END dentro da função print serve para adicionar uma string após a saída
    # Da mesma forma que \n serve para quebrar linha, END serve justamente para o contrário
print("fim")

#forma completa
for c in range(0,50):
    if c % 2 == 0:
        print(c + 2, end=' ')
        # Aqui, o (+ 2) está tendo a função de pular o 0 e ir até o 50
        # Senão iria somente até o 48
print("fim")


