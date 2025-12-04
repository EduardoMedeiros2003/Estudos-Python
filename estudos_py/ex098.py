preco_hamburgue = 12
preco_batata = 7
preco_refri = 5
print('-'*30)
print('--Cardapio da venda--')
print('Hamburguer: R$ 12')
print('Batata: R$ 7')
print('Refrigerante: R$ 5')
print('-'*30)
print('Informe 0 se Não for compra o produto')
quant_hamburguer = int(input('Quantidade de hamburguer: '))
quant_batata = int(input('Quantidade de batata: '))
quant_refri = int(input('Quantidade de refrigerante: '))
total_hamburguer = quant_hamburguer * preco_hamburgue
total_batata = quant_batata * preco_batata
total_refri = quant_refri * preco_refri
total = total_hamburguer + total_batata + total_refri
print(f'O total da compra foi: R${total}')