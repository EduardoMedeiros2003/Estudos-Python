def aumentar(num=0, taxa=0, formato = False):
    res = num + (num* taxa/100)
    return res if formato is False else moeda(res)

def diminuir(num=0, taxa=0, formato = False):
    res = num - (num* taxa/100)
    return res if formato is False else moeda(res)

def dobro(num=0, formato = False):
    res = num * 2
    return res if formato is False else moeda(res)

def metade(num=0, formato = False):
    res = num / 2
    return res if formato is False else moeda(res)

def moeda(num=0, moeda ='R$',):
    return f'{moeda}{num:.2f}'.replace('.',',') # Retrona R$ valor e troca todo o '.' por ','

def resumo(num=0,taxaa=0,taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(num):>10}')
    print(f'Dobro do preço  : \t{dobro(num,True):>10}')
    print(f'Metade do valor : \t{metade(num,True):>10}')
    print(f'{taxaa}% de aumento :\t{aumentar(num,taxaa, True):>10}')
    print(f'{taxar}% de redução : \t{diminuir(num,taxar, True):>10}')
    print('-'*30)

def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print('ERRO: é um valor invalido!')
        else:
            valido = True
            return float(entrada)
#falta o tratamento de erro se for com int e str no input