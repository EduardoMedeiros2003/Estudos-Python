# um numero dividido por 2 e o resto é 0 ele é par
num = int(input('Digite um número: '))

if num % 2==0 :
    print(f'O número {num} é PAR')
else: print(f'O número {num} ÍMPAR')

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verifica o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor =c   
#Verificando o maior
maior = a
if b> a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor valor digitado foi: {menor}')
print(f'O maior valor digitado foi: {maior}')