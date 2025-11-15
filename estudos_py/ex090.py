def notas(*n, sit=False):
    '''
    -> Vai ler qauntos números for preciso para fazer a media da sala
    -> Vai fazer um cauculo da média e mostra ela
    -> E vai indentificar se a média da turma esta boa ou não
    '''
    r = dict()#Dicionario
    r['Total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)

    if sit:
        if r['media'] >=7:
            r['situacao'] = 'BOA'
        elif r ['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUM'
    
    return r

def linha():
    print('-'*56)

#Programa principal
linha()
print('        Analisando notas de Alunos!')
linha()
#Pergunta se vai querer mostra a critica da turma
critica = str(input('Quer ter o retorno da Situação dos alunos?: [S/N]: ')).strip().upper()[0]
sit = True if critica == 'S'else False

#lendo as notas
valores = []
aluno = 1

#Laço de repetção para ir lendo as notas e perguntando se tem mais notas para ser adicionadas
while True:
    nota = float(input(f'Infome a nota do aluno {aluno}: '))
    valores.append(nota)
    aluno += 1
    rep = str(input('Deseja adicionar outra nota de aluno?: [S/N]: ')).strip().upper()[0]
    if rep == 'N':
        break

#Chamando a função com desempacotamento
resp = notas(*valores,sit=sit)
linha()
print('Resultados Da Análise')
print(resp)
linha()
