from datetime import date

def voto(ano):
    atual = date.today().year
    idade = atual - ano
    print(f'Com idade de: {idade}.', end=' ')
    if idade >= 18 and idade < 65:
        print('Voto Obrigatorio.')
    elif idade >= 65:
        print('Voto Opcional.')
    else:
        print('Não vota.')

voto(int(input('Qual foi o ano do seu nacsimento? ')))
