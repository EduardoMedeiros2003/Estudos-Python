num = [2,1,6,9,3]
num[2] = 3 # subistituiu o da posição
num.append(7)# adiciona o número no final da lista
num.sort(reverse=True)# muda a ordem da lista, os ultimos serao os primeiros
num.insert(2,0)# no lugar 2 coloca 0 | adiciona no lugar desejado
num.pop(3)# Deleta o elemento selecionado
if 2 in num:
   num.remove(2)# Vai remover o primeiro elemento 2 no caso o primeiro selecionado, se remover algo que não esta na lista vai da erro
   # Para não dar erro tem que colocae em um if
else:
   print('Não tem o número 2 na lista')
print(num)
print(f'Nessa lista tem {len(num)} elementos.')

valores = []# Uma lista vazia
valores.append(1)
valores.append(5)
valores.append(9)

for v in valores:
   print(v)# mostra a lista seguida

for c , v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')

var = list()
for cont in range(0,5):
   var.append(int(input('Digite um número: ')))

for z , x in enumerate(var):
    print(f'Na posição {z} encontrei o valor {x}')

print('Cheguei no final da lista')
# Se tenho duas listas igualadas com o = se eu mudar um elemento de uma vai mudar da outra tambem, ligação
a = [2,3,4,5,] 
b= a [:]# assim faz uma copia
b[2]= 8
print(a)
print(b)