"""utilize o mesmo exercicio 08, mostrando a tabuada
de um número que o usuário escolher, só que agora
utilizando o laço for"""

# Primeiramente, criamos uma variável num para armazenar o número que o usuário irá escolher
num = int(input("digite um número: "))  # Solicita ao usuário para digitar um número inteiro.

# Agora, o primeiro laço 'for' será responsável por mostrar a tabuada desse número.
for tabuada in range(1, 11):  # O 'range(1, 11)' vai gerar os números de 1 até 10, ou seja, o intervalo da tabuada.
    # Aqui estamos imprimindo cada resultado da multiplicação, formando a tabuada.
    print(f"{num} x {tabuada} = {num * tabuada}")  # Exibe a multiplicação de 'num' por cada número de 1 a 10.

# Perguntamos ao usuário se ele quer saber a tabuada de outro número.
dec = input("deseja saber a tabuada de mais algum número? (s) // (n)\n")  # Se a resposta for 's', o programa repete.

# A estrutura de repetição 'while' garante que o programa continue até que o usuário escolha 'n' para não continuar.
while dec == "s":  # Enquanto a resposta for 's' (sim), o programa continuará repetindo.
    num2 = int(input("escolha um número: "))  # Solicita um novo número para mostrar sua tabuada.
    
    # A segunda parte do código irá gerar a tabuada para o novo número fornecido pelo usuário.
    for tabuada in range(1, 11):  # Gera a tabuada do novo número, com os números de 1 até 10.
        print(f"{num2} x {tabuada} = {num2 * tabuada}")  # Exibe cada multiplicação da tabuada do novo número.
    
    # Pergunta novamente se o usuário deseja continuar ou não.
    dec = input("deseja saber a tabuada de mais algum número? (s) // (n)\n")  # Se responder 's', o laço continua.

# Quando o usuário escolhe não continuar, o programa imprime a mensagem de despedida e termina.
else:
    print("ok até uma próxima")  # A mensagem é exibida caso o usuário digite 'n' (não), finalizando o programa.


