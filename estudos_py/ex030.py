nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 +nota2) / 2

print(f'Com a primeira nota de {nota1} e a segunda de {nota2}, sua média é :{media}')
if media >= 7:
    print(f'Parabéns você está APROVADO com uma média de :{media}')
elif media >= 4 and media < 6.9:
    print(f'Você está de RECUPERAÇÃO, com uma média de :{media}')
else:
    print(f'Você está REPORVADO, com uma média de :{media}')