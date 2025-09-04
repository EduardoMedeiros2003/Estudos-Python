soma = 0#Somador
cont = 0#Contador
for n in range(1, 501,2):
    if n %3 == 0:
        cont += 1
        soma = soma + n

print(cont,'Números divisiveis por 3')
print(soma, 'Soma de todos os números')
print('FIM')