#Cadastrando um usuário no sistema
while True:
    nome_usuario= str(input('Digite seu nome de usuário: ')).lstrip()
    senha = str(input('Digite sua senha: '))
    if len(nome_usuario) < 5:
        print('O nome do usuário deve ter pelo menos 5 caracteres!')
        continue
    if len(senha) < 8:
        print('A senha deve ter pelo menos 8 caracteres!')
        continue
    print('Cadastro realizado com sucesso!')
    break
    
    
    
def contar_caracteres(palavra): 
    return len(palavra) 
 
texto = input("Digite uma palavra: ") 
print(f"Essa palavra tem {contar_caracteres(texto)} caracteres.") 


def saudacao(hora): 
    if hora < 12: 
        return "Bom dia!" 
    elif hora < 18: 
        return "Boa tarde!" 
    else: 
        return "Boa noite!" 
 
hora_atual = int(input("Digite a hora atual (0-23): ")) 
print(saudacao(hora_atual)) 


def converter_telefones(lista):  

   return [int(telefone) for telefone in lista] 

def verifica_tipos(lista):  

   for num in lista:  

       if not isinstance(num, int):  

           return "Erro na conversão."  

   return "Todos os números foram convertidos corretamente!" 

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

telefones_convertidos = converter_telefones(telefones) 

print(verifica_tipos(telefones_convertidos)) 
