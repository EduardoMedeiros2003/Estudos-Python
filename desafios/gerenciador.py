tarefas = ['Estudar Python']

def gerenciador_de_tarefas():
    while True:
        linhas()
        print('1: Adicionar uma tarefa.\n2: Visualizar a lista de tarefas.\n3: Remover uma tarefa da lista.\n4: Sair do programa.\n')
        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            print('Erro: Digite um número válido!')
            continue

        if opcao == 1:
            linhas()
            adicionar_tarefas()
            
        elif opcao == 2:
            linhas()
            visualizar_tarefas()
            
        elif opcao == 3:
            linhas()
            remove_tarefa()
            
        elif opcao == 4:
            print('Finalizando o Gerenciador de tarefas!')
            break
        
def adicionar_tarefas():
    nova_tarefa= str(input('Digite sua nova tarefa: '))
    if nova_tarefa == '':
        print('Tarefa invalida! esta vazia!!')
    else:
        tarefas.append(nova_tarefa)
        print('Tarefa adicionada')

def visualizar_tarefas():
    print('\nLISTA DE TAREFAS:')
    if not tarefas:
        print('Nenhuma tarefa listada!')
    for i, tarefa in enumerate(tarefas, start=1):
        print(f'{i}- {tarefa}')

def remove_tarefa():
    linhas()
    if not tarefas:
        print('Não há tarefas para remover.')
        return
    
    visualizar_tarefas()

    try:
        indici = int(input('Digite o número da tarefa que quer remover: '))
        tarefa_removida = tarefas.pop(indici - 1)
        print(f'Tarefa"{tarefa_removida}" Removida com sucesso!')
    except(ValueError, IndexError):
        print('Erro: Número invalido!')

def linhas():
    print('-='*30)

gerenciador_de_tarefas()