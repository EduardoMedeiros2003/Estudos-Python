time = list()
jogador = dict()
partidas = list()
# Aqui esta pegando os dados e colocando na lista time, para ter varios jogadores
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
        jogador['gols'] = partidas[:]
        jogador['total'] = sum(partidas)
    time.append(jogador.copy()) # para copiar um dicionario em uma lista tem que ser assim
    
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N')
    if resp == 'N':
        break
# Aqui começa o codigo de mostra os resultados
print('-='*40)
print('COD ', end='')
for i in jogador.keys():
    print(f'{i:>15}', end='')
print()
print('-'*50)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
print('-'*50)
# Aqui vai mostra os dados dos jogadores individualmente

while True:
    busca = int(input('Digite o Cod do jogador: [999 para sair]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe valor com o Cod {busca} !')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR -> {time[busca]["nome"]}:' )
        # para listas se usa o enumerate
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')
