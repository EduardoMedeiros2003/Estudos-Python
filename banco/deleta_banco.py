import os

def deletar_banco():
    if os.path.exists("escola.db"):
        os.remove("escola.db")
        print("Banco de dados deletado com sucesso.")
    else:
        print("Banco não encontrado.")

deletar_banco()