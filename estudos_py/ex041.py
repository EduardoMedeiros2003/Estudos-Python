frase = str(input('Digite uma frase: ')).split().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
    if inverso == junto:
        print('Tesmos um palíndromo!')
    else:
        print('Não é um palíndromo!')