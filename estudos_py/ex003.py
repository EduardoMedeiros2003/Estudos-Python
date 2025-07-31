# media de um aluno
n1 = int(input('Digite sua primeira nota: '))
n2 = int(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

print(f'Sua media foi: {media}')

#taboada

def mostra_tabuada(numero):
    for i in range(1,11):
        print(f'{numero} X {i} = {numero * i}')


num = int(input('Digite um número: '))
mostra_tabuada(num)