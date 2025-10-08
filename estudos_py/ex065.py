lista = []
par = []
impar = []

while True:
   num = int(input('Digite um número para a lista: '))
   lista.append(num)
   resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

   if num %2 == 0:
    par.append(num)
   else:
    impar.append(num)

    if resposta == 'N':
        break

print(f'-='*30)
print(f'Os números digitados foram: {lista}')
print(f'Os números pares digitados foram :{par}')
print(f'Os números impares digitados foram {impar}')
print('FIM')