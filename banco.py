import sqlite3

# Conexão
conexao = sqlite3.connect('alunos.db')

# Cursor
cursor = conexao.cursor()

# Tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        curso TEXT NOT NULL,
        nota_final REAL
    );
""")

# Fechar conexão
conexao.close()
print("Tabela de alunos criada com sucesso!")
