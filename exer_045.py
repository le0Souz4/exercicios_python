"""Faça um programa que mostre na tela uma
contagem regressiva para o estouro de fogos
de artificio, indo de 10 até 0, com um pausa de
1 segundo entre elas"""

# Importamos o módulo 'time' para poder usar a função sleep, que fará o programa "pausar" por um tempo.
import time

# Iniciamos um laço de repetição (loop) com o comando 'for'. Ele vai contar de 10 até 0.
# A função range(10, -1, -1) gera uma sequência de números: começa em 10, vai até -1 (não inclui o -1), e diminui de 1 a cada vez.
# O número que está no meio (o -1) é o "passo", que indica que a contagem será decrescente.
for c in range(10, -1, -1):
    # 'print(c)' imprime o número atual da contagem na tela. No começo, será 10, depois 9, e assim por diante.
    print(c)
    
    # A função time.sleep(1) "pausa" o programa por 1 segundo.
    # Isso é feito para dar uma sensação de contagem regressiva, como se fosse um relógio que demora um segundo para mostrar o próximo número.
    time.sleep(1)

# Quando a contagem chega a 0, o laço 'for' termina e o programa imprime uma mensagem final.
# Nesse caso, a mensagem é de felicitações para o Ano Novo.
print("Feliz ano novo, partiu aglomerar?")
