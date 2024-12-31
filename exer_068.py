"""Crie um programa que leia a idade e o sexo 
de várias pessoas. A cada pessoa cadastrada, o 
programa deverá perguntar se o usuário quer ou 
não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""

# Inicialização das variáveis de contagem
maiores_18 = 0
homens = 0
mulheres_menor_20 = 0

while True:
    # Leitura dos dados de idade e sexo
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M para masculino, F para feminino): ").strip().lower()

    # Condição para contar quantas pessoas têm mais de 18 anos
    if idade > 18:
        maiores_18 += 1

    # Condição para contar quantos homens foram cadastrados
    if sexo == 'm':
        homens += 1

    # Condição para contar quantas mulheres têm menos de 20 anos
    if sexo == 'f' and idade < 20:
        mulheres_menor_20 += 1

    # Pergunta se o usuário quer continuar cadastrando
    continuar = input("Você deseja continuar cadastrando pessoas? (S para sim, N para não): ").strip().lower()
    if continuar != 's':
        break

# Exibição dos resultados
print(f"\nA) Quantas pessoas têm mais de 18 anos: {maiores_18}")
print(f"B) Quantos homens foram cadastrados: {homens}")
print(f"C) Quantas mulheres têm menos de 20 anos: {mulheres_menor_20}")
