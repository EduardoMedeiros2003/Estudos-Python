salario = float(input('Digite quanto tem na conta para poder gastar no mês: R$'))
total_gastos = 0  

while True:
    pagar = float(input('Informe valor do gasto: R$'))
    total_gastos += pagar  

    verifica = str(input('Tem outros gastos? [S/N]: ')).strip().upper()[0]
    if verifica == 'N':
        break  

resto = salario - total_gastos

print(f'Você tem R${salario:.2f} e tem uma dívida de R${total_gastos:.2f}.')
print(f'O que vai sobrar é R${resto:.2f}.')
