import moeda

num = float(input('Informe um valor em real: R$'))
print(f'A metade de {moeda.moeda(num)} é R${moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é R${moeda.dobro(num, True)}')
print(f'Aumentando 10% de {moeda.moeda(num)} temos {moeda.aumentar(num,10, True)}')
print(f'Diminuindo 15% de {moeda.moeda(num)} temos {moeda.diminuir(num,15, True)}')