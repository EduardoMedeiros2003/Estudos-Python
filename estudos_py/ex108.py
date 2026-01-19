convidados = set()

while True:
    nome = str(input('Digite o nome do convidado ou [sair] para encerrar: '))

    if nome.lower() == 'sair':
        break
    convidados.add(nome)

print(f'Convidados confirmados {convidados}')


texto1 = set(input("Texto 1: ").lower().split()) 

texto2 = set(input("Texto 2: ").lower().split()) 

comuns = texto1.intersection(texto2) 

print(f"Palavras em comum: {comuns}") 
# outra atividade
permissoes_principais = set(input("Permissões principais: ").strip().lower().split(',')) 

permissoes_solicitadas = set(input("Permissões solicitadas: ").strip().lower().split(',')) 

for i in range(len(permissoes_principais)):  

    permissoes_principais[i] = permissoes_principais[i].strip() 

for i in range(len(permissoes_solicitadas)):  

    permissoes_solicitadas[i] = permissoes_solicitadas[i].strip() 

eh_subconjunto = permissoes_solicitadas.issubset(permissoes_principais) 

if eh_subconjunto:  # For verdade =

    print("As permissões solicitadas fazem parte das permissões principais.")  

else:  # se não

    print("As permissões solicitadas não fazem parte das permissões principais.")

    
equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}  

equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}  

tarefas_combinadas = equipe_a.union(equipe_b) 

tarefa_remover = input("Tarefa a ser removida: ").lower()  

if tarefa_remover in tarefas_combinadas:  

    tarefas_combinadas.remove(tarefa_remover) 

print(f"Tarefas finais: {tarefas_combinadas}")  