#importando SQlite3
import sqlite3

# CONEXÃO COM BANCO DE DADOS

#criando conexão
try:
    cone = sqlite3.connect("Cadastro_alunos.db")
    print("conexão com banco de dados concluida!")
except sqlite3.Error as e:
    print("Erro ao conectar com o banco de dados!!", e)

# tabela de cursos --------------------------------------

#criar cursos (create C )
def criar_curso(i):
    with cone:
        cur = cone.cursor()
        query = "INSERT INTO Cursos (nome, duracao, preco) VALUES (?,?,?)"
        cur.execute(query,i)

#criar_curso(['Python', 'Semanas', 50])

# ver todos os cursos (read R )
def ver_cursos():
    lista = []
    with cone:
        cur = cone.cursor()
        cur.execute("SELECT * FROM Cursos")
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista


# atualizar cursos (update U )
def atualizar_curso(i):
    with cone:
        cur = cone.cursor()
        query = "UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id=?"
        cur.execute(query,i)



# deletar cursos (delete D )
def deletar_curso(i):
    with cone:
        cur = cone.cursor()
        query = "DELETE FROM Cursos WHERE id=?"
        cur.execute(query,i)

# tabela de turmas --------------------------------------

# criar turmas ( inserir ) 
def criar_turma(i):
    with cone:
        cur = cone.cursor()
        query = "INSERT INTO Turmas (nome, curso_nome, data_inicio) VALUES (?, ?, ?)"
        cur.execute(query, i)

# ver todos as turmas (read R )
def ver_turmas():
    lista = []
    with cone:
        cur = cone.cursor()
        cur.execute("SELECT * FROM Turmas")
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

# atualizar turmas (update U )
def atualizar_turma(i):
    with cone:
        cur = cone.cursor()
        query = "UPDATE turmas SET nome=?, curso_nome=?, data_inicio=? WHERE id=?"
        cur.execute(query,i)


# deletar turma (delete D )
def deletar_turma(i):
    with cone:
        cur = cone.cursor()
        query = "DELETE FROM Turmas WHERE id=?"
        cur.execute(query,i)


# tabela de alunos --------------------------------------

# criar alunos ( inserir ) 
def criar_alunos(i):
    with cone:
        cur = cone.cursor()
        query = "INSERT INTO Alunos (nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

# ver alunos (read R )
def ver_aluno():
    lista = []
    with cone:
        cur = cone.cursor()
        cur.execute("SELECT * FROM Alunos")
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

# atualizar alunos (update U )
def atualizar_aluno(i):
    with cone:
        cur = cone.cursor()
        query = "UPDATE alunos SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, turma_nome=? WHERE id=?"
        cur.execute(query,i)


# deletar alunos (delete D )
def deletar_aluno(i):
    with cone:
        cur = cone.cursor()
        query = "DELETE FROM Alunos WHERE id=?"
        cur.execute(query,i)