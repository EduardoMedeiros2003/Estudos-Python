def jogador(n,g):
    if n =='':
        n = '<JogadorDesconhecido>'
    if g == '':
        g = 0
    print(f'O nome do Jogador é: {n}')
    print(f'O Jogador {n}, fez {g} gol(s)')

nome = str(input('Digite o nome do Jogador: '))
gol = str(input('Digite qauntos gols o Jogador fez: '))
jogador(nome,gol)

def ficha(jog='<Desconhecido>', gou=0):
    print(f'O jogador {jog} fez {gou} gol(s) no campeonato.')

no = str(input('Nome do jogador: '))
go = str(input('Número de Gols: '))

if go.isnumeric():
    go = int(go)
if no.strip() == '':
    ficha(gou=go)
else:
    ficha(no, go)