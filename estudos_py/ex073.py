from random import randint
from time import sleep
lista = list()
jogos = list()
print('-='*30)
print('                    JOGA NA MEGA SENA')
print('-='*30)
qaunt = int(input('Qauntos jogos você quer fazer?: '))
tot = 1
while tot<= qaunt:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista: #enquanto num não esta na lista coloque na lista 
            lista.append(num)
            cont += 1
        if cont >= 6:# se o contador chegar a 6 é para parar 
            break
    lista.sort()# vai deixar os números cresentes
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-='*3,f'Sorteando os {qaunt}', '-='*3)
sleep(1)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
print('Boa sorteee!!')
