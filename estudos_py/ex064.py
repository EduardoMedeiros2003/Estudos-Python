num = []

while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Tente novamente!')

    cont = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break

num.sort()# ordenando os números
print('-='*20)
print(f'Você digitou estes números: {num}')
print('Fim do programa')