# Banco de dados com Python -> RELACIONAL
import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()
#Codigo SQL -  Banco de Dados, Cria uma tabela caso ela não exista, vai ser uma chave primaria sem repetir
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS estudantes (
id INTEGER PRIMAY KEY,
NOME TEXT,
idade INTEGER   )
""")
#Incira na tabela o nome e idade esses valores
cursor.execute(
    "INSERT INTO estudantes (nome, idade)\
        VALUES (?, ?)", ("João", 20))# Aqui é uma tupla

conn.commit()
#Comando SQL para mostrar toda a tabela selecionada 
cursor.execute("SELECT * FROM estudantes")
print(cursor.fetchall())

conn.close()