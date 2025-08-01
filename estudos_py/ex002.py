#Contas

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f'A soma é {s},\n Produto é {m},\n Divisão é {d:.3f}')
print(f'A divisão inteira {di},\n Elevado {e}')

n3 = int(input('Digite um número para lhe mostra seu antecessor e seu sucessor: '))
n4 = n3 + 1
n5 = n3 - 1
print(f'Analisando o valor: {n3}, seu antecessor é: {n5} e o sucessor é: {n4}.')

n6 = int(input('Digite um número para lhe mostra seu doblro, triplo e raiz quadrada: '))
n7 = n6 * 2
n8 = n6 * 3
n9 = n6 ** (1/2)

print(f'O dobro de {n6} vale {n7}.')
print(f'O triplo de {n6} vale {n8}.')
print(f'A raiz de {n6} vale {n9:.2f}.')