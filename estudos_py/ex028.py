print('Digite dois números inteiros')
num1 = int(input('Digite o Primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'{num1} é maior que {num2}, primeiro valor MAIOR')
elif num1 < num2:
    print(f'{num1} é menor que {num2}, segundo valor MAIOR')
elif num1 == num2:
    print(f'Não existe valor maior ou menor, os dois São IGUAS {num1} = {num2}')
