import tkinter as tk
import tkinter.messagebox as messagebox
import sqlite3



#criando uma função para cadastrar clientes
def cadastrar_cliente():
    #Criando uma nova janela
    janela_cadastrar_cliente = tk.Toplevel(janela)
    janela_cadastrar_cliente.title("Cadastro de Clientes")
    janela_cadastrar_cliente.geometry("400x500")
    janela_cadastrar_cliente.configure(bg="black")
    janela_cadastrar_cliente.resizable(False, False)
    #Titulo grande centralizado no topo da tela
    titulo_cadastrar_cliente = tk.Label(janela_cadastrar_cliente, text="Cadastro de Clientes", font=("Arial", 20), bg="black", fg="white")
    titulo_cadastrar_cliente.pack(pady=20)
    titulo_cadastrar_cliente.place(relx=0.5, rely=0.05, anchor="center")
    #Criando um lable para o nome
    label_nome = tk.Label(janela_cadastrar_cliente, text="Nome", font=("Arial", 10), bg="black", fg="white")
    label_nome.pack(pady=5)
    label_nome.place(relx=0.5, rely=0.15, anchor="center")
    #Criando um entry para o nome
    entry_nome = tk.Entry(janela_cadastrar_cliente, font=("Arial", 10), width=30)
    entry_nome.pack(pady=5)
    entry_nome.place(relx=0.5, rely=0.25, anchor="center")
    #Criando um lable para o cpf
    label_cpf = tk.Label(janela_cadastrar_cliente, text="CPF", font=("Arial", 10), bg="black", fg="white")
    label_cpf.pack(pady=5)
    label_cpf.place(relx=0.5, rely=0.35, anchor="center")
    #Criando um entry para o cpf
    entry_cpf = tk.Entry(janela_cadastrar_cliente, font=("Arial", 10))
    entry_cpf.pack(pady=5)
    entry_cpf.place(relx=0.5, rely=0.45, anchor="center")
    #Criando um lable para o telefone
    label_telefone = tk.Label(janela_cadastrar_cliente, text="Telefone", font=("Arial", 10), bg="black", fg="white")
    label_telefone.pack(pady=5)
    label_telefone.place(relx=0.5, rely=0.55, anchor="center")
    #Criando um entry para o telefone
    entry_telefone = tk.Entry(janela_cadastrar_cliente, font=("Arial", 10))
    entry_telefone.pack(pady=5)
    entry_telefone.place(relx=0.5, rely=0.65, anchor="center")
    #Criando um lable para o endereço
    label_endereco = tk.Label(janela_cadastrar_cliente, text="Endereço", font=("Arial", 10), bg="black", fg="white")
    label_endereco.pack(pady=5)
    label_endereco.place(relx=0.5, rely=0.75, anchor="center")
    #Criando um entry para o endereço
    entry_endereco = tk.Entry(janela_cadastrar_cliente, font=("Arial", 10), width=30)
    entry_endereco.pack(pady=5)
    entry_endereco.place(relx=0.5, rely=0.85, anchor="center")
    #Criando um frame para os botões
    frame_botoes = tk.Frame(janela_cadastrar_cliente, bg="black")
    frame_botoes.place(relx=0.5, rely=0.95, anchor="center")
    
    def cadastrar():
        #Pegando os dados dos entries
        nome = entry_nome.get()
        cpf = entry_cpf.get()
        telefone = entry_telefone.get()
        endereco = entry_endereco.get()
        #Verificando se os campos estão preenchidos
        if not nome or not cpf or not telefone or not endereco:
            messagebox.showerror("Erro", "Preencha todos os campos")
            return
        #Conectando ao banco de dados
        conn = sqlite3.connect('c:/python/projeto1/bd/hotel.db')
        c = conn.cursor()
        #Inserindo os dados na tabela de clientes
        c.execute('''INSERT INTO clientes (nome, cpf, telefone, endereco) VALUES (?, ?, ?, ?)''', (nome, cpf, telefone, endereco))
        #Salvando as alterações
        conn.commit()
        #Fechando a conexão
        conn.close()
        #Messagebox de sucesso
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso")
        print("Cliente cadastrado com sucesso")
        #Fechando a janela de cadastro
        janela_cadastrar_cliente.destroy()
    #Criando um botão para cadastrar
    botao_cadastrar = tk.Button(frame_botoes, text="Cadastrar", font=("Arial", 10), bg="black", fg="white", width=12, command=cadastrar)
    botao_cadastrar.pack(side=tk.LEFT, padx=10)
    #criando um botão para cancelar
    botao_cancelar = tk.Button(frame_botoes, text="Cancelar", font=("Arial", 10), bg="black", fg="white", command=janela_cadastrar_cliente.destroy, width=12)
    botao_cancelar.pack(side=tk.LEFT, padx=10)    
        


