from tkinter import *
from tkinter import messagebox

root = Tk()

contas = [['Moser','Moser123'],['Millena','miih']]

def cadastrar(login,senha):
    conta = [login,senha]
    contas.append(conta)
    janela_cadastro.destroy()
    print(conta)
    print(contas)

def logar(login, senha):
    for conta in contas:
        login_inside = conta[0]
        senha_inside = conta[1]

    if login == login_inside:
        if senha == senha_inside:
            messagebox.showinfo('Parabens', 'Voce logou no sistema')
            root.destroy()
        else:
            messagebox.showerror('', 'Senha Invalida')
    else:
        messagebox.showerror('', 'Login Invalido')

def cadastro():
    

    global janela_cadastro
    janela_cadastro = Toplevel()
    cadastro = Label(janela_cadastro,text='Login').grid(row=0,column=0)
    senha = Label(janela_cadastro,text='Senha').grid(row=1,column=0)
    cadastro_input = Entry(janela_cadastro)
    senha_input = Entry(janela_cadastro)
    senha_input.grid(row=0,column=1)
    cadastro_input.grid(row=1,column=1)
    botao_cadastrar = Button(janela_cadastro,text='CADASTRAR',command=lambda:cadastrar(cadastro_input.get(),senha_input.get()))
    botao_cadastrar.grid(row=2,columnspan=3)


texto_login = Label(root, text='Nome').grid(row=0, column=0)
texto_senha = Label(root, text='Senha').grid(row=1, column=0)
s = Entry(root,show='*')
l = Entry(root)
l.grid(row=0, column=1)
s.grid(row=1, column=1)


botao_login = Button(root, text='LOGIN',command=lambda : logar(l.get(),s.get()))
botao_cadastro = Button(root,text='CADASTRAR',command=cadastro).grid(row=3,column=1)
botao_login.grid(row=3,column=0)


root.mainloop()