import tkinter as tk

atendentes = []

def adicionar_atentendes():
    nome = entrada_nome.get().strip()
    if not nome:
        #pendente 
        return
    
    #Verifica se o nome do atendente esta em uma lista de uma unica linha
    if nome in [a['nome'] for a in atendentes]:
        #pendente
        return
    
    atendentes.append({'nome': nome, 'vendas': 0})
    entrada_nome.delete(0, tk.END) #Limpa caixa de texto

#Interface principal
janela = tk.Tk()
janela.title('Controle de vendas - Smart View')

entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5)