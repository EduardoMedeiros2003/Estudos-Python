def fatorial(n,s):
    '''
    n = Pede um número para o fatoramento.
    s = pergunta se quer ver o fatoramento completo do número. Se não so mostra o número final
    CRIADO POR: Eduardo Medeiros
    '''
    f = 1
    for c in range(num, 0 , -1):
        if show:
            print(c, end='')
            if c > 1:
                print('x', end='')
            else:
                print('=', end='')
        f *= c
    print(f'{f}')
    print(f'{n}, {s}')


num = int(input('Digite um número: '))
show = str(input('Quer ver o fatoramento? '))
fatorial(num, show= True)
help(fatorial)