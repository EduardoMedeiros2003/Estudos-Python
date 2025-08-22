velo = float(input('Digite a quantos KM esta seu carro: '))
if velo > 80:
    exesso = velo - 80
    muta = exesso * 7
    print(f'Seu carro esta a cima da velocidade permitida de 80km, você esta a {velo}KM')
    print(f'Teve uma multa de :{muta}$')
else: 
    print('Você esta em boa velocidade!')
