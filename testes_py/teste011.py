import uteis
    
num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)# aqui joga o valor em uma 
dobro = uteis.dobro(num)
triplo = uteis.triplo(num)

print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {dobro}')
print(f'O triplo de {num} é {triplo}')