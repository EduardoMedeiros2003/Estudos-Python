from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('Suas opções é:\n[0] Pedra\n[1] Papel\n[2] Pedra')

jogador = int(input('Sua opção é: '))
print('-='*12)
print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')
print('-='*12)

# Fazer atualização para mostra quem ganha e quem perde 