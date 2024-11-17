"""Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores "m" ou "f". caso esteja errado,
 peça a digitação novamente até ter um valor correto"""

gen = "" # A variável começa com um valor nulo que será preenchido depois

while gen not in ['m', 'f']: # A condição verifica se o valor digitado está dentro da lista de generos aceitos

    gen = str(input("Digite o sexo de uma pessoa: [m] ou [f]\n")).lower() # Alocamos a variável e usamos o método lower() para aceitar caso o usuário escreva em maiúscula

    if gen == 'm': # Estrutura condicional que retorna uma mensagem caso o genero esteja cadastrado ou incorreto
        print('genero masculino cadastrado')
    elif gen == 'f':
        print('genero feminino cadastrado')
    else:
        print('por favor, digite um genero valido')