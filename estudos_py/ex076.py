from random import randint
from time import sleep

jogo = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}

print('Valores sorteados:')
for jogador, valor in jogo.items():
    print(f'{jogador} tirou {valor} no dado.')
    sleep(0.1)

print('-=' * 20)

ranking = sorted(jogo.items(), key=lambda x: x[1], reverse=True)

# Mostrar o ranking
print('   🏆 Ranking dos jogadores 🏆')
for i, (jogador, valor) in enumerate(ranking):
    print(f'{i+1}º lugar: {jogador} com {valor}')
    sleep(0.5)
