#Comversão do Real em Dolar
real = float(input('Quantos Reais você tem na carteira? R$:'))
dolar = real / 5.54
print(f'Com R$:{real}, você pode compra US$:{dolar:.2f} ')

real = float(input('Quantos Reais você tem na carteira? R$:'))
euro = real / 6.42
print(f'Com R$:{real}, você pode compra EU$:{euro:.2f} ')

real = float(input('Quantos Reais você tem na carteira? R$:'))
iene = real * 0.037
print(f'Com R$:{real}, você pode compra IENE$:{iene:.2f} ')