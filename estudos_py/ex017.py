cidade = input('Em qual Cidade você nasceu: ').strip().upper()

partes = cidade.split()# vai dividir o nome da cidade

if partes[0]== 'SANTOS':
    print('A cidade começa com SANTOS!!')
else: 
    print('A cidade NÃO começa com SANTOS')

nome = input('Digite seu nome completo: ').upper()

parte_nome = nome.split()

if 'SILVA' in parte_nome:
    print('Seu nome tem Silva')
else:
    print('Seu nome não tem Silva') 

frase = input('Digite uma frase: ').lower().strip()
conte = frase.count('a')
primeira = (frase.find('a')+1)# vai ser o primeiro que aparecer,o (+1) é para ajustar para nos o ínicio
ultima = (frase.rfind('a')+1)# vai pegar o (r) da direita right,o (+1) é para ajustar para nos o ínicio
print(f'A letra (a) aparece {conte} vezes na frase')
print(f'A primeira vez qeu o (a) aparece é na posição: {primeira}')
print(f'O ultimo (a) aparece na posição: {ultima}')

nome = input('Digite seu nome completo: ').strip()
divisao = nome.split()#divisão por espaços
primeiro = divisao[0]
ultimo = divisao[-1]#-1 pega o último nome digitado
print(f'Seu primeiro nome é: {primeiro}')
print(f'Seu último nome é: {ultimo}')
