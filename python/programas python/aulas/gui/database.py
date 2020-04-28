from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.geometry('350x400')

#database


#create database or connect with
conn = sqlite3.connect('addres_book.db')


#create cursor
c = conn.cursor()


#create table
'''
c.execute("""CREATE TABLE addresses (
        First_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
            )""")
'''

#func to delete a record
def delete():
    # create database or connect with
    conn = sqlite3.connect('addres_book.db')
    # create cursor
    c = conn.cursor()

    #delete record
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    # commit changes
    conn.commit()
    # close connection
    conn.close()

#submit function
def submit():
    # create database or connect with
    conn = sqlite3.connect('addres_book.db')
    # create cursor
    c = conn.cursor()

    #inserir na table
    c.execute('INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)',
              {
                  'f_name':f_name.get(),
                  'l_name':l_name.get(),
                  'address':address.get(),
                  'city':city.get(),
                  'state':state.get(),
                  'zipcode':zipcode.get()
              })



    # commit changes
    conn.commit()
    # close connection
    conn.close()


    f_name.delete(0,END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    # create database or connect with
    conn = sqlite3.connect('addres_book.db')
    # create cursor
    c = conn.cursor()

    #query the database
    c.execute('SELECT *,oid FROM addresses')
    records = c.fetchall()
    #print(records)

    print_records = ''
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1])  + '\t ' + str(record[6]) + '\n'

    query_label = Label(root,text=print_records).grid(row=12,column=0,columnspan=2)
    # commit changes
    conn.commit()
    # close connection
    conn.close()
# Edit funcion to uptade records

def update():
    #create database or connect with
    conn = sqlite3.connect('addres_book.db')
    #create cursor
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute('''UPDATE addresses SET
    first_name = :first,
    last_name= :last,
    address= :address,
    city = :city,
    state = :state,
    zipcode = :zipcode

    WHERE oid = :oid''',
    {
    'first': f_name.get(),
    'last': l_name.get(),
    'address':address.get(),
    'city': city.get(),
    'state':state.get(),
    'zipcode':zipcode.get(),
    'oid':record_id
    })


    #commit changes
    conn.commit()
    #close connection
    conn.close()

    editor.destroy()
    
def edit():
    global editor
    editor = Tk()
    editor.geometry('350x400')
    editor.title('Editar record')
    
    # create database or connect with
    conn = sqlite3.connect('addres_book.db')
    # create cursor
    c = conn.cursor()

    record_id = delete_box.get()

    #query the database
    c.execute("SELECT *,oid FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
    
    global f_name
    global l_name
    global address
    global city
    global state
    global zipcode

    #create text boxes
    f_name = Entry(editor,width=30)
    f_name.grid(row=0,column=1,padx=20,pady=(10,0),columnspan=2)
    l_name = Entry(editor,width=30)
    l_name.grid(row=1,column=1,padx=20,columnspan=2)
    address = Entry(editor,width=30)
    address.grid(row=2,column=1,padx=20,columnspan=2)
    city = Entry(editor,width=30)
    city.grid(row=3,column=1,padx=20,columnspan=2)
    state = Entry(editor,width=30)
    state.grid(row=4,column=1,padx=20,columnspan=2)
    zipcode = Entry(editor,width=30)
    zipcode.grid(row=5,column=1,padx=20,columnspan=2)

    #create text box labels
    f_name_label = Label(editor,text='First name').grid(row=0,column=0,pady=(10,0))
    l_name_label = Label(editor,text='Last name').grid(row=1,column=0)
    address_label = Label(editor,text='Address').grid(row=2,column=0)
    city_label = Label(editor,text='City').grid(row=3,column=0)
    state_label = Label(editor,text='State').grid(row=4,column=0)
    zipcode_label = Label(editor,text='Zipcode').grid(row=5,column=0)
     
    #save button
    save_btn = Button(editor,text='edit',command=update).grid(row=6,column=0,padx=10,pady=10)

    for record in records:
        f_name.insert(0,record[0])
        l_name.insert(0,record[1])
        address.insert(0,record[2])
        city.insert(0,record[3])
        state.insert(0,record[4])
        zipcode.insert(0,record[5])


#create text boxes
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0),columnspan=2)
l_name = Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20,columnspan=2)
address = Entry(root,width=30)
address.grid(row=2,column=1,padx=20,columnspan=2)
city = Entry(root,width=30)
city.grid(row=3,column=1,padx=20,columnspan=2)
state = Entry(root,width=30)
state.grid(row=4,column=1,padx=20,columnspan=2)
zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20,columnspan=2)
delete_box = Entry(root,width=30)
delete_box.grid(row=10,column=1,columnspan=2)

delete_box_label = Label(root,text='ID#')
delete_box_label.grid(row=10,column=0)

#create text box labels
f_name_label = Label(root,text='First name').grid(row=0,column=0,pady=(10,0))
l_name_label = Label(root,text='Last name').grid(row=1,column=0)
address_label = Label(root,text='Address').grid(row=2,column=0)
city_label = Label(root,text='City').grid(row=3,column=0)
state_label = Label(root,text='State').grid(row=4,column=0)
zipcode_label = Label(root,text='Zipcode').grid(row=5,column=0)

#submit button
submit_btn = Button(root,text='add record to DataBase',command=submit)
submit_btn.grid(row=6,column=0,columnspan=3,pady=10,padx=10,ipadx=100)

#query button
query = Button(root,text='show records',command=query).grid(row=7,column=0,
                                                            padx=10,pady=10)
#delete button

delete_btn = Button(root,text='delete',command=delete).grid(row=7,column=1,
                                                            padx=10,pady=10)

#criar botao para editar
edit_btn = Button(root,text='edit',command=edit).grid(row=7,column=2,
                                                            padx=10,pady=10)



#commit changes
conn.commit()
#close connection
conn.close()

root.mainloop()