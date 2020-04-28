from tkinter import *


class botoes:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printbutton = Button(frame,text='Print message',command=self.printmessage)
        self.printbutton.pack()

        self.quitbutton = Button(frame,text='quit ',command=frame.quit)
        self.quitbutton.pack()


    def printmessage(self):
        print('mensagem')


root = Tk()
b = botoes(root)
root.mainloop()