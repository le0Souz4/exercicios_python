"""escreva um programa que leia um numero inteiro
qualquer e peça para o usuário escolher qual será a
base de conversão. Sendo 1 para binário, 2 para octal e 3 para hexadecimal."""
print("="*40)
print("Bem vindo ao conversos de medidas")
print("="*40)
num = int(input("insira um numero inteiro a ser convertido: "))
decisao = int(input("ok, agora insira para qual opção converte-lo:"
      "\n(1)binário (2)octal (3)hexadecimal"
                    "\n"))
if decisao == 1:
    print(f"o numero {num} na forma binária fica {bin(num)}")
elif decisao == 2:
    print(f"o numero {num} na forma octal fica {oct(num)}")
elif decisao == 3:
    print(f"o numero {num} na forma hexadecimal fica {hex(num)}")
else:
    print("escolha um opção válida")