#Aqui vai ter as informações dos usuarios 
import document as model

view = None

def atribuir_view(_view):
    global view
    view = _view

def adicionar_atendente(nome):
    
    resultado = model.adicionar_atendente(nome)

    if resultado == 'vazio':
        view.alerta('Nome Vazio', 'Digite um nome')
    elif resultado == 'duplicado':
        view.alerta('Duplicado', 'Atendente ja existe')
    elif resultado == 'ok':
        view.atualizar_interface()

def resetar_atendentes():
    if view.confirmar_reset():
        model.resetar_atendentes()
        view.atualizar_interface()

def incrementar_vendas(indice):
    model.incrementar_vendas(indice)
    view.atualizar_interface()

def lista_atendentes():
    return model.obter_atendentes()