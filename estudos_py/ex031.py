from datetime import date

atual = date.today().year #Pegando o ano atual

ano = int(input('Informe o ano do seu nascimento: '))

idade = atual - ano

if idade <= 9:
    print(f'Você é um atleta MIRIM com uma idade de :{idade}')
elif idade <=14:
    print(f'Você é um atleta INFANTIL com uma idade de :{idade}')
elif idade <=19:
    print(f'Você é um atleta JUNIOR com uma idade de :{idade}')
elif idade <= 25:
    print(f'Você é um atleta SÊNIOR com uma idade de :{idade}')
elif idade > 25:
    print(f'Voê é um atleta MASTER com uma idade de :{idade}')
