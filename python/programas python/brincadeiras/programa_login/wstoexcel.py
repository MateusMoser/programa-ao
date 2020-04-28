import openpyxl

users_path = 'C:\\Users\\moser\\Documents\\programaçao\\python\\programas python\\brincadeiras\\programacomlogin\\userscad.xlsx'



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

cadastrar('Perola','perola_gatinha')
