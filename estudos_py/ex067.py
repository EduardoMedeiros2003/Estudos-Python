lista = []
while True:
    lista.append(int(input('Digite um número para a lista: ')))
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break

print('-='*30)
print(f'Foram digitados: {len(lista)} números')
lista.sort(reverse=True)# muda a variavel para o modo decrescente
print(f'Esta é a ordem dos números digitados em ordem decrescente:{lista}')
if 5 in lista:
    print('O valor 5 foi digitado e está na lista!')
else:
    print('O valor 5 não foi digitado e não está na lista!')
print(f'FIM')