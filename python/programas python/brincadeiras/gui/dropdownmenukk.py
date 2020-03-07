from tkinter import *
import tkinter.messagebox


def donothing():
    print('OK OK')

root = Tk()

menu = Menu(root)
root.config(menu=menu)


submenu = Menu(menu)#criando o menu (aquele superior)
menu.add_cascade(label='file',menu=submenu)#adicionando uma item no menu daqueles que quando clica descem mais opçoes
submenu.add_command(label='now project',command=donothing)#adiciona um comando ao submenu
submenu.add_separator()#adiciona uma linha separadora no submenu
submenu.add_command(label='exit',command=donothing)#adiciona outro comando no submenu

editmenu = Menu(menu)#cria outro menu
menu.add_cascade(label='edit',menu=editmenu)#adiciona o menu como uma cascata de opçoes (como antes)
editmenu.add_command(label='redo',command=donothing)#adiciona uma opçao que faz um comando

toolbar = Frame(root,bg='blue')

inserbutt = Button(toolbar,text='Insert image',command=donothing)
inserbutt.pack(side=LEFT,padx=2,pady=2)
printbutton = Button(toolbar,text='Insert image',command=donothing)
printbutton.pack(side=LEFT)
toolbar.pack(side=TOP,fill=X)

#status bar

status = Label(root,text='doing nothing....',bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

root.mainloop()