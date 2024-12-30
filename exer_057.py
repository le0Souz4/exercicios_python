""" Melhore o jogo do exer_28 onde o computador vai gerar 
um numero aleatório entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final 
quantos palpites foram necessário para vencer"""

# Importa a função randint da biblioteca random, que será usada para gerar números aleatórios
from random import randint

# Inicializa as variáveis necessárias
# Solicita ao usuário que digite um número entre 0 e 10, e já o converte para inteiro
num_user = int(input('Digite um número de 0 a 10: \n'))

# Gera um número aleatório entre 0 e 10 para o computador
num_pc = randint(0, 10)

# Inicializa o contador de tentativas como 0
tentativas = 0

# Estrutura de repetição para verificar se o número escolhido pelo usuário é diferente do número do computador
while num_user != num_pc:
    # Mostra ao usuário o número escolhido pelo computador e informa que os números não coincidem
    print('O número escolhido pelo computador foi {} '
          'enquanto o seu foi {} '
          '\nTente novamente'.format(num_pc, num_user))
    
    # Gera um novo número aleatório para o computador
    num_pc = randint(0, 10)
    
    # Solicita um novo número ao usuário
    num_user = int(input('Digite um número de 0 a 10: \n'))
    
    # Incrementa o contador de tentativas
    tentativas += 1

# Quando os números coincidirem, o programa sai do laço e exibe uma mensagem de sucesso
print(f'Parabéns, você e a máquina escolheram o mesmo número! Foram necessárias {tentativas} tentativas.')

"""
Notas adicionais:
- A variável `tentativas` é usada para contar quantas vezes o usuário precisou tentar até acertar.
- O método `randint(0, 10)` garante que o computador escolha um número entre 0 e 10 de forma aleatória a cada tentativa.
- Não é necessário usar uma variável booleana como no exemplo comentado do professor, já que o laço `while` com a condição `num_user != num_pc` é suficiente para controlar a repetição.
"""

"""
Ainda estou tendo certas dificuldades com relação a trabalhar as variáveis dentro do laço while.
Acredito que com mais alguns exercícios, ficarei mais habituado.
"""
