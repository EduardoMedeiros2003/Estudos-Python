print('=' * 30)
print(f'           BANCO EDU')
print('=' * 30)

valor = int(input('Digite o valor que quer sacar: R$'))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0   # reinicia o contador de cédulas
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO EDU! Tenha um bom dia!')
