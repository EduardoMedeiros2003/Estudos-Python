print('Digite um número. Para sair digite 999:')
cont = n = soma = 0
n = int(input('Digite um número: '))# assim nao faz elel contar o flag 999 para sair
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número: '))#lendo o flag da ultima linha faz o codigo nao ler ele para a soma

print(f'Voê digitou {cont} números e a soma deles foi {soma}')
        