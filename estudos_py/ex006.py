# algoritimo que pega o preço de um produto e coloca 5% de desconto | 0,05
p1 =(input('Digite o nome do produto que ira entra em promoção: '))
d1 = float(input('Digite o valor atual do produto: ')) 

desconto = d1 * 0.05

final = d1 - desconto

print(f'O produto que ira entra em desconto é {p1}, seu valor inicial é de: {d1}, com -{desconto} do desconto dos 5%, o valor final vai ser:{final}')