#faça um programa que leia o nome de uma pessoa
#e mostre uma mensagem de boas vindas

nome1 = input("olá, qual o seu nome?")
print("olá",nome1,"seja bem vindo")

nome2 = input("digite seu sobrenome: ")
print(f"funcionário,{nome1} {nome2}, cadastrado no sistema")

"""
Aqui vemos o uso da função input() que permitirá o usuário digitar algo, e poder 
atribuir o valor digitado à veriável, nesse caso, nome1 e nome2.
Temos Tambem dois exemplos de uso da função print() só que agora inserindo as variáveis
para que elas tambem sejam mostradas. 
No primeiro caso temos a variável isolada, e no segundo usando o comando f"" para avisar
a função que queremos concatenar as variáveis ao texto, colocando elas entre chaves {}
"""
