import moeda

num = float(input('Informe um valor em real: R$'))
print(f'A metade de {moeda.moeda(num)} é R${moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é R${moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando 10% de {moeda.moeda(num)} temos {moeda.moeda(moeda.aumentar(num,10))}')
print(f'Diminuindo 15% de {moeda.moeda(num)} temos {moeda.moeda(moeda.diminuir(num,15))}')