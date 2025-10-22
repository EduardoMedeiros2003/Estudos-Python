aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
    print(f'O aluno: {aluno["nome"]} está {aluno["situacao"]}')
elif aluno['media'] > 4:
    aluno['situacao'] = 'Recuperação'
    print(f'O aluno: {aluno["nome"]} está em {aluno["situacao"]}')
else:
    aluno['situacao'] = 'Reprovado'
    print(f'O aluno: {aluno["nome"]} está {aluno["situacao"]}')

print('-='*30)
for k, v in aluno.items():
    print(f'-{k} é igual a {v}')