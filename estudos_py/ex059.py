times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Bahia', 'Botafogo',
    'Atlético Mineiro', 'Ceará', 'Corinthians', 'Fluminense',
    'Fortaleza', 'Grêmio', 'Internacional', 'Red Bull Bragantino',
    'Santos', 'São Paulo', 'Sport', 'Vasco da Gama', 'Mirassol',
    'Juventude')
print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Primeiros 5 colocados:{times[0:5]}')
print('-='*15)
print(f'Os ultimos colocados: {times[-4:]}')
print('-='*15)
print(f'Todos os times em ordem alfabética:{sorted(times)}')
print('-='*15)
print(f'O sport está na {times.index("Sport")+1} posição!')