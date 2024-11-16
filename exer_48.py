"""utilize o mesmo exercicio 08, mostrando a tabuada
de um número que o usuário escolher, só que agora
utilizando o laço for"""

num = int(input("digite um número: ")) # Começo criando uma variável que será o numero a ser multiplicado

for tabuada in range(1, 11):
    print(f"{num} x {tabuada} = {num * tabuada}") # Crio um laço para mostrar toda a tabuada do número escolhido
dec = input("deseja saber a tabuada de mais algum número? (s) // (n)\n") # Aqui crio um laço de repetição que irá fazer com que
# o programa continue até que o usuário não queira mais

while dec == "s": #enquanto a decisão for sim, o laço se repetirá
    num2 = int(input("escolha um número: ")) # Toda vez que o laço recomeça, a variável é alterada
    for tabuada in range(1, 11):
        print(f"{num2} x {tabuada} = {num2 * tabuada}")
    dec = input("deseja saber a tabuada de mais algum número? (s) // (n)\n")
else:
    print("ok até uma proxima")




