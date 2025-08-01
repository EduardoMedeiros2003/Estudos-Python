# media de um aluno
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

print(f'Sua media foi: {media:.1f}')

#taboada

def mostra_tabuada(numero):
    for i in range(1,11):
        print(f'{numero} X {i} = {numero * i}')


num = int(input('Digite um número para ver sua taboada: '))
mostra_tabuada(num)

n3 = int(input('Digite outro numero para a taboada: '))

print('--' *12)
print(f'{n3} X {1} = {n3 * 1}')
print(f'{n3} X {2} = {n3 * 2}')
print(f'{n3} X {3} = {n3 * 3}')
print(f'{n3} X {4} = {n3 * 4}')
print(f'{n3} X {5} = {n3 * 5}')
print(f'{n3} X {6} = {n3 * 6}')
print(f'{n3} X {7} = {n3 * 7}')
print(f'{n3} X {8} = {n3 * 8}')
print(f'{n3} X {9} = {n3 * 9}')
print(f'{n3} X {10} = {n3 * 10}')
print('--' *12)