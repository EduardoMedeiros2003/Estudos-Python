import sqlite3

conn = sqlite3.connect('escola1.db')
cursor = conn.cursor()

# UPTATE = Modificar algo dentro do banco de dados| ? = proteção do banco de dados
cursor.execute(
    """
        UPDATE estudantes SET nome = ? WHERE \
        id = ?
    """,
    ("Lendro",3)# Aqui estou faszendo a mudança do nome do id 3 do banco de dados
)
conn.commit()
conn.close()