#Criando um botão para logar na area administrativa
def logar():
    
    #Criando uma função para verificar o login
    def verificar_login():
        #Hash da senha
        hash_armazenado = "0b955572716abc2aed6f8659a93b0f6c81cd168ec67e518cd556053e5d8f1f07"
        #Função para verificar a hash
        def verificar_hash(senha):
            import hashlib
            
            #Comparando a hash
            hash_senha = hashlib.sha256(senha.encode()).hexdigest()
            if hash_senha == hash_armazenado:
                #Messagebox de sucesso
                messagebox.showinfo("login", "Login correto")
                print("login correto")
                janela_login.destroy()
                area_administrativa()
            else:
                #Messagebox de erro
                messagebox.showerror("login", "Login incorreto")
                print("login incorreto")
                janela_login.destroy()

        #Pegando o usuario e a senha
        usuario = entry_login_usuario.get()
        if usuario != "grilo":
            print("usuario incorreto")
            janela_login.destroy()
            return
        senha = verificar_hash(entry_login_senha.get())
        #verificando o login    
    
    #Criando uma nova janela
    janela_login = tk.Toplevel(janela)
    janela_login.title("Login")
    janela_login.geometry("400x300")
    janela_login.configure(bg="black")
    janela_login.resizable(False, False)
    #criando um lable para o login
    label_login = tk.Label(janela_login, text="Login", font=("Arial", 20), bg="black", fg="white")
    label_login.pack(pady=20)
    label_login.place(relx=0.5, rely=0.1, anchor="center")
    #Criando um lable para o usuario
    label_login_usuario = tk.Label(janela_login, text="Usuário", font=("Arial",10 ), bg="black", fg="white")
    label_login_usuario.pack(pady=5)
    label_login_usuario.place(relx=0.5, rely=0.3, anchor="center")
    #Criando um entry para o usuario
    entry_login_usuario = tk.Entry(janela_login, font=("Arial", 10))
    entry_login_usuario.pack(pady=5)
    entry_login_usuario.place(relx=0.5, rely=0.4, anchor="center")
    #Criando um lable para a senha
    label_login_senha = tk.Label(janela_login, text="Senha", font=("Arial", 10), bg="black", fg="white")
    label_login_senha.pack(pady=5)
    label_login_senha.place(relx=0.5, rely=0.5, anchor="center")
    #Criando um entry para a senha
    entry_login_senha = tk.Entry(janela_login, font=("Arial", 10), show="*")
    entry_login_senha.pack(pady=5)
    entry_login_senha.place(relx=0.5, rely=0.6, anchor="center")
    #criando um frame para os botões
    frame_botoes = tk.Frame(janela_login, bg="black")
    frame_botoes.place(relx=0.5, rely=0.75, anchor="center")
    #Criando um botão para logar
    botao_login = tk.Button(frame_botoes, text="Logar", font=("Arial", 10), bg="black", fg="white", command=verificar_login, width=10)
    botao_login.pack(side=tk.LEFT, padx=10)
    #Criando um botão para cancelar
    botao_cancelar = tk.Button(frame_botoes, text="Cancelar", font=("Arial", 10), bg="black", fg="white", command=janela_login.destroy, width=10)
    botao_cancelar.pack(side=tk.LEFT, padx=10)

    

#Criando o banco de dados
conn = sqlite3.connect('c:/python/projeto1/bd/hotel.db')
c = conn.cursor()
#Criando a tabela de quartos
c.execute('''CREATE TABLE IF NOT EXISTS quartos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero INTEGER NOT NULL,
                tipo TEXT NOT NULL,
                preco REAL NOT NULL)''')
#Criando a tabela de clientes
c.execute('''CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL,
                telefone TEXT NOT NULL,
                endereco TEXT NOT NULL)''')
#Criando a tabela de hospedagem
c.execute('''CREATE TABLE IF NOT EXISTS hospedagem (
                id_hospedagem INTEGER PRIMARY KEY AUTOINCREMENT,
                id_clente INTEGER NOT NULL,
                id_quarto INTEGER NOT NULL,
                pessoas INTEGER NOT NULL,
                data_entrada TEXT NOT NULL,
                data_saida TEXT NOT NULL,
                valor_total REAL NOT NULL )''')
#Criando a tabela de funcionarios
c.execute('''CREATE TABLE IF NOT EXISTS funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL,
                senha PASSWORD NOT NULL,
                telefone TEXT NOT NULL,
                endereco TEXT NOT NULL)''')


#Criando uma janela
janela = tk.Tk()
janela.title("Hotel Mato Grosso")
janela.geometry("400x400")
janela.configure(bg="black")
janela.resizable(False, False)

#Titulo grande centralizado no topo da tela
titulo = tk.Label(janela, text="Hotel Mato Grosso", font=("Arial", 20), bg="black", fg="white")
titulo.pack(pady=20)
titulo.place(relx=0.5, rely=0.1, anchor="center")

#Criando uma barra de menu
menu = tk.Menu(janela)
janela.config(menu=menu)
#Criando um menu
submenu = tk.Menu(menu)
hotel_submenu = tk.Menu(menu)
menu.add_cascade(label="Menu", menu=submenu)
submenu.add_command(label="Sobre")
submenu.add_command(label="Sair", command=janela.quit)
submenu.add_command(label="Ajuda")
submenu.add_command(label="Configurações")
menu.add_cascade(label="Hotel", menu=hotel_submenu)
hotel_submenu.add_command(label="Cadastro de Clientes", command=cadastrar_cliente)
hotel_submenu.add_command(label="Logar", command=logar)

#criando uma nova janela para área administrativa
def area_administrativa():
    janela_admin = tk.Toplevel(janela)
    janela_admin.title("Área Administrativa")
    janela_admin.geometry("400x400")
    janela_admin.configure(bg="black")
    janela_admin.resizable(False, False)
    #Titulo grande centralizado no topo da tela
    titulo_admin = tk.Label(janela_admin, text="Área Administrativa", font=("Arial", 20), bg="black", fg="white")
    titulo_admin.pack(pady=20)
    titulo_admin.place(relx=0.5, rely=0.1, anchor="center")
    
#Mantendo a janela aberta
janela.mainloop()

