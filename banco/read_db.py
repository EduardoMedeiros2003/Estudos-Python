import sqlite3

conn = sqlite3.connect('escola1.db')
cursor = conn.cursor()

#Criando comando de LEITURA do SQL:

# SELECT = consulta o banco | *FROM = Pega todas as ocorrencias da tabela

#cursor.execute(
#    """
#    SELECT * FROM estudantes
#    """
#)

#cursor.execute(
#    """
#        SELECT * FROM disciplinas
#    """
#)

# Aqui vai pegar todos os alunos que estão matriculados em disciplinas, mostrando a disciplina e o nome| Consulta conjunta entre as duas tabelas criadas 
cursor.execute(
    """
        SELECT estudantes.nome, disciplinas.nome_disciplina FROM disciplinas JOIN estudantes ON disciplinas.estudante_id
    """
)
conn.commit()

print(cursor.fetchall())

diciplinas = cursor.fetchall()
for diciplina in diciplinas:
    print(diciplina)

# este comando vai salvar tudo que ele conseguiu achar do do comando anterior do banco de dados e salvar em estudantes, para ver o que tem nele so fazer um luoop for

#estudantes = cursor.fetchall()

#for estudante in estudantes:
#    print(estudante)

conn.close()