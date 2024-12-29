"""faça um programa que leia 4 notas de um
aluno e calcule sua média. Mostrando uma mensagem
no final, de acordo com a sua nota atingida.
média < 5.0 : reprovado
média >= 5 e <= 6.9 : recuperação
média >=7 : aprovado"""

# Solicita o nome do professor
nome = input('Por favor, insira seu nome:\n ')

# Exibe uma mensagem de boas-vindas
print("=" * 40)
print(f"BEM VINDO(A) PROFESSOR(A) {nome}")
print("=" * 40)

# Solicita as notas do aluno
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
nota4 = float(input('Insira a quarta nota: '))

# Calcula a média das quatro notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Avalia o desempenho do aluno de acordo com a média
if media < 5.0:
    # Se a média for menor que 5.0, o aluno foi reprovado
    print(f"Sinto muito, o aluno foi reprovado pois sua média foi {media:.2f}")
elif 5.0 <= media <= 6.9:
    # Se a média estiver entre 5.0 e 6.9, o aluno está em recuperação
    print(f"O aluno está de recuperação pois sua média foi {media:.2f}")
else:
    # Se a média for maior ou igual a 7.0, o aluno foi aprovado
    print(f"Parabéns, o aluno foi aprovado pois sua média foi {media:.2f}")
