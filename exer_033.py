"""
Escreva um programa que pergunte o salário de um funcionário 
e calcule o valor do seu aumento. Para salários superiores a R$1250,00, 
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

# Solicita o salário do funcionário
salario = float(input("Digite o salário do funcionário: R$"))

# Verifica a condição do salário e calcula o aumento
if salario > 1250:
    aumento = salario * 0.10  # 10% de aumento
    novo_salario = salario + aumento
    print(f"Com um aumento de 10%, o novo salário será R${novo_salario:.2f}.")
else:
    aumento = salario * 0.15  # 15% de aumento
    novo_salario = salario + aumento
    print(f"Com um aumento de 15%, o novo salário será R${novo_salario:.2f}.")
