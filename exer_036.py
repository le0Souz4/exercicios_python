"""escreva um programa que leia um numero inteiro
qualquer e peça para o usuário escolher qual será a
base de conversão. Sendo 1 para binário, 2 para octal e 3 para hexadecimal."""

# Apresentação inicial do programa
print("=" * 40)  # Linha decorativa para melhorar a aparência
print("Bem-vindo ao Conversor de Medidas")  # Título do programa
print("=" * 40)  # Linha decorativa para separação visual

# Solicita ao usuário um número inteiro para a conversão
num = int(input("Insira um número inteiro a ser convertido: "))

# Apresenta as opções de conversão disponíveis
decisao = int(input("Ok, agora insira para qual opção deseja convertê-lo:"
                    "\n(1) Binário"
                    "\n(2) Octal"
                    "\n(3) Hexadecimal"
                    "\n"))  # Captura a escolha do usuário

# Verifica qual opção o usuário escolheu e realiza a conversão correspondente
if decisao == 1:
    # Utiliza a função bin() para converter o número para binário
    print(f"O número {num} na forma binária é {bin(num)[2:]}")
elif decisao == 2:
    # Utiliza a função oct() para converter o número para octal
    print(f"O número {num} na forma octal é {oct(num)[2:]}")
elif decisao == 3:
    # Utiliza a função hex() para converter o número para hexadecimal
    print(f"O número {num} na forma hexadecimal é {hex(num)[2:]}")
else:
    # Informa ao usuário que a escolha foi inválida
    print("Escolha uma opção válida.")
