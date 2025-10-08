lista = []

for i in range(5):
    num = int(input(f'Digite o {i+1}º número: '))
    
    # Se for o primeiro número ou maior que o último da lista, adiciona no final
    if i == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista!')
    else:
        # Encontra a posição correta para inserir o número
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Foi adicionado na posição {pos} da lista')
                break
            pos += 1

print('-=' * 20)
print(f'Os números digitados em ordem foram: {lista}')
