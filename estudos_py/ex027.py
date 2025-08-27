num = int(input('Digite um número qualquer inteiro: '))
escolha = int(input('Digite:[1] para Binárion\nDigite:[2] para Octal\nDigite:[3] para Hexadecimal\nSua opção é: '))

if escolha == 1:
    print(f'{num} em Binário é {bin(num)[2:]}')
elif escolha== 2:
    print(f'{num} em Octal é {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} em Hexadecimal é {hex(num)[2:]}')
else:
    print('Opção inválida')