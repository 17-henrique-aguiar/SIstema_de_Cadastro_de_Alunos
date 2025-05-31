import sqlite3

def conectar_bd():
    return sqlite3.connect('alunos.db')

def inserir_aluno(nome, idade, curso, nota_final):
    con = conectar_bd()
    cur = con.cursor()
    cur.execute("""
        INSERT INTO alunos (nome, idade, curso, nota_final)
        VALUES (?, ?, ?, ?)
    """, (nome, idade, curso, nota_final))
    con.commit()
    con.close()

def listar_alunos():
    con = conectar_bd()
    cur = con.cursor()
    cur.execute("SELECT * FROM alunos")
    dados = cur.fetchall()
    con.close()
    return dados

def deletar_aluno(id_aluno):
    con = conectar_bd()
    cur = con.cursor()
    cur.execute("DELETE FROM alunos WHERE id = ?", (id_aluno,))
    con.commit()
    con.close()

def listar_cursos_unicos():
    con = conectar_bd()
    cur = con.cursor()
    cur.execute("SELECT DISTINCT curso FROM alunos")
    cursos = [c[0] for c in cur.fetchall()]
    con.close()
    return cursos

def listar_por_curso(curso):
    con = conectar_bd()
    cur = con.cursor()
    cur.execute("SELECT * FROM alunos WHERE curso = ?", (curso,))
