nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

with open ('input_data.txt', 'a') as f: # No lugar do 'a' se for um 'w' ele vai escrever por cima e criar o arquivo, tem q começar com o 'w'
    f.write(f'Nome: {nome}\n')
    f.write(f'Idade: {idade}\n')

with open('input_data.txt', 'r') as f:
    for linha in f:
        print(linha)