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
    print(f'Preço analisado: {moeda(num)}')
    print(f'Dobro do preço: {dobro(num,True)}')
    print(f'Metade do valor: {metade(num,True)}')
    print(f'{taxaa}% de aumento:{aumentar(num,taxaa, True)}')
    print(f'{taxar}% de redução : {diminuir(num,taxar, True)}')
    print('-'*30)