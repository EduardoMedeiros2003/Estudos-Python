km = float(input('Digite a distância da sua viagemem KM:'))
if km <= 200:
    curta = km * 0.5
    print(f'Sua passagem foi de :{curta:.2f}$')
else: 
    longa = km * 0.45
    print(f'Sua passagem foi de:{longa:.2f}$')
