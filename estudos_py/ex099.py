#Comvertor de Temperatura C para F
def converterCparaF(celsius):
    f = (celsius *9/5) + 32
    return f

def cabecalho(text):
    print('-'*30)
    print(text.center(30))
    print('-'*30)

#Código principal
cabecalho('Conversor de Temperatura')
c = int(input('Digite a temperatura em Celsius: '))
f = converterCparaF(c)
print(f'O valor da temperatura em F :{f}')
