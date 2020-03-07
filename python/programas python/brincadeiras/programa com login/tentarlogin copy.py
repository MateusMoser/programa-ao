from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('contas.db')

root = Tk()

contas = [['Moser','123'],['Millena','miih2'],['mateus','melado']]
#Criando funçoes
#funçao para a criaçao de contas
def cadastrar(login,senha):
    conta = [login,senha]
    contas.append(conta)
    janela_cadastro.destroy()


#validaçao da conta
def logar(login, senha):
        for conta in contas:
            login_inside = conta[0]
            senha_inside = conta[1]
        if login == login_inside and senha_inside == senha:
                messagebox.showinfo('Parabens', 'Voce logou no sistema')
                root.destroy()
        else:
            messagebox.showerror('', 'Login ou senha Invalidos')

#criaçao da janela para cadastro
def cadastro():
    global janela_cadastro
    janela_cadastro = Toplevel()
    
    cadastro = Label(janela_cadastro,text='Login').grid(row=0,column=0)
    senha = Label(janela_cadastro,text='Senha').grid(row=1,column=0)
    
    Login_info = Entry(janela_cadastro)
    senha_info = Entry(janela_cadastro)

    senha_info.grid(row=0,column=1)
    Login_info.grid(row=1,column=1)

    botao_cadastrar = Button(janela_cadastro,text='CADASTRAR',command=lambda:cadastrar(Login_info.get(),senha_info.get()))
    botao_cadastrar.grid(row=2,columnspan=3)


texto_login = Label(root, text='Nome:').grid(row=0, column=0,sticky=E)
texto_senha = Label(root, text='Senha:').grid(row=1, column=0,sticky=E)
s = Entry(root,show='*',width=35)
l = Entry(root,width=35)
l.grid(row=0, column=1,columnspan=2)
s.grid(row=1, column=1,columnspan=2)

botao_login = Button(root, text='LOGIN',command=lambda : logar(l.get(),s.get()))
botao_cadastro = Button(root,text='CADASTRAR',command=cadastro).grid(row=3,column=1,sticky=W)
botao_login.grid(row=3,column=0)
manterlogado = Checkbutton(root,text='Mantenha-me \n logado').grid(row=3,column=2)

root.mainloop()