jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Qauntos jogos o jogador{jogador["nome"]} participou?: '))
if jogador['partidas'] > 0:
    for i in range(jogador['partidas']):
        gol = int(input(f'Qauntos gols {jogador["nome"]} fez na partida {i+1}: '))
        gols.append(gol)

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print(jogador)
print('-='*30)
print(f"O jogador {jogador['nome']} fez um total de {jogador['total']} gols nas {jogador['partidas']} partidas.")