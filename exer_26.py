'''
Faça um programa queleia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente
'''

# usando o fatiamento de strings
nome = input('por favor, digite seu nome completo: ').strip().lower()
print(f"Seu primeiro nome é {nome[0:nome.find(" ")]}")
print(f'E seu ultimo nome é {nome[nome.rfind(" "):]}')

# usando a função .split()
nome2 = input("por favor, digite outro nome: ")
n = nome2.split()
print(f'Seu primeiro nome é {n[0]}, e '
      f'\nseu ultimo nome é {n[-1]}')