casa = float(input('Digite o valor da casa que pretende compra: R$'))
salario = float(input('Informe seu salário: R$ '))
anos = int(input('Em quantos anos pretende pagar a casa:'))

prestacao = casa / (anos * 12)

porcentagem = salario * 30/100  

if prestacao >= porcentagem:
    print('Você não podera pagar pela casa!')
else:
    print('Parabnes você vai poder pagar pela casa')

print(f'Para pagar uma casa de R${casa} em {anos} anos', end=". ")
print(f'A prestação é de {prestacao:.2f}')

print('Comparando a porsentagem da prestação')
print(f'{prestacao} Prestação {porcentagem} porcentagem do salário')
