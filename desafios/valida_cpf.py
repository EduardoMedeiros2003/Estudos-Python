import re
# DEpois voltar aqui e fazer o calculo correto para a validação, e passando em int o cpf
cpf = str(input('Digite o CPF no formato xxx.xxx.xxx-xx: '))
padarao = r'\d{3}\.\d{3}\.\d{3}-\d{2}'

if re.search(padarao, cpf):
    print('O CPF está no formato correto.')
else:
    print('O CPF está no formato incorreto')

texto = input("Digite o título dos livro: ") 
letra = input("Digite a letra inicial para pesquisa: ")  
palavras = re.findall(rf'\b{letra}[a-zà-ÿ]*', texto, re.IGNORECASE)# Vai funcionar com maiúsculas e minúsculas
print(palavras)
