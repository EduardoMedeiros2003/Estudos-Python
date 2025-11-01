def soma(a, b):
    s = a + b
    print('-'*15)
    print(f'{a} + {b} = {s}')
    
soma(2,3)
soma(9,5)
soma(4,3)

#Empacotamento
def contador(* num):
   tam = len(num)
   print(f'Recebi os valores de: {num}. E foram {tam}.', end='')
   print()
   
contador(1,2,3,4,5,6,7,8,9)
contador(2,3,5,6,7,9)

def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos]*=2
        pos += 1

valores=[2,3,4,5,6,7,8,9,10]
print(valores)
dobra(valores)
print(valores)

def soma2(*valores2):
    adicao = 0
    for num in valores:
        adicao += num
    print(f'Somando os valores: {valores2} temos {adicao}')

soma2(5,2)
soma2(8,2)
soma2(2,9)