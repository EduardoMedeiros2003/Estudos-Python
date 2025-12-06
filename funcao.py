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
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando app...')
    os.system('cls')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de Restaurante')

    nome = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome}: ')

    restaurante = {'nome': nome, 'categoria': categoria, 'ativo': False}
    restaurantes.append(restaurante)

    print(f'\nO restaurante {nome} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Lista de Restaurantes')

    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        estado = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome.ljust(20)} | {categoria.ljust(15)} | {estado}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
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
