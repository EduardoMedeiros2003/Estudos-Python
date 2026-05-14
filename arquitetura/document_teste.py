import document
# Aqui vai testar todas as funções do arquivo document.py
# O comando 'assert' ele verifica uma condição se ela nao for True vai aparecer uma mensagem de erro 
def testar_adicao_e_duplicar():
    document.resetar_atendentes()
    assert document.adicionar_atendente('Pessoa') == 'ok'
    assert document.adicionar_atendente('') == 'vazio'
    assert document.adicionar_atendente('Pessoa') == 'duplicado'

def testar_incremento():
    document.resetar_atendentes()
    document.adicionar_atendente('Pessoa')
    document.incrementar_vendas(0)
    assert document.obter_atendentes()[0]['vendas'] == 1

# Frente de execução
if __name__ == '__main__':
    testar_adicao_e_duplicar()
    testar_incremento()
    print('Todos os testes passaram!')
