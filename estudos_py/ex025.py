r1 = float(input('Digite um comprimento de retas em CM: '))
r2 = float(input('Digite outro comprimento de retas em CM: '))
r3 = float(input('Digite outro comprimento de retas em CM: '))

cont = r1 + r2 
verifica = cont > r3

if verifica:
    print('As retas podem formar um triângulo!')
else:
    print('As retas Não pode formar um triângulo')
