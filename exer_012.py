"""faça um algoritmo que leia o salario de um funcionário
e mostre seu novo salário com 15% de aumento"""

# Solicita ao usuário o salário atual e converte a entrada para número decimal (float)
sal1 = float(input("Informe o salário: R$ "))

# Calcula o novo salário após o reajuste de 15%. 
# A operação 'sal1 * 0.15' calcula 15% do salário atual, que é somado ao valor original do salário
sal2 = sal1 + (sal1 * 0.15)

# Exibe o novo salário após o reajuste de 15%
print(f"O novo salário, com um reajuste de 15%, terá o valor de {sal2}")
