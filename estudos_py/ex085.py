from random import randint

def sorteia(lista):
    print(f'Os números sorteados foram: ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ')
    print('FIM!')
    
def somap(lista):
    pares = []
    soma = 0
    for valor in lista:
        if valor %2 ==0:
            soma += valor
            pares.append(valor)
    print(f'Lista sorteada: {lista}')
    print(f'temos os números pares: {pares}, e a soma de todos é: {soma}')
        
#Programa principal 
print('-='*50)
numero = list()
sorteia(numero)
somap(numero) 
print('-='*50)
