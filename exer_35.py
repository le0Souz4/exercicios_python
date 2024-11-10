"""escreva um programa para aprovar um emprestimo
bancário para a compra de uma casa.
o programa vai perguntar o valor da casa, o salario do comprador
e em quantos anos ele vai pagar.
calcule o valor da prestação mensal, sabendo que ela não pode
exceder 30% do salario ou então o emprestimo será negado."""

print("="*40)
print("seja bem vindo ao banco imaginário")
print("="*40)
dec = input("gostaria de simular um consórcio? (s/n) ")
if dec == "s":
    print("certo, vamos começar")
    valor_casa = int(input("qual seria o valor da casa negociada?: R$ " ))
    renda_men = int(input("qual seria o renda mensal?: R$ "))
    anos_pgnd = int(input("em quantos anos pretende pagar?: "))

    if anos_pgnd <= valor_casa and anos_pgnd > 0 and (valor_casa / (anos_pgnd * 12)) >= renda_men * (30 / 100):
        print("sinto muito, o consórcio foi negado pois não entende aos requisitos necessários")
    else:
        print(f"parabens, seu consorcio foi aprovado, no valor de R${valor_casa / (anos_pgnd * 12):.2f} mensais, por {anos_pgnd * 12} meses")

else:
    print("ok, até um proximo momento")
    exit()