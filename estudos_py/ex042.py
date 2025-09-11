from datetime import date

atual = date.today().year
totalmaior = 0
totalmenor = 0

for pess in range(1,8):
    nasc = int(input(f'Em qual ano a {pess}º pessoa nasceu? '))
    idade = atual - nasc

    if idade >= 18:
        totalmaior += 1 
        print(idade)
    else:
        totalmenor += 1
        print(idade)

print(f'Ao todo tivemos {totalmaior} pessoas maiores de idade!')
print(f'Ao todo tivemos {totalmenor} pessoas menores de idade!')
