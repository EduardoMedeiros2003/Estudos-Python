print('-'*30)
print('       LOJA SUPER BARATÃO')
print('-'*30)
total = cima1000 = menor = cont =0
nomemenor = ' '

while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        cima1000 +=1
    if cont == 1 or preco < menor:
        menor = preco
        nomemenor = nome
    continua = ' ' # quando passa aqui de novo ele volta a ser nulo, se tiver fora do while ele sempre vai ter o 'S' e não vai parar 
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        print('====== FIM DO PROGRAMA ======')
        break

print(f'O Preço total da sua compra foi de R${total:.2f} Reais')
print(f'Você teve {cima1000} compras a cima de R$1000')
print(f'O produto mais barato foi {nomemenor} de valor de R${menor} Reais')
print(f'')

print('Fim do programa')
