# Solicita os dados do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o resultado
print(f"Seu IMC é {imc:.1f}")

# Classificação básica
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Classificação: Peso normal")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
