'''
Faça um programa queleia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente
'''

# Usando fatiamento de strings
nome = input('Por favor, digite seu nome completo: ').strip().lower()

# Aqui, procuramos o primeiro nome até o espaço, e o último nome a partir do último espaço
# Fatiamento para pegar o primeiro nome
print(f"Seu primeiro nome é {nome[:nome.find(' ')]}")

# Fatiamento para pegar o último nome
print(f'E seu último nome é {nome[nome.rfind(" ") + 1:]}')

# Usando a função .split()
nome2 = input("Por favor, digite outro nome: ")

# A função .split() divide a string em partes com base no espaço
n = nome2.split()

# Acessa o primeiro nome (índice 0) e o último nome (índice -1)
print(f'Seu primeiro nome é {n[0]}, e '
      f'\nseu último nome é {n[-1]}')
