#Fateamanto de string
frase = 'estudando a lingaugem python'
frase.count('u') # vai contar quantas vezes aparece 
len(frase)# vai contar quantas letras tem no array
#analise
frase.find('lin') # vai mostra onde começa essa a palavra - se receber o valor -1 significa que não existe
'python' in frase # vai responde bolean = True , operador in
#Transformação
frase.replace('python', 'japones')
frase.upper()# vai deixar todas as letras maiúsculas 
frase.lower()# vai deixar todas as letras em minúsculas
frase.capitalize()# vai deixar so a primeira letra em maiúscula e todas as outras em minúscula
frase.title()# vai deixar todas as palavras com a inicial em maiúsculas, descobrindo onde nao tem letra para gerar a palavra 
frase[:9]
frase01 = ('   Esttude sempre   ')
frase01.strip()# vai tirar os espaços inuteis da string
#Divisão
dividido = frase.split()# vai ver onde tem espaços e contar quantas palavras, Lista de palavras 
'-'.join(frase)# vai juntar todas as palavras com (-) entre elas\

print(dividido)