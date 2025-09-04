soma = 0
cont = 0 
for n in range(0, 6):
    numero = int(input('Digite um número inteiro: '))
    if numero %2==0:
        cont += 1
        soma = soma + numero

print(f'Foram {cont} números pares digitados')
print(f'A soma desses números foi = {soma}')
print('FIM')