#
from datetime import date

atual = date.today().year #Pegando o ano atual
nasceu = int(input('Ano de nascimento: '))
sexo = input('Você é homem ou mulher? (h)Homem (m)Mulher\n: ')

idade = atual - nasceu

print(f'Quem nasceu em {nasceu} tem {idade} anos, em {atual}')
if idade == 18 and sexo == 'h':
    print(f'Você tem que se alistar o qaunto antes')
elif idade < 18 and sexo == 'h':
    saldo = 18  - idade
    print(f'Ainda faltam {saldo} anos, para se alistar')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade > 18 and sexo == 'h':
    saldo = idade - 18
    print(f'Você deveria ter se alistado a {saldo} anos.')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}.')
elif sexo == 'm':
    print('Você não precisa se alistar')