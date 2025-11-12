def fatorial(n,show=False):
    '''
    n = Pede um número para o fatoramento.
    s = pergunta se quer ver o fatoramento completo do número. Se não so mostra o número final
    CRIADO POR: Eduardo Medeiros
    '''
    s = 0
    f = 1
    for c in range(num, 0 , -1):
        if show == 'S':
            print(c, end='')
            if c > 1:
                print('x', end='')
            else:
                print('=', end='')
        f *= c
    print(f'{f}')
   


num = int(input('Digite um número: '))
show = str(input('Quer mostrar todo o fatoramento? [S/N]: ')).upper()[0]

fatorial(num, show)
#help(fatorial)

print('FIM')