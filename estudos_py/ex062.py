mercadorias = (
    ('Lápis', 1.50),
    ('Caderno', 15.00),
    ('Borracha', 2.00),
    ('Mochila', 120.00),
    ('Caneta', 3.50),
    ('Livro', 45.00),
    ('Estojo', 25.00),
    ('Régua', 4.00),
    ('Apontador', 3.00),
    ('Agenda', 20.00)
)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for item, preco in mercadorias:
    print(f'{item:.<30} R$ {preco:>7.2f}') # espaço para aparecer
print('-' * 40)

