livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    print(livro)
    if livro == 'O Hobbit':
        break

compra = int(input('Digite quantos livros quer compra: '))
estoque = 5
venda= estoque - compra
if venda < 0:
    print('Não temos essa qauntidade no estoque!')
while estoque > 0:
    estoque -= 1
    print(f'Venda realizada! Estoque restante: {estoque+1}')
print('Estoque esgotado')

for num in range(10,0,-1):
    if num %2 ==0:
        print(f'Faltam apenas {num} segundos -Não perca essa oportunidade!')
    else:
        print(f'A contagem continua: {num} segundos restantes!')

print('Aproveite a promoção agora!')

filmes = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2},
    {"nome": "Percy Jackson O ladrão de raios", "estoque": 1}
]

for filme in filmes:
    if filme["estoque"] == 0:
        continue
    print(f'Filme disponível: {filme["nome"]}')