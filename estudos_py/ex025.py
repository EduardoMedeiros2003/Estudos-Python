r1 = float(input('Digite um comprimento de retas em CM: '))
r2 = float(input('Digite outro comprimento de retas em CM: '))
r3 = float(input('Digite outro comprimento de retas em CM: '))


verifica = r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2


if verifica:
    print('As retas podem formar um triângulo')
    if r1 == r2 ==r3:
        print('O triângulo vai ser um Equilátero')
    elif r1 != r2 !=r3 != r1:
        print('O triângulo vai ser um Escaleno')
    else:
        print('O triângulo vai ser um Isósceles')
else:
    print('As retas NÃO pode formar um triângulo')

# #if verifica and r1 == r2 ==r3:
#     print('As retas podem formar um triângulo!')
#     print('O triângulo vai ser um Equilátero')
# elif verifica and r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
#     print('As retas podem formar um triângulo!')
#     print('O triângulo vai ser um Isósceles')
# elif verifica and r1 != r2 !=r3 != r1:
#     print('As retas podem formar um triângulo!')
#     print('O triângulo vai ser um Escaleno')