def criar_desconto(porcentagem):
    def calcular_preco(valor):
        return valor - (valor * (porcentagem/100))
    return calcular_preco
    
porcentagem = float(input('Digite a porcentagem do desconto: '))
calcula_preco_final = criar_desconto(porcentagem)

valor= float(input('Informe o valor do produto: '))

print(f'O preço final com desconto foi de :{calcula_preco_final(valor)}')


def soma_recursiva(n): #Somando todos os números de 1 ao número digitado
    if n == 1: 
        return 1 
    return n + soma_recursiva(n - 1)# Representa que vai voltando o número  
 
numero = int(input("Digite um número: ")) 
print(f"A soma de 1 a {numero} é: {soma_recursiva(numero)}") 