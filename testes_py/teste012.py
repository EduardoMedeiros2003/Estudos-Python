#Tratamento de erro
try: # Tente executar este código
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    divisao = num1/num2
except(ValueError, TypeError) :#Se não conseguir vai mostra isso
    print('Tivemos um problema com os tipos de dados que você digitou.')
except(ZeroDivisionError):
    print('Não é possível dividir um número por zero.')
except(KeyboardInterrupt):
    print('O usuário preferiu não informar os dados.')
else:#Se conseguir vai executar normalmente
    print(f'o resultado foi {divisao}')
finally:#Sempre vai ser executado
    print('Volte sempre!Muito obrigado!')