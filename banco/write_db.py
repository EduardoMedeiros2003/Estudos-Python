import sqlite3

conn = sqlite3.connect('escola1.db')
cursor = conn.cursor()

#Para usar comandos SQL:Veja na tabela estudantes o nome e a idade| VALUES(?,?) Esta ajudando na segurança dos dados, Antes de colocar os dados no banco tem que haver uma validação 
cursor.execute(
    """
    INSERT INTO estudantes(nome, idade)\
    VALUES (?,?)
    """,
    ("Carlos", 28) #Aqui esta entrando os dados no banco de dados
)

conn.commit()
conn.close()

#Estes comandos estão colocando Dados no banco de dados, mas expecfico o nome e idade de um estudante