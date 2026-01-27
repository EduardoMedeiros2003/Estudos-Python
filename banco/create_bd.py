import sqlite3

conn = sqlite3.connect('escola1.db') #Cria | Conecta| Fazendo a conexão com o banco de dados | Crianco o banco de dados caso ela não exista

cursor = conn.cursor() #Aqui faz os comandos do banco de dados

#Aqui vai um comando puro de SQL| INTEGER esta criando o campo inteiro na cahve estudantes | e adiciona a chave primaria | Criando uma tabela
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS estudantes(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER
    )
    """
)
#FOREIGN KEY é uma chave estrangeira | A tabela disciplinas tem ligamento com a tabela estudantes pelo id do estudante
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS disciplinas(
        id INTEGER PRIMARY KEY,
        nome_disciplina TEXT,
        estudante_id INTEGER,
        FOREIGN KEY (estudante_id) \
            REFERENCES estudantes(id)
    )
    """
)

#Sempre tem que confirmar o comando SQL do banco de dados com o comando commite
conn.commit()
# Tem que fechar a conexão do banco de dados quando terminar o código
conn.close()