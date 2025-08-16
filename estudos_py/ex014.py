import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Treceiro aluno: '))
n4 = str(input('Qaurto aluno: '))

lista = [n1,n2,n3,n4] #Listas se usa []

escolhido = random.choice(lista) #Um escolhido

print(f'O escolhido foi {escolhido}')

random.shuffle(lista) #Enbarailhando a lista

print('A ordem da apresentação será ')
print(lista)
