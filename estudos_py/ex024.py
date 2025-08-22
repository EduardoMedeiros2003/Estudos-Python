salario = float(input('Digite qual é seu salário atual: '))
if salario <= 1250:
     aumento = salario + (salario * 15 / 100)
     print(f'Seu novo salário é de:{aumento:.2f}$')
    
else:
    aumento = salario + (salario * 10 / 100)
    print(f'Seu novo salário é de:{aumento:.2f}$')      