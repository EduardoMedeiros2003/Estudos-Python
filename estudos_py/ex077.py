from datetime import date
ano_atual = date.today().year

dados = {}
dados['nome'] = str(input('Digite seu nome: '))
dados['ano_nascimento'] = int(input('Digite seu ano de nascimento: '))
dados['idade'] =  ano_atual - dados['ano_nascimento']
dados['carteira_de_trabalho'] = int(input('Digite o número da carteira de trabalho:[0 para sair]: '))

if dados['carteira_de_trabalho'] !=0:
    dados['ano_de_contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    print('Analisando...')
else:
    print('Analisando...')

print(dados)

print('-='*30)
print(f'nome tem valor: {dados["nome"]}')
print(f'Idade tem valor: {dados["idade"]}')
print(f'Carteira de trabalho: {dados["carteira_de_trabalho"]}')

if dados['carteira_de_trabalho'] == 0:
    print('Não teve contrato assinado.')
else:
    aponsentadoria = dados["idade"] + 35
    print(f'Contratação: {dados["ano_de_contratacao"]}')
    print(f'Sua aposentadoria você tera uma idade de : {aponsentadoria}')

#com quantos anos vai se aposentar 35 anos de colaboração
# ano que começou
