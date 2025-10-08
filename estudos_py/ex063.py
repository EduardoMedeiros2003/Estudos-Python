maior= menor = 0
listatun =[]
for c in range(0,5):
    listatun.append(int(input(f'Digite um número na posição {c}: ')))
    if c==0:
        maior = menor = listatun[c]
    else:
        if listatun[c] > maior:
            maior = listatun[c]
        if listatun[c] < menor:
            menor = listatun[c]

    
print('=-'*20)
print(f'Os números digitados foram = {listatun}')
print(f'O maior número digitado foi de {maior} e sua posição foi de ', end='')
for i, v in enumerate(listatun):
    if v == maior:
        print(f'{i}...')
print(f'O menor número digitado foi de {menor} e sua posição foi de ', end='')
for i,v in enumerate(listatun):
    if v == menor:
        print(f'{i}...')
print('FIM')