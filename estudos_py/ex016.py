#Sistema que le um numero e diz quantas unidades tem em cada casa
num = int(input('Digite um número de 0 a 9999: '))
unidades = num % 10
dezenas = (num // 10) % 10
centenas = (num // 100) % 10
milhares = (num // 1000) % 10
print(f'Unidades: {unidades}')
print(f'Dezenas: {dezenas}')
print(f'Centenas: {centenas}')
print(f'Milhares: {milhares}')
