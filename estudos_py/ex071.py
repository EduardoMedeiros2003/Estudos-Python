matris0 = []
matris1 = []
matris2 = []

for c in range(0,3):
    num = int(input(f'Digite um valor para [{0,c}]: '))
    matris0.append(num)

for c in range(0,3):
    num = int(input(f'Digite um valor para [{1,c}]: '))
    matris1.append(num)

for c in range(0,3):
    num = int(input(f'Digite um valor para [{2,c}]: '))
    matris2.append(num)

print('=-'*30)
for a in matris0:
    print(f'[{a}]', end='')
print()

for s in matris1:
    print(f'[{s}]', end='')
print()

for d in matris2:
    print(f'[{d}]', end='')
