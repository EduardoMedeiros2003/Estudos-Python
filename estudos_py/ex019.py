#while = enquanto
from random import randint
from time import sleep
tentativas = 1
num = -1 # tem que fazer essa pequena gambiarra para fazer o while rodar
numero_secreto = randint(0 , 10) 
while num != numero_secreto:
    print('Tente adivinhar um numero de 0 a 10:')
    num = int(input('Digite um número: '))
    print('Procesando...')
    sleep(0.5)
    if num == numero_secreto:
        print(f'Acertou o número, muito bem {num} é {numero_secreto} são iguais!')
        print(f'Você acertou em {tentativas} tentativas!')
    else:
        tentativas += 1
        print('Você errou!\nTente novamente!')
        if num < numero_secreto:
            print('O número secreto é MAIOR!')
        else:
            print('O número secreto é MENOR!')

print('FIM')
