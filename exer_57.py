""" Melhore o jogo do exer_28 onde o computador vai gerar 
um numero aleatório entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final 
quantos palpites foram necessário para vencer"""

from random import randint

# de acordo com o Copilot, seria interessante começar as variaveis com valor nulo, como None ou 0
num_user = (int(input('digite um numero de 0 a 10: \n')))
num_pc = randint(0, 10)
tentativas = 0

# nessa parte o professor escolheu usar uma variável booleana para usar como condicional
# 'acertou = false'
# while not acertou:
# acredito que não seja tão necessário
while num_user != num_pc:
    print('o número escohido pelo computador foi {} '
          'enquanto o seu foi {} '
          '\ntente novamente'.format(num_pc,num_user))
    num_pc = randint(0, 10)
    num_user = (int(input('digite um numero de 0 a 10: \n')))
    tentativas += 1

print(f'Parabens, você e a maquina escolheram o mesmo número \n foram necessárias {tentativas} tentativas.')

 """ 
 ainda estou tendo certas dificuldades com relação a trabalhar as variáveis dentros laço while
 acredito que com mais alguns exercícios fique mais habituado
 """