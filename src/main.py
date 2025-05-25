import tkinter as tk
import tkinter.messagebox as messagebox
import sqlite3


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
    #Criando um botão para logar
    botao_login = tk.Button(janela_login, text="Logar", font=("Arial", 10), bg="black", fg="white", command=verificar_login)
    botao_login.pack(pady=5)
    botao_login.place(relx=0.5, rely=0.7, anchor="center")
    #Criando um botão para cancelar
    botao_cancelar = tk.Button(janela_login, text="Cancelar", font=("Arial", 10), bg="black", fg="white", command=janela_login.destroy)
    botao_cancelar.pack(pady=5)
    botao_cancelar.place(relx=0.5, rely=0.8, anchor="center")

    

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
hotel_submenu.add_command(label="Cadastro de Clientes")
hotel_submenu.add_command(label="Logar", command=logar)



#Mantendo a janela aberta
janela.mainloop()

