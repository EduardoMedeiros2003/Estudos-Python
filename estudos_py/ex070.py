lista = []
par = []
impa = []
for c in range(0,7) :
    num = (int(input(f'Digite o {c+1}. Valor: ')))
    lista.append(num)

    if num %2 == 0:  # No if tem que ser uma variavel, não tem como fazer com a propria lista
        par.append(num)
    else:
        impa.append(num)

lista.sort()
par.sort()
impa.sort()

print(f'Toda lista digitada foi: {lista}')
print(f'Os números pares digitados foram: {par}')
print(f'Os números ímpares digitados forram: {impa}')
