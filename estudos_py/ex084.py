
def maior(* num):
    maior = cont = 0
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    # Poderia descobri qauntos números tem pelo cont 
    print(f'. Ao todo foram passados: {len(num)} números')
    print(f'O maior valor é: {maior}')
    print('-='*35)

maior(1,2,3,4,5)
maior(6,3,8,1)
maior(0)
maior(2)
maior(23,57,12,69,42,49)