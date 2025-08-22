#Analisa se o ano é bissexto ou nao
from datetime import date
ano = int(input('Qual ano quer analisar? digite 0 para ser o ano atual: '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto') 