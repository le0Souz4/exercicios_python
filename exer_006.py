"""desenvolva um programa que leia as notas de um aluno,
calcule e mostre sua média"""

# Solicita ao usuário que insira a primeira nota do aluno.
# A função input() captura o dado como texto, e int() converte para um número inteiro.
nota1 = int(input("Digite a primeira nota: "))

# Solicita ao usuário que insira a segunda nota do aluno.
nota2 = int(input("Digite a segunda nota: "))

# Solicita ao usuário que insira a terceira nota do aluno.
nota3 = int(input("Digite a terceira nota: "))

# Calcula a média aritmética das três notas.
# A média é obtida somando as notas e dividindo o total por 3.
med = (nota1 + nota2 + nota3) / 3

# Exibe a média final do aluno.
# A f-string permite formatar a mensagem com a variável diretamente no texto.
print(f"A nota final do aluno foi {med}")
