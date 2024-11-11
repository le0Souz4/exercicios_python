"""faça um programa que leia 4 notas de um
aluno e calcule sua média. Mostrando uma mensagem
no final, de acordo com a sua nota atingida.
média < 5.0 : reprovado
média >= 5 e <= 6.9 : recuperação
média >=7 : aprovado"""

nome = input('Por favor, insira seu nome:\n ')

print("=" * 40)
print(f"BEM VINDO(A) PROFESSOR(A) {nome}")
print("=" * 40)

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
nota4 = float(input('Insira a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4)/ 4
if media < 5.0:
    print(f"sinto muito, o aluno foi reprovado pois sua média foi {media}")
elif media >= 5.0 or media <= 6.9:
    print(f"o aluno está de recuperação pois sua média foi {media}")
else:
    print(f"parebens, o aluno foi aprovado pois sua média foi {media}")
