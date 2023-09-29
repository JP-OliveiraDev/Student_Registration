#importando SQlite3
import sqlite3

#CRIAÇÃO DO BANCO DE DADOS

#Criando conexão
try:
    cone = sqlite3.connect("Cadastro_alunos.db")
    print("conexão com banco de dados concluida!")
except sqlite3.Error as e:
    print("Erro ao conectar com o banco de dados!!", e)

#Criando a tabela de cursos
try:
    with cone:
        cur = cone.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS cursos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            duracao TEXT,
            preco REAL   
        )""")
        print("Tabela cursos criada com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar a tabela de cursos!!", e)

#Criando a tabela de turmas
try:
    with cone:
        cur = cone.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS turmas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            curso_nome TEXT,
            data_inicio DATE,
            FOREIGN KEY (curso_nome) REFERENCES cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE
        )""")
        print("Tabela turmas criada com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar a tabela de turmas!!", e)

#Criando a tabela de alunos
try:
    with cone:
        cur = cone.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone TEXT,
            sexo TEXT,
            imagem TEXT,
            data_nascimento DATE,
            cpf INTEGER,
            turma_nome TEXT,
            FOREIGN KEY (turma_nome) REFERENCES turmas (nome) ON DELETE CASCADE
        )""")
        print("Tabela alunos criada com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar a tabela de alunos!!", e)