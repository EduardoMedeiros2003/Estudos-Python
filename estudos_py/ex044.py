
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for p in range(1,5):
    print(f'----- {p}º -----')
    nome = input('Nome:').strip()
    idade = int(input('Idade:'))
    sexo = input('Sexo [M/F]:').strip()
    somaidade = somaidade + idade
    if p ==1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade> maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1


mediaidade = somaidade / 4
print(f'A média das idades do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e seu nome é {nomevelho}.')
print(f'Ao todo são {totalmulher20} mulheres com menos de 20 anos.')
