import os

# Lista de restaurantes
restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Italiana', 'ativo': True},
    {'nome': 'Café', 'categoria': 'Brasileira', 'ativo': True}
]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝
""")

def exibir_opcoes():
    ''' Esta função lista as opções'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Esta função finaliza o app, sempre utilizada no final de cada outra função'''
    exibir_subtitulo('Finalizando app...')
    os.system('cls')

def voltar_ao_menu_principal():
    ''' Esta função volta para a tela principal'''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    ''' Esta função é um controle de erro para se o usuario usar não travar o sistema'''
    print('Opção inválida!')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Esta função vai mostra sempre o sub-titulo da área que está entrando no  app, sempre utilizada no início de outras funções'''
    os.system('cls')
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''' Esta função vai adicionar um novo restalrante com nome e categoria, seu status sempre vai ser False'''
    exibir_subtitulo('Cadastro de Restaurante')

    nome = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome}: ')

    restaurante = {'nome': nome, 'categoria': categoria, 'ativo': False}
    restaurantes.append(restaurante)

    print(f'\nO restaurante {nome} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Esta função vai listra os restaurantes de forma bonita para a visualização do usuario'''
    exibir_subtitulo('Lista de Restaurantes')

    print(f"{'Nome do restalrante'.ljust(22)} | {'Categoria'.ljust(15)} | Status")
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        estado = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome.ljust(20)} | {categoria.ljust(15)} | {estado}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' Esta função vai mudar o status do restalrante, de False para Trueou de True para False'''
    exibir_subtitulo('Alterar Estado do Restaurante')

    nome = input('Digite o nome do restaurante: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome.lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            estado = "ativado" if restaurante['ativo'] else "desativado"
            print(f'O restaurante {nome} foi {estado} com sucesso.')
            break

    if not restaurante_encontrado:
        print('Restaurante não encontrado.')

    voltar_ao_menu_principal()

def escolher_opcao():
    ''' Esta função vai ser a navegação do app de restaurantes'''
    try:
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            cadastrar_novo_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            alternar_estado_restaurante()
        elif opcao == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except ValueError:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
