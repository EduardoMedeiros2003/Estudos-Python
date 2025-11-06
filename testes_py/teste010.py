def fatorial(num=1):
    f = 1
    for c in range(num, 0 , -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(9)
f3 = fatorial(4)
f4 = fatorial()

print(f'Os resultados são {f1}, {2}, {3}, e {4}')

def par(n=0):
    if n%2== 0:
        return True
    else:
        return False
    
num= int(input('Digite um número: '))
if par(num):
    print('É um número par!')
else:
    print('É um número ímpar')