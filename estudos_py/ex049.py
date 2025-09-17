n = int(input("Quantos termos de Fibonacci você quer ver? "))

a, b = 0, 1
print("Sequência de Fibonacci:")

for _ in range(n):
    print(f'{a} -> ', end="")
    a, b = b, a + b

print('FIM')

n2 = int(input('Digite outra quantidade: '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} -> {t2}', end='')

while cont <= n2:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
    cont += 1

print('fim')