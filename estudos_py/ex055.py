tot18= totH = totM20 =0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    continua = ' '
   
    if idade >= 18:
        tot18 += 1
    if sexo =='M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1

    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        print('-' * 30)
        print('      CADASTRE UMA PESSOA')
        print('-' * 30)
    if continua == 'N':
        print('====== FIM DO PROGRAMA ======')
        break

print(f'Ao todo tem: {tot18} pessoas a cima ou igual a 18 anos')
print(f'No total temos {totH} Homens cadastrados')
print(f'E temmos {totM20} Mulheres com menos de 20 anos')

print('Acabou')