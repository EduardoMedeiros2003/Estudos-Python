# Verificador de limite de gastos do mês
def total():
    print(f'O total dos seus gastos por mês foi de {gasto}')

limite = 3000
gasto = 0
while True:
    gasto = float(input('Difite o gasto total do mês: R$'))
    gasto += gasto
    resp = str(input('Tem outro gasto para adicionar ao mês? [N/S]: ')).lower()[0]
    if resp == 'n':
        break

if gasto > limite:
    total()
    print(f'Atenção! Você ultrapassou o limite do orçamento de {limite}! ')
else:
    total()
    print(f'Você está dentro do limite adequado de {limite}!')