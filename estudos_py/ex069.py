pessoas = []
pesos = []
lista = []
mai = men = 0
cont = 0
while True:
    # Assim ficou bem mais organizado mas nem deve ser assim q era para fazer o desafio
    pessoa = str(input('Digite um nome para a lista: '))
    peso =float(input('Digite seu peso: '))
    lista.append([pessoa, peso])
    pessoas.append(pessoa)
    pesos.append(peso)
    if len(lista) == 1:
        mai = men = peso
    else:
        if peso > mai:
            mai = peso
        if peso < men:
            men = peso

    resp = str(input('Digite se quer continuar ou não: [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
# fazer uma atualização para mostra quem é o mais pesado e o mais leve ou mostra em ordem 
print('=-'*30)
print(f'Ao todo foram {len(lista)} pessoas cadastradas')
print(f'Aqui está todos cadarstados: {lista}')
print(f'Todas as pessoas cadrastadas: {pessoas}')
print(f'O peso de todos: {pesos}')
print(f'Os maiore pesos foram: {mai}KG. Peso de: ', end='')
for p in lista:
    if p[1] == mai:
        print(f'{p[0]} ')
print(f'Os menores peso foram: {men}KG. Peso de:  ', end='')
for p in lista:
    if p[1] == men:
        print(f'{p[0]} ')

print('Fim')