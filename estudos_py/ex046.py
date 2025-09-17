n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
menu = 0

while menu != 5:
    menu = int(input('[1]Soma\n[2]Multiplica\n[3]Maior\n[4]Novos Números\n[5]Sair do porgrama\nQual é a opção desejada: '))
    
    if menu == 1:
        print(f'A soma de {n1} e {n2} foi {n1 + n2}')
        print(f'{n1} + {n2} = {n1 + n2}')
    elif menu == 2:
        print(f'O produto de {n1} e {n2} foi {n1 * n2}')
        print(f'{n1} X {n2} = {n1 * n2}')
    elif menu == 3:
        if n1 > n2:
            print(f'O número maior é: ',n1)
        else:
            print(f'O número maior é: {n2}')
    elif menu == 4:
         n1 = int(input('Digite um valor: '))
         n2 = int(input('Digite outro valor: '))
    elif menu == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente: ')
    print('='*20)

   
print('Fim do programa')

