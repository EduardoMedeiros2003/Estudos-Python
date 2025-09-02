print('='*20)
print('LOJAS DO EDUARDO')
print('='*20)

valor = float(input('Preço das compras: R$ '))
print('Forma do pagamento')
condicao = int(input('[1] a vista dinheiro/cheque\n[2] a vista cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão\nQual é a opção? '))

if condicao == 1:
    efeito = valor - (valor * 0.10)
    print(f'O valor da compra foi de R${valor:.2f} e agora é de R${efeito:.2f}, desconto de 10%')
elif condicao == 2:
    efeito =  valor - (valor * 0.05)
    print(f'O valor de R${valor:.2f} e agora é de R${efeito:.2f}, desconto de 5%')
elif condicao == 3:
    efeito = valor / 2
    print(f'O valor é de R${valor:.2f}, e por mês vai pagar R${efeito:.2f}, sem juros')
elif condicao == 4:
    efeito = valor + (valor * 0.20)
    mes = int(input('Quantas parcelas? '))
    parcela = efeito / mes
    print(f'Sua compra será parcelada em {mes}X de {parcela:.2f}')
    print(f'O valor de R${valor:.2f} com um juros de 20% ficou a R${efeito:.2f}')
else:
    print('Opcão invalida. Tente novamente!')
