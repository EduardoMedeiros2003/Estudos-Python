# Condicional if, else | se , se nao
tempo = int(input('Digite quanto tempo tem seu carro: '))
if tempo <=5:
    print('Seu carro é novo!')
else: 
    print('Seu carro ja esta velho!')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1+n2)/2
print(f'Sua média foi: {media:.1f}')
if media < 7:
    print('Você esta de recuperação')
else: print('Você passou de ano.')