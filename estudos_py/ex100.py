compras = []        # Lista que guarda (nome, valor)
valor_total = 0     # Acumulador

total_compras = int(input('Quantas compras deseja registrar? '))

for i in range(1, total_compras + 1):
    nome = input(f'Nome da compra {i}: ')
    valor = float(input(f'Valor da compra {i}: R$ '))
    
    compras.append((nome, valor))  # salva nome e valor
    valor_total += valor           # soma 

print('-' * 40)
print('LISTA DE COMPRAS:')

for nome, valor in compras:
    print(f'- {nome}: R$ {valor:.2f}')

print('-' * 40)

# DESCONTO
cartao = input('Possui cartão da loja? [S/N]: ').strip().upper()

if cartao == 'S':
    desconto = valor_total * 0.10   # 10% de desconto
    valor_final = valor_total - desconto
    print(f'Desconto aplicado: R$ {desconto:.2f}')
else:
    valor_final = valor_total

print(f'Valor total a pagar: R$ {valor_final:.2f}')
