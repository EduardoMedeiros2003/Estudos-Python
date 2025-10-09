dados = [['Pedro', 25], ['Carlos', 29], ['Lucas', 30]]

pessoas = list()

pessoas.append(dados[:])
pessoas.append(['Eduardo', 22])

print(dados)
print(pessoas)
print(dados[2][0])
for p in pessoas:
    print(p[0]) # outro metodo de mostra todos da lista

totmai = 0
totmen = 0

galera = []
dado = list()
for c in range(0,3):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Digite sua idade: ')))
    galera.append(dado[:])
    dado.clear()# Deleta o dado

for p in galera:
    if p [1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(galera)
print(dado)

print(f'Temmos {totmai} maiores de idade e {totmen} menores de idade.')
