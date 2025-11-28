def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro!  Digite um número inteiro válido.\033[m')
            continue
    
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')

        else:
            return n

num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}') 