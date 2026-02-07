import re

texto = input(str('Digite a descrição da receita: '))
numero = re.findall(r'\d+', texto)[0]
print(f'O número da receita é: {numero}')

texto1 = input("Digite o texto a ser revisado: ")  
palavra_antiga = input("Qual palavra deseja substituir? ")  
palavra_nova = input("Qual a nova palavra? ")  
#                               Vai mudar       para esta     nesse texto
nova_frase = re.sub(rf'\b{palavra_antiga}\b', palavra_nova, texto1)
print(nova_frase)

nome = input("Digite o nome do cliente para validação: ")  
if re.fullmatch(r'[A-Z][a-z]*', nome):
    print("Nome válido!")
else:
    print("Nome inválido!")