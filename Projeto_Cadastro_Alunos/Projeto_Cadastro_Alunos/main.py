# Importando bibliotecas necessárias
from tkinter.tix import IMAGETEXT
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from typing import Self
from PIL import Image
from PIL import ImageTk
from tkcalendar import calendar_ 
from tkcalendar import DateEntry
from datetime import date
import customtkinter

# Importando View
from view import *



# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha
co6 = "#038cfc"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10 ="#808080"

# Criando a janela

janela = customtkinter.CTk()
janela.title("")
janela.geometry('850x620')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

Style = Style(janela)

# Crinado frames e linhas

frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)


frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)
ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)


frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)


frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=0, sticky=NSEW)

# Frame foto e titulo ---------------------------------------------------

app_lg = Image.open("logo.png")
app_lg = app_lg.resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text=" Cadastro de Alunos", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=("Courier 17 bold"), bg=co10, fg=co1)
app_logo.place(x=0, y=0)

# Função para cadastrar alunos --------------------------------------------
def alunos():
    
    # Função Novo aluno
    def novo_aluno():
        # Função para escolher imagem
        global imagem, imagem_string, l_imagem
        
        nome = e_nome.get()
        email = e_email.get()
        telefone = e_tel.get()
        sexo = c_sexo.get()
        data = data_nasc.get()
        cpf = e_cpf.get()
        curso = c_turma.get()
        imagem = imagem_string
        
        
        lista = [nome, email, telefone, sexo, imagem, data, cpf, curso]
        
        # Verificando se todos os campos estão preenchido
        for i in lista or imagem_string:
            if i=="":
                messagebox.showerror("ERRO", "Preencha todos os campos!")
                return
            
        # Inserindo os dados no banco de dados
        criar_alunos(lista)
        
        # Mostrando mensagem de sucesso
        messagebox.showinfo("Sucesso", "Os dados preenchidos foram inseridos com êxito!")
        
        # Limpando os campos de entrada
        e_nome.delete(0,END)
        e_email.delete(0,END)   
        e_tel.delete(0,END)
        c_sexo.destroy
        data_nasc.delete(0,END)
        e_cpf.delete(0,END)
        c_turma.destroy
        
        
        # Mostrando os valores na tabela
        mostrar_alunos()
        
    # Função Atualizar aluno
    def update_aluno():
        # Função para escolher imagem
        global imagem, imagem_string, l_imagem
        
        try:
            tree_itens = tree_aluno.focus()
            tree_dicionario = tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario["values"]
            
            valor_id = tree_lista[0]
            
            # Limpando os campos de entrada
            e_nome.delete(0,END)
            e_email.delete(0,END)   
            e_tel.delete(0,END)
            c_sexo.destroy
            data_nasc.delete(0,END)
            e_cpf.delete(0,END)
            c_turma.destroy
           
            
            # Inserindo os valores nos campos de entrada
            e_nome.insert(0,tree_lista[1])
            e_email.insert(0,tree_lista[2])   
            e_tel.insert(0,tree_lista[3])
            c_sexo.get
            data_nasc.insert(0,tree_lista[6])
            e_cpf.insert(0,tree_lista[7])
            c_turma.get
            
            imagem = tree_lista[5]
            imagem_string = imagem
            
            # Abrindo a imagem
            imagem = Image.open(imagem)
            imagem = imagem.resize((130, 130))
            imagem = ImageTk.PhotoImage(imagem)
            l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
            l_imagem.place(x=300, y=10)
            
                
            
            def update():
                
                nome = e_nome.get()
                email = e_email.get()
                telefone = e_tel.get()
                sexo = c_sexo.get()
                data = data_nasc.get()
                cpf = e_cpf.get()
                curso = c_turma.get()
                imagem = imagem_string
                
                lista = [nome, email, telefone, sexo, imagem, data, cpf, curso, valor_id]
                
                # Verificando se todos os campos estão preenchido
                for i in lista:
                    if i=="":
                        messagebox.showerror("ERRO", "Preencha todos os campos!")
                        return
                    
                # Atualizando os dados no banco de dados
                atualizar_aluno(lista)
                
                # Mostrando mensagem de sucesso
                messagebox.showinfo("Sucesso", "Os dados preenchidos foram atualizados com êxito!")
                
                # Limpando os campos de entrada
                e_nome.delete(0,END)
                e_email.delete(0,END)   
                e_tel.delete(0,END)
                c_sexo.destroy
                data_nasc.delete(0,END)
                e_cpf.delete(0,END)
                c_turma.destroy
                l_imagem.destroy
                
                
                # Mostrando os valores na tabela
                mostrar_alunos()
                
                # Destruindo Botão salvar
                botao_update.destroy()   
                

            # Botão Confirmar
            botao_update = Button(frame_detalhes, command=update, anchor=CENTER, text="salvar Atualização".upper(), overrelief=RIDGE, font=("Courier 7"), bg=co0, fg=co1)
            botao_update.place(x=638, y=100)
            
        except IndexError:
            messagebox.showerror("ERRO", "Selecione um dos alunos na tabela!")
            
    # Função Deletar aluno
    def delete_aluno():
        try:
            tree_itens = tree_aluno.focus()
            tree_dicionario = tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario["values"]
            
            valor_id = tree_lista[0]
            
            # Deletar os dados no banco de dados
            deletar_aluno([valor_id])
            
            # Mostrando mensagem de sucesso
            messagebox.showinfo("Sucesso","Aluno deletado com êxito!")
            
            # Mostrando valores na tabela
            mostrar_alunos()
            
        except IndexError:
            messagebox.showerror("ERRO", "Selecione um aluno na tabela!")
            
