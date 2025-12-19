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

print('Pedindo a conta do restaurante...')
conta = float(input('Digite o valor da conta: R$ '))
gorjeta_porcentagem = float(input('Digite o valor da gorjeta em %:'))
gorjeta_calculada = (gorjeta_porcentagem/100)*conta
total_pagar = conta + gorjeta_calculada

print(f'O total da gorjeta para pagar é de R${gorjeta_calculada:.2f}')
print(f'Contudo o valor total a ser pago é de R${total_pagar:.2f}')