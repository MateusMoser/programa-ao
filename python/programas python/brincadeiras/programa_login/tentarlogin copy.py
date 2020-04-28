from tkinter import *
from tkinter import messagebox
import pandas as pd
import openpyxl


root = Tk()
users_path = 'C:\\Users\\moser\\Documents\\programaçao\\python\\programas python\\brincadeiras\\programacomlogin\\userscad.xlsx'
contas = pd.read_excel(r"C:\Users\moser\Documents\programaçao\python\programas python\brincadeiras\programacomlogin\userscad.xlsx")


def cadastrar(login,senha):
    book = openpyxl.load_workbook(users_path)
    sheet = book.active
    cont2 = 1
    while True:
        if sheet.cell(row=cont2, column=1).value == None:
            sheet['A'+str(cont2)] = login
            sheet['B'+str(cont2)] = senha  
            break      
        cont2 += 1
    book.save(users_path)
    global contas
    contas = pd.read_excel(r"C:\Users\moser\Documents\programaçao\python\programas python\brincadeiras\programacomlogin\userscad.xlsx")
    janela_cadastro.destroy()

def logar(login, senha):
    passww = ' '
    user = ' '
    cont = -1
    
    try:
        while user != login:
            cont += 1
            user = contas.iloc[cont,0]
    except IndexError:
        print('LOGIN ERRADO AMIGAO CIRCULANDO')
        messagebox.showwarning('','LOGIN ERRADO AMIGAO CIRCULANDO')
    if user == login:
        passw = senha

        try:
            passww = contas.iloc[cont,1]
            if passww == passw:
                messagebox.showinfo('','VOCE TA DENTRO PARCEIRO')

        except:
            messagebox.showwarning('','SENHA ERRADA AMIGAO CIRCULANDO')
                

def cadastro():
    

    global janela_cadastro
    janela_cadastro = Toplevel()
    cadastro = Label(janela_cadastro,text='Login').grid(row=0,column=0)
    senha = Label(janela_cadastro,text='Senha').grid(row=1,column=0)
    cadastro_input = Entry(janela_cadastro)
    senha_input = Entry(janela_cadastro)
    senha_input.grid(row=1,column=1)
    cadastro_input.grid(row=0,column=1)
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