# Criando campos de entrada para alunos

   # Caixa de texto do Nome
    l_nome = customtkinter.CTkLabel(master=frame_detalhes, text="", text_color="green")
    l_nome.place(x=280, y=28)
    e_nome = customtkinter.CTkEntry(master=frame_detalhes, placeholder_text="Nome do Aluno", width=280, border_width=2, corner_radius=10, fg_color=co0)
    e_nome.place(x=7, y=50)
    
    
    # Caixa de texto do Email
    l_email = customtkinter.CTkLabel(master=frame_detalhes, text="", text_color="green")
    l_email.place(x=185, y=89)
    e_email = customtkinter.CTkEntry(master=frame_detalhes, placeholder_text="Email do Aluno", width=280, border_width=2, corner_radius=10, fg_color=co0)
    e_email.place(x=7, y=110)
    
    # Caixa de texto do Telefone
    l_tel = customtkinter.CTkLabel(master=frame_detalhes, text="", text_color="green")
    l_tel.place(x=40, y=149)
    e_tel = customtkinter.CTkEntry(master=frame_detalhes, placeholder_text="Telefone do Aluno", width=130, border_width=2, corner_radius=10, fg_color=co0)
    e_tel.place(x=7, y=170)
    
    # Caixa da escolha de sexo
    opcao = customtkinter.StringVar(value="Sexo")
    sexos = ["Masculino", "Feminino"]
    sexo = []
    for i in sexos:
        sexo.append(i)
    c_sexo = customtkinter.CTkComboBox(master=frame_detalhes, width=115, values=["Masculino", "Feminino"], variable=opcao, border_width=2, corner_radius=10, fg_color=co0)
    c_sexo["values"] = (sexo)
    c_sexo.place(x=170, y=170) 
    
    # Caixa de texto Data de nascimneto
    l_nasc = Label(frame_detalhes, text="Data de Nascimneto: *", height=1, anchor=NW, font=("Courier 9"), bg=co1, fg=co4)
    l_nasc.place(x=444, y=29)
    data_nasc = DateEntry(frame_detalhes, width=15, background="black", foreground="white", borderwidth=2, year=2023)
    data_nasc.place(x=447, y=50)
    
    # Caixa de texto do CPF
    l_cpf = customtkinter.CTkLabel(master=frame_detalhes, text="", text_color="green")
    l_cpf.place(x=470, y=89)
    e_cpf = customtkinter.CTkEntry(master=frame_detalhes, placeholder_text="CPF do Aluno", width=150, border_width=2, corner_radius=10, fg_color=co0)
    e_cpf.place(x=447, y=110)
    
    # Caixa da escolha da turma
    opcao = customtkinter.StringVar(value="Turmas")
    turmas = ver_turmas()
    turma = []
    for i in turmas:
        turma.append(i[1])
    c_turma = customtkinter.CTkComboBox(master=frame_detalhes, width=150, values=turma, variable=opcao, border_width=2, corner_radius=10, fg_color=co0)
    c_turma["values"] = (turma)
    c_turma.place(x=447, y=170) 
    
    
    # Caixa de texto do Procurar aluno
    l_Procurar = customtkinter.CTkLabel(master=frame_detalhes, text="", text_color="green")
    l_Procurar.place(x=638, y=29)
    e_Procurar = customtkinter.CTkEntry(master=frame_detalhes, placeholder_text="Procurar Aluno", width=200, border_width=2, corner_radius=10, fg_color=co0)
    e_Procurar.place(x=640, y=50)

    # Botão Procurar 
    botao_Procurar = customtkinter.CTkButton(frame_detalhes, anchor=CENTER, text="Procurar", width=20, height=10, corner_radius=10, border_width=1, border_color=co1, bg_color=co0, fg_color=co0, font=("ariel", 11) )
    botao_Procurar.place(x=780, y=54) 
    
    # Botões Procurar Alunos
    
    # Botão Salvar
    botao_carregar = customtkinter.CTkButton(frame_detalhes, command=novo_aluno, anchor=CENTER, text="Novo".upper(), width=20, height=10, border_width=1, border_color="#000", bg_color=co1, hover_color=co3, fg_color=co0, corner_radius=10)
    botao_carregar.place(x=640, y=125)    
    
    # Botão Atualizar
    botao_atualizar = customtkinter.CTkButton(frame_detalhes, command=update_aluno, anchor=CENTER, text="Atualizar".upper(), width=20, height=10, border_width=1, border_color="#000", bg_color=co1, fg_color=co0, hover_color=co6, corner_radius=10)
    botao_atualizar.place(x=638, y=150) 
    
    # Botão Deletar
    botao_deletar = customtkinter.CTkButton(frame_detalhes, command=delete_aluno, anchor=CENTER, text="Deletar".upper(), width=20, height=10, border_width=1, border_color="#000", bg_color=co1, fg_color=co0, hover_color=co7, corner_radius=10)
    botao_deletar.place(x=638, y=175) 
    
    # Botão Ver
    #botao_ver = customtkinter.CTkButton(frame_detalhes, command=novo_aluno, anchor=CENTER, text="Ver".upper(), width=20, height=10, border_width=1, border_color="#000", bg_color=co1, fg_color=co0, corner_radius=10)
    #botao_ver.place(x=740, y=175) 
    
    # Função para colocar imagem
    global imagem, imagem_string, l_imagem
    
    def escolher_imagem():
        global imagem, imagem_string, l_imagem
        imagem = fd.askopenfilename()
        imagem_string = imagem
        
        # Abrindo a imagem
        imagem = Image.open(imagem)
        imagem = imagem.resize((130, 130))
        imagem = ImageTk.PhotoImage(imagem)
        l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
        l_imagem.place(x=300, y=10)
        
        botao_carregar["text"] = "TROCAR DE FOTO"
    
    botao_carregar = customtkinter.CTkButton(frame_detalhes, command=escolher_imagem, anchor=CENTER, text="CARREGAR FOTO".upper(), width=20, height=10, border_width=1, border_color="#000", bg_color=co1, fg_color=co0, hover_color=co10, corner_radius=10)
    botao_carregar.place(x=310, y=175) 
    
     # Tabela
    
    def mostrar_alunos():
        app_nome = Label(frame_tabela, text="                                          Tabela de Estudantes", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Courier 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # criando uma visualização em árvore com barras de rolagem duplas
        list_header = ['id','Nome','email',  'Telefone','sexo', 'imagem', 'Data', 'CPF','Curso']

        df_list = ver_aluno()
        global tree_aluno
        tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
        # horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)

        tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_aluno.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","nw","center","center","center","center","center","center"]
        h=[40,150,150,70,70,70,80,80,100]
        n=0

        for col in list_header:
            tree_aluno.heading(col, text=col.title(), anchor=NW)
            # ajuste a largura da coluna para a string do cabeçalho
            tree_aluno.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_aluno.insert('', 'end', values=item)

    mostrar_alunos()
    
    
        
        
    
    # Linha divisória -----------------------------------------------------
    
    l_linha = Label(frame_detalhes, relief=GROOVE, text="h", width=1, height=120, anchor=NW, font=("Courier 1"), bg=co0, fg=co0)
    l_linha.place(x=617, y=10)
    l_linha = Label(frame_detalhes, relief=GROOVE, text="h", width=1, height=120, anchor=NW, font=("Courier 1"), bg=co1, fg=co0)
    l_linha.place(x=615, y=10)
    

    # Função para adicionar Cursos e Turmas -----------------------------------
def adicionar():
    # Criando frame para a tabela Cursos
    frame_tabela_curso = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_curso.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
    
    # Criando frame linha
    frame_tabela_linha = Frame(frame_tabela, width=30, height=200, bg=co1)
    frame_tabela_linha.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)
    
    # Criando frame para a tabela Turmas
    frame_tabela_turma = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_turma.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)
    
    # Criando campos de entrada para Cursos ---------------------------------
    
    # Função novo curso
    def novo_curso():
        nome = e_nome_curso.get()
        duracao = e_duracao.get()
        preco = e_preco.get()
        
        lista = [nome, duracao, preco]
        
        # Verificando se está vazio

        for i in lista:
            if i=="":
                messagebox.showerror("ERRO", "Prencha todos os campos!")
                return
            
        # Inserindo os dados
        criar_curso(lista)
    
        # Mostrando mensagem sucesso
        messagebox.showinfo("Sucesso", "Os dados preenchidos foram inseridos com êxito!")
        
        # Excluindo os valores
        e_nome_curso.delete(0,END)
        e_duracao.delete(0,END)
        e_preco.delete(0,END)
        
        # Mostrando os valores na tabela
        mostrar_cursos()
        
    
    # Função atualizar curso
    def update_curso():
        try:
            tree_itens = tree_curso.focus()
            tree_dicionario = tree_curso.item(tree_itens)
            tree_lista = tree_dicionario["values"]
            
            valor_id = tree_lista[0]
            
            # Inserindo os valores na entries
            e_nome_curso.insert(0, tree_lista[1])
            e_duracao.insert(0, tree_lista[2])
            e_preco.insert(0, tree_lista[3])
            
            # Criando função atualizar
            def update():
                
                nome = e_nome_curso.get()
                duracao = e_duracao.get()
                preco = e_preco.get()
                
                lista = [nome, duracao, preco, valor_id]
                
                # Verificando se está vazio

                for i in lista:
                    if i=="":
                        messagebox.showerror("ERRO", "Prencha todos os campos!")
                        return
                    
                # Inserindo os dados
                update_curso(lista)
            
                # Mostrando mensagem sucesso
                messagebox.showinfo("Sucesso", "Os dados preenchidos foram inseridos com êxito!")
                
                # Excluindo os valores
                e_nome_curso.delete(0, END)
                e_duracao.delete(0, END)
                e_preco.delete(0, END)
                
                # Mostrando os valores na tabela
                mostrar_cursos()    

                # Destruindo botão confirmar
                botao_salvar.destroy()
   
            # Botão Confirmar
            botao_salvar = Button(frame_detalhes, command=update, anchor=CENTER, text="salvar Atualização".upper(), overrelief=RIDGE, font=("Courier 7"), bg=co0, fg=co1)
            botao_salvar.place(x=256, y=135)
            
        except IndexError:
            messagebox.showerror("EERO", "Selecione um dos cursos na tabela!")
            
    # Função deletar curso
    def delete_curso():
        try:
            tree_itens = tree_curso.focus()
            tree_dicionario = tree_curso.item(tree_itens)
            tree_lista = tree_dicionario["values"]
            
            valor_id = tree_lista[0]

            # Deletar os dados do banco de dados
            deletar_curso([valor_id])
        
            # Mostrando mensagem sucesso
            messagebox.showinfo("Sucesso", "Os dados preenchidos foram deletados com êxito!")

            # Mostrando os valores na tabela
            mostrar_cursos()
            
        except IndexError:
            messagebox.showerror("ERRO", "Selecione um dos cursos na tabela!")    
    
                    
    # Caixa de texto do nome do curso
    l_nome = customtkinter.CTkLabel(master=frame_detalhes, text="", text_color="green")
    l_nome.place(x=4, y=19)
    e_nome_curso = customtkinter.CTkEntry(master=frame_detalhes, placeholder_text="Nome do curso", width=250, border_width=2, corner_radius=10, fg_color=co0)
    e_nome_curso.place(x=7, y=40)
    
    
    # Caixa de texto da Duração
    l_duracao = customtkinter.CTkLabel(master=frame_detalhes, text="", text_color="green")
    l_duracao.place(x=4, y=79)
    e_duracao = customtkinter.CTkEntry(master=frame_detalhes, placeholder_text="Duração", width=150, border_width=2, corner_radius=10, fg_color=co0)
    e_duracao.place(x=7, y=100)
    
    
    # Caixa de texto do preço
    l_preco = customtkinter.CTkLabel(master=frame_detalhes, text="", text_color="green")
    l_preco.place(x=4, y=139)
    e_preco = customtkinter.CTkEntry(master=frame_detalhes, placeholder_text="Preço", width=150, border_width=2, corner_radius=10, fg_color=co0)
    e_preco.place(x=7, y=160)
    
    
    # Criando botões do frame CURSO
    
    #Botão Salvar
    botao_carregar = customtkinter.CTkButton(frame_detalhes, command=novo_curso, anchor=CENTER, text="Novo".upper(), width=20, height=10, border_width=1, border_color="#000", bg_color=co1, hover_color=co3,fg_color=co0, corner_radius=10)
    botao_carregar.place(x=170, y=165)    
    
    #Botão Atualizar
    botao_atualizar = customtkinter.CTkButton(frame_detalhes, command=update_curso, anchor=CENTER, text="Atualizar".upper(), width=20, height=10, border_width=1, border_color="#000", bg_color=co1, fg_color=co0, hover_color=co6,corner_radius=10)
    botao_atualizar.place(x=219, y=165) 
    
    #Botão Deletar
    botao_deletar = customtkinter.CTkButton(frame_detalhes, command=delete_curso, anchor=CENTER, text="Deletar".upper(), width=20, height=10, border_width=1, border_color="#000", bg_color=co1, fg_color=co0, hover_color=co7,corner_radius=10)
    botao_deletar.place(x=300, y=165) 
    
    # Tabela CURSOS
    
    def mostrar_cursos():
        app_nome = Label(frame_tabela_curso, text="             Tabela de Cursos", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Courier 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # criando uma visualização em árvore com barras de rolagem duplas
        list_header = ['ID','Curso','Duração','Preço']

        df_list = ver_cursos()
        global tree_curso
        tree_curso = ttk.Treeview(frame_tabela_curso, selectmode="extended",columns=list_header, show="headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_curso, orient="vertical", command=tree_curso.yview)
        # horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela_curso, orient="horizontal", command=tree_curso.xview)

        tree_curso.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_curso.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_curso.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","e","e"]
        h=[30,110,130,70]
        n=0

        for col in list_header:
            tree_curso.heading(col, text=col.title(), anchor=NW)
            # ajuste a largura da coluna para a string do cabeçalho
            tree_curso.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_curso.insert('', 'end', values=item)
    mostrar_cursos()
    
    # Linha divisória -----------------------------------------------------
    
    l_linha = Label(frame_detalhes, relief=GROOVE, text="h", width=1, height=120, anchor=NW, font=("Courier 1"), bg=co0, fg=co0)
    l_linha.place(x=374, y=10)
    l_linha = Label(frame_detalhes, relief=GROOVE, text="h", width=1, height=120, anchor=NW, font=("Courier 1"), bg=co1, fg=co0)
    l_linha.place(x=372, y=10)
    
    # Linha divisória tabela -----------------------------------------------
    
    l_linha = Label(frame_tabela_linha, relief=GROOVE, text="h", width=1, height=140, anchor=NW, font=("Courier 1"), bg=co0, fg=co0)
    l_linha.place(x=6, y=10)
    l_linha = Label(frame_tabela_linha, relief=GROOVE, text="h", width=1, height=140, anchor=NW, font=("Courier 1"), bg=co1, fg=co0)
    l_linha.place(x=4, y=10)
    
    # Detalhes da Turma ----------------------------------------------------
    
    # Função nova turma
    def nova_turma():
        nome = e_nome_turma.get()
        curso = c_curso.get()
        data = data_inicio.get()
        
        lista = [nome, curso, data]
        
        # Verificando se está vazio
        for i in lista:
            if i=="":
                messagebox.showerror("ERRO", "Prencha todos os campos!")
                return
            
        # Inserindo os dados
        criar_turma(lista)
    
        # Mostrando mensagem sucesso
        messagebox.showinfo("Sucesso", "Os dados preenchidos foram inseridos com êxito!")
        
        # Excluindo os valores
        e_nome_turma.destroy
        c_curso.destroy
        data_inicio.destroy
        
        # Mostrando os valores na tabela
        mostrar_turmas()
        
    # Função atualizar Turma
    def update_turma():
        try:
            tree_itens = tree_turma.focus()
            tree_dicionario = tree_turma.item(tree_itens)
            tree_lista = tree_dicionario["values"]
            
            valor_id = tree_lista[0]
            
            # Inserindo os valores na entries
            e_nome_turma.insert(0, tree_lista[1])
            c_curso.get(0)
            data_inicio.get(0)
            
            # Criando função atualizar
            def update():
                
                nome = e_nome_turma.get()
                curso = c_curso.get()
                data = data_inicio.get()
                
                lista = [nome, curso, data, valor_id]
                
                # Verificando se está vazio

                for i in lista:
                    if i=="":
                        messagebox.showerror("ERRO", "Prencha todos os campos!")
                        return
                    
                # Inserindo os dados
                atualizar_turma(lista)
            
                # Mostrando mensagem sucesso
                messagebox.showinfo("Sucesso", "Os dados preenchidos foram inseridos com êxito!")
                
                # Excluindo os valores
                e_nome_turma.destroy
                c_curso.destroy
                data_inicio.destroy
                
                # Mostrando os valores na tabela
                mostrar_turmas()    

                # Destruindo botão confirmar
                botao_salvar.destroy()

            # Botão Confirmar
            botao_salvar = Button(frame_detalhes, command=update, anchor=CENTER, text="salvar Atualização".upper(), overrelief=RIDGE, font=("Courier 7"), bg=co0, fg=co1)
            botao_salvar.place(x=706, y=135)
            
        except IndexError:
            messagebox.showerror("EERO", "Selecione um dos cursos na tabela!")
            
    # Função deletar turma
    def delete_turma():
        try:
            tree_itens = tree_turma.focus()
            tree_dicionario = tree_turma.item(tree_itens)
            tree_lista = tree_dicionario["values"]
            
            valor_id = tree_lista[0]

            # Deletar os dados do banco de dados
            deletar_turma([valor_id])
        
            # Mostrando mensagem sucesso
            messagebox.showinfo("Sucesso", "Os dados preenchidos foram deletados com êxito!")

            # Mostrando os valores na tabela
            mostrar_turmas()
            
        except IndexError:
            messagebox.showerror("ERRO", "Selecione um dos cursos na tabela!")
    
    
    # Caixa de texto do nome da turma
    l_nome = customtkinter.CTkLabel(master=frame_detalhes, text="", text_color="green")
    l_nome.place(x=404, y=19)
    e_nome_turma = customtkinter.CTkEntry(master=frame_detalhes, placeholder_text="Nome da turma", width=250, border_width=2, corner_radius=10, fg_color=co0)
    e_nome_turma.place(x=407, y=40)
    
    # Caixa de texto da Duração
    
    opcao = customtkinter.StringVar(value="Turmas")
    cursos = ver_cursos()
    curso = []
    for i in cursos:
        curso.append(i[1])
    c_curso = customtkinter.CTkComboBox(master=frame_detalhes, width=150, values=curso, variable=opcao, border_width=2, corner_radius=10, fg_color=co0)
    c_curso["values"] = (curso)
    c_curso.place(x=407, y=100) 
    
    
    # Caixa da Data
    l_data_inicio = Label(frame_detalhes, text="Data de Início: *", height=1, anchor=NW, font=("Courier 10"), bg=co1, fg=co4)
    l_data_inicio.place(x=404, y=139)
    data_inicio = DateEntry(frame_detalhes, width=23, background="black", foreground="white", borderwidth=1, year=2023)
    data_inicio.place(x=407, y=160)
    
    # Criando botões do frame TURMAS
    
    #Botão Salvar
    botao_carregar = customtkinter.CTkButton(frame_detalhes, command=nova_turma, anchor=CENTER, text="Novo".upper(), width=20, height=10, border_width=1, border_color="#000", bg_color=co1, hover_color=co3, fg_color=co0, corner_radius=10)
    botao_carregar.place(x=620, y=160)    
    
    #Botão Atualizar
    botao_atualizar = customtkinter.CTkButton(frame_detalhes, command=update_turma, anchor=CENTER, text="Atualizar".upper(), width=20, height=10, border_width=1, border_color="#000", bg_color=co1, hover_color=co6, fg_color=co0, corner_radius=10)
    botao_atualizar.place(x=670, y=160) 
    
    #Botão Deletar
    botao_deletar = customtkinter.CTkButton(frame_detalhes, command=deletar_turma, anchor=CENTER, text="Deletar".upper(), width=20, height=10, border_width=1, border_color="#000", bg_color=co1, hover_color=co7, fg_color=co0, corner_radius=10)
    botao_deletar.place(x=752, y=160)
    
    
    # Tabela TURMAS
    def mostrar_turmas():
        app_nome = Label(frame_tabela_turma, text="               Tabela de Turmas", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Courier 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # criando uma visualização em árvore com barras de rolagem duplas
        list_header = ['ID','Nome da Turma','Curso','Início']

        df_list = ver_turmas()
        
        global tree_turma
        tree_turma = ttk.Treeview(frame_tabela_turma, selectmode="extended",columns=list_header, show="headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_turma, orient="vertical", command=tree_turma.yview)
        # horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela_turma, orient="horizontal", command=tree_turma.xview)

        tree_turma.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_turma.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_turma.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","e","e"]
        h=[30,150,110,80]
        n=0

        for col in list_header:
            tree_turma.heading(col, text=col.title(), anchor=NW)
            # ajuste a largura da coluna para a string do cabeçalho
            tree_turma.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_turma.insert('', 'end', values=item)
    mostrar_turmas()
    

# Função para salvar ------------------------------------------------------
def salvar():
    print("Salvar")

# função de controle ------------------------------------------------------

def controle(i):
    # cadastro de alunos
    if i == "cadastro":
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        # Chamando a função alunos
        alunos()

    # Adicionar alunos
    if i == "adicionar":
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        # Chamando a função adicionar
        adicionar()
        
    # Salvar
    if i == "salvar":
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        # Chamando a função salvar
        salvar()


# Criando botões ----------------------------------------------------------

# Botão cadastro
app_img_cadastro = Image.open("add.png")
app_img_cadastro = app_img_cadastro.resize((18, 18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = customtkinter.CTkButton(frame_dados, command=lambda:controle("cadastro"), image=app_img_cadastro, text=" CADASTRO", width=120, compound=LEFT, border_width=3, border_color=co0, bg_color=co1, fg_color=co0, corner_radius=10)
app_cadastro.place(x=10, y=33)

# Botão adicionar
app_img_adicionar = Image.open("add.png")
app_img_adicionar = app_img_adicionar.resize((18, 18))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = customtkinter.CTkButton(frame_dados, command=lambda:controle("adicionar"), image=app_img_adicionar, text=" Adicionar".upper(), width=120, compound=LEFT, border_width=3, border_color=co0, bg_color=co1, fg_color=co0, corner_radius=10)
app_adicionar.place(x=135, y=33)


# Botão salvar
#app_img_salvar = Image.open("salvar.png")
#app_img_salvar = app_img_salvar.resize((18, 18))
#app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
#app_salvar = Button(frame_dados, command=lambda:controle("salvar"), image=app_img_salvar, text=" Salvar", width=100, compound=LEFT, relief=RAISED, overrelief=RIDGE, font=("Courier 10"), bg=co1, fg=co0)
#app_salvar.place(x=240, y=35)



# Executando a janela
alunos()

janela.mainloop()



# PARTE 18