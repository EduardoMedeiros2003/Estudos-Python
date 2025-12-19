def limpa_texto(texto):
    texto = texto.lower()# deixando tudo em minusculo
    caracteres = ",.\?!:;'()[]{}",
    for char in caracteres:
        texto = texto.replace(char,"") # vai limpar todos os caracteres não desejados do texto
        return texto
    
def contar_palavras(frase):
    frase = limpa_texto(frase)
    if not frase.split():
        return {}
    palavras = frase.split()
    contagem = {}
    for palavra in palavras:
        contagem [palavra] = contagem.get(palavra,0) + 1
    return contagem

#Codigo principal
print('-'*30)
print('       Contador de Palavras')
print('-'*30)

frase = str(input('Digite uma frase: ')).strip()
if not frase: 
    print('Erro: Nenhuma frase foi digitada.')
else:
    resultado = contar_palavras(frase)
    if resultado:
        print('Vai contar quantas Palavras foram digitadas')
        print('Contagem de Palavras: ')
        for palavra , qauntidade in resultado.items():
            print(f'{palavra}: {qauntidade}')
        else:
            print(f'Nenhuma palavra válida foi digitada.')
    
