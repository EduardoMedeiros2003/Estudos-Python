# programa do jogo de par ou impa!
from random import randint
vitorias = v = 0
while True:
    jogador = int(input('Diga um valor (1 a 10): '))
    if jogador == 0:
        break
    computador = randint(1,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpa?[P/I]: ')).strip().upper()[0]
    print(f'Jogador:{jogador}\nComputador:{computador} \nTotal:{total}')
    print('Deu PAR' if total %2 ==0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            v+=1
            print(f'Você VENCEU!!')
        else:
            print(f'Você PERDEU!')
            break

    elif tipo == 'I':
        if total %2 == 1:
            v += 1
            print(f'Você GANHOU!')
        else: print(f'Você PERDEU!')
        break
    print('Vamos Jogar NOVAMENTE... ')

print(f'Você teve {v} Vitorias e 1 Derrota!')
print('FIM')
