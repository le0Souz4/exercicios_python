"""Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores "m" ou "f". caso esteja errado,
 peça a digitação novamente até ter um valor correto"""

# A variável começa com um valor nulo que será preenchido depois
gen = ""

# A condição verifica se o valor digitado está dentro da lista de generos aceitos
while gen not in ['m', 'f']:

    # Aloquei a variável
    # Usei tambem as funções strip() para caso o usuário coloque um espaço sem querer e o lower() para trazer a opção para minuscula
    gen = str(input("Digite o sexo de uma pessoa: [m] ou [f]\n")).strip().lower()

    # Estrutura condicional que retorna uma mensagem caso o genero esteja cadastrado ou incorreto
    if gen == 'm':
        print('genero masculino cadastrado')
    elif gen == 'f':
        print('genero feminino cadastrado')
    else:
        print('por favor, digite um genero valido')


"""A resolução que o professor trouxe é bem mais enxuta,
segue o codigo:

 sexo = str(input('informe seu sexo: [M] ou [F]\n')).strip().upper()[0]
 while sexo not in 'MmFf':
    sexo = str(input('dados invalidos, por favor informe seu sexo: [M] ou [F]\n')).strip().upper()[0]
print(f'sexo {sexo} registrado com sucesso'

 """

"""O que eram 9 linhas de codigo (com excessão dos comentários)
viraram 4 linhas, alem de parecer bem mais profissional"""