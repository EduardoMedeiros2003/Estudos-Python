lista = []
par = []
impar = []

while True:
    num = int(input('Digite um número para a lista: '))
    lista.append(num)

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

    resposta = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if resposta == 'N':
        break


print(f'-='*30)
print(f'Os números digitados foram: {lista}')
print(f'Os números pares digitados foram: {par}')
print(f'Os números ímpares digitados foram: {impar}')
print('FIM')
# 3 listas, uma mostra todos os números outra mostra os números pares e a última mostra os números ímpares
