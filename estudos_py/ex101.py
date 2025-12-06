#Plano Cartesiano
x = float(input('Digite o valor de x: '))
y = float(input('Digite o valor de y: '))

if x > 0 and y > 0:
    print('Primeiro Quadrante')
elif x<0 and y>0:
    print('Segundo Quadrante')
elif x<0 and y<0:
    print('Terceiro Quadrante')
elif x>0 and y<0:
    print('Quarto Quadrante')
else:
    print('Na origem')

