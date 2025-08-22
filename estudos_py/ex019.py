#while = enquanto

from random import randint
from time import sleep
numero_secreto = randint(0 , 10)
print('Tente adivinhar um numero de 0 a 10:')
num = int(input('Digite um número: '))
print('Procesando...')
sleep(1)
if num == numero_secreto:
    print(f'Acertou o número, muito bem')
else:
    print(f'O número esta errado, era {numero_secreto} e não {num}')
