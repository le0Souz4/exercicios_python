"""
 Faça um programa que tenha uma função chamada escreva()
 que receba um texto como parametro e motre uma mensagem
 com tamanho adaptável
"""

def mensagem(msg):
     tam = len(msg) + 4
     print("~" * tam)
     print(f"  {msg}")
     print("~" * tam)

mensagem("Olá mundo!")
mensagem("Me chamo Leonardo Souza")