dados =  {'nome':'Eduardo', 'idade': 22}
print(dados['nome'])
print(dados['idade'])
filme = {'Titulo':'Homem de ferro',
         'ano': 2003,
         'Diretor': 'Cara de chapeu'}

print(filme.values())# values é um metodo entao tem que ter o () no final // Parte de cima
print(filme.keys())# keys outro metodo que tem os () no final // parte de baixo - nome das variaveis do dicionario
print(filme.items())# mostra tudo // tudo pode usar nos for

for k, v in filme.items():
    print(f'{k} : {v}')


print(dados['nome'])
print(f'O {dados["nome"]} tem {dados["idade"]}')
print(dados.items())
dados['peso'] = 80.5

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(f'{brasil} esse é do print')
for e in brasil:# para a lista
    print(e)

for e in brasil:
    for v in e.values():
        print(v,end=' ')