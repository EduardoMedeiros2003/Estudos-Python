jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Qauntos jogos o jogador {jogador["nome"]} participou?: '))
if jogador['partidas'] > 0:
    for i in range(jogador['partidas']):
        gol = int(input(f'Qauntos gols {jogador["nome"]} fez na partida {i+1}: '))
        gols.append(gol)

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print(jogador)
print('-='*30)
print(f"O jogador {jogador['nome']} fez um total de {jogador['total']} gols nas {jogador['partidas']} partidas.")
print('-='*30)
for k, v in jogador.items():
    print(f'-> o campo {k} tem o valor {v}.')
print('-='*30)
print(f'O campo nome tem valor {jogador["nome"]}')
print(f'O campo gols tem valor {jogador["gols"]}')
print(f'O campo total tem valor {jogador["total"]}')
print('-='*30)
for i in range(jogador['partidas']):
    print(f'-> Na partida {i}. fez {jogador["gols"]}.')