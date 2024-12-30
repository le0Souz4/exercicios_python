"""Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores "m" ou "f". caso esteja errado,
 peça a digitação novamente até ter um valor correto"""

# A variável começa com um valor nulo que será preenchido depois
gen = ""

# O loop continua enquanto a entrada do usuário não for válida ('m' ou 'f')
while gen not in ['m', 'f']:
    # Solicita ao usuário que insira seu gênero
    # strip() remove espaços extras antes e depois da entrada
    # lower() converte a entrada para minúsculas para facilitar a validação
    gen = str(input("Digite o sexo de uma pessoa: [m] ou [f]\n")).strip().lower()

    # Verifica se o gênero digitado é masculino ('m') e exibe a mensagem correspondente
    if gen == 'm':
        print('Gênero masculino cadastrado')
    # Verifica se o gênero digitado é feminino ('f') e exibe a mensagem correspondente
    elif gen == 'f':
        print('Gênero feminino cadastrado')
    # Caso a entrada seja inválida, exibe uma mensagem de erro
    else:
        print('Por favor, digite um gênero válido')

# Solicita ao usuário que informe seu sexo e já trata a entrada
# strip() remove espaços extras, upper() converte para maiúsculas e [0] seleciona apenas a primeira letra
sexo = str(input('Informe seu sexo: [M] ou [F]\n')).strip().upper()[0]

# Loop que continua enquanto a entrada não estiver dentro dos valores válidos ('M' ou 'F')
while sexo not in 'MF':
    # Solicita novamente a entrada caso seja inválida
    sexo = str(input('Dados inválidos, por favor informe seu sexo: [M] ou [F]\n')).strip().upper()[0]

# Exibe uma mensagem final indicando que o sexo foi registrado com sucesso
print(f'Sexo {sexo} registrado com sucesso')
