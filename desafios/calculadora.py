def somar(num1,num2):
    return num1 + num2

def subtrair(num1,num2):
    return num1 - num2

def multiplicar(num1,num2):
    return num1 * num2

def dividir(num1,num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2

def cauculadora():
    while True:
        try:
            num1 = float(input('Digite o primeiro número: '))
            escolha = int(input('Escolha uma das opções:\n1 - Soman\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n->'))
            num2 = float(input('Digite o segundo número: '))
            if escolha == 1:
                resultado = somar(num1, num2)
            elif escolha == 2:
                resultado = subtrair(num1, num2)
            elif escolha == 3:
                resultado = multiplicar(num1, num2)
            elif escolha == 4:
                resultado = dividir(num1, num2)
            else:
                print('Operação inválida!')
                return
            print(f'Resultado final = {resultado}')
        except ValueError:
            print("Erro: Entrada inválida. Digite apenas números.")
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida.")

        opcao = str(input('Gostaria de fazer outra conta? [N/S] :')).lower()[0]
        if opcao =='n':
            break

cauculadora()