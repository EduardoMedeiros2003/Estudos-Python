jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
partidas.append(jogador.copy())

print('-=')* 30