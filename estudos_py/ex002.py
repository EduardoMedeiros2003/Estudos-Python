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

n3 = int(input('Digite um número para lhe mostra seu anterior e seu antessesor: '))
n4 = n3 + 1
n5 = n3 - 1
print(n5, n3, n4)

n6 = int(input('Digite um número para lhe mostra seu doblro, triplo e raiz quadrada: '))
n7 = n6 * 2
n8 = n6 * 3
n9 = n6 ** 0.5

print(n6,n7,n8,n9)