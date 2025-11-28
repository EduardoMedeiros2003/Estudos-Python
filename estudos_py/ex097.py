from interface import*
from arquivo import*
from time import sleep

arq = 'dadospessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        #Opção para ler o arquivo da base de dados
        lerArquivo(arq)
    elif resposta == 2:
        #Cadrasta novas pessoas a lista de dados
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade:')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        #Sai do sistema
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        cabecalho('ERRO! Digite uma opção válida!')
    sleep(1)

   