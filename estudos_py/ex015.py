#Sistema que le um nome completo, mexe em sua estrutura e ler o primeiro nome e diz quantas letras tem nele
nome = str(input('Digite seu nome completo: '))
print ('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}') 
print(f'Seu nome em minúsculas é {nome. lower ()}')
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")
separa = nome. split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len (separa[0])} Letras')