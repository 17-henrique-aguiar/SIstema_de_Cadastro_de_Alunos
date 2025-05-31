import streamlit as st
import dados

st.title("Sistemas de Cadastro de Alunos")

# Cadastro
st.header("Cadastrar Novo Aluno")
nome = st.text_input("Nome do Aluno")
idade = st.number_input("Idade", min_value=1, max_value=100)
curso = st.selectbox("Curso", ["Ciências de Dados", "Engenharia", "Administração", "Direito", "Outro"])
nota_final = st.slider("Nota Final", 0.0, 10.0, 5.0)

if st.button("Cadastrar Aluno"):
    if nome and idade and curso:
        dados.inserir_aluno(nome, idade, curso, nota_final)
        st.success("Aluno cadastrado com sucesso!")
    else:
        st.error("Preencha todos os campos obrigatórios.")

st.divider()

# Listar com filtro por curso
st.header("Lista de Alunos")

cursos = ["Todos"] + dados.listar_cursos_unicos()
curso_filtro = st.selectbox("Filtrar por curso", curso)

if curso_filtro != "Todos":
    alunos = dados.listar_por_curso(curso_filtro)
else:
    alunos = dados.listar_alunos()

st.table(alunos)

# Remoção
st.subheader("Remover Aluno")
id_excluir = st.number_input("ID do aluno a ser removido", min_value=1, step=1)
if st.button("Remover Aluno"):
    dados.deletar_aluno(id_excluir)
    st.success("Aluno removido com sucesso!")