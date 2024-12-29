"""
 Faça um programa que tenha uma função chamada escreva()
 que receba um texto como parametro e motre uma mensagem
 com tamanho adaptável
"""

def mensagem(msg):  # Define a função 'mensagem' que recebe um parâmetro 'msg'
    tam = len(msg) + 4  # Calcula o tamanho necessário para a moldura com base no comprimento da mensagem
    print("~" * tam)  # Imprime uma linha de "~" com o comprimento da moldura
    print(f"  {msg}")  # Imprime a mensagem centralizada, com dois espaços de margem
    print("~" * tam)  # Imprime outra linha de "~" com o mesmo comprimento da moldura

# Exemplo de uso da função
mensagem("Olá mundo!")  # Chama a função com a mensagem "Olá mundo!"
mensagem("Me chamo Leonardo Souza")  # Chama a função com outra mensagem
