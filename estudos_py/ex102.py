lista_numeros = [1,65,3,37,29,13,90, 'oi']
soma = 0

try:
    for numero in lista_numeros:
        soma+=numero
    print(f'Soma dos elementos é: {soma}')
except Exception as e:# Vai mostra o que esta dando errado no ex: so pode valores int e esta com um str
    print(f'O correu um erro: {e}')

lista_valores=[15,20,25,30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores /(len(lista_valores))
    print(f'A média dos valores é: {media}')
except ZeroDivisionError:
    print('A lista está vazia, Não é possível calcular a média.')
except Exception as e:
    print(f'Ocorreu um erro: {e}')



pessoa = ({'nome': 'Felipe', 'idade': 30, 'cidade': 'São Paulo'},
          {'nome': 'Eduardo','idade': 22, 'cidade': 'Cumaru'})
pessoa[0]['idade'] = 31
pessoa[1]['idade']= 23
pessoa[0]['profissao'] = 'Engenheiro'
pessoa[1]['profissao'] = 'Programador'
print(pessoa)
if 'nome' in pessoa:
    print(f'A chave (nome) existe no dicionário.')
else:
    print('A chave (nome), Não existe no dicionário')

numeros_quadrados={x:x**2 for x in range(1,6)}
print(numeros_quadrados)

frase = str(input('Digite uma frase: '))
quantidade = len(frase.split())
print(f'A quantidade de palavras na frase foi de: {quantidade}')