import os
import webbrowser
from tkinter import *
import sqlite3
from PIL import ImageTk,Image

root = Tk()
root.title(" DB Acess ")
root.geometry("276x300")
im = PhotoImage(file = "icon.png")
root.iconphoto(False,im)
#Database
#Create connection One time 
conn = sqlite3.connect('database.db')
c = conn.cursor()

  
def submit():
    search = Tk()
    search.title("Search")
    search.geometry("276x300")

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    def search_link():
        searched = search_box.get()
        sql = "SELECT lien FROM LINKS WHERE number = "+ searched

        result = c.execute(sql)
        result = c.fetchall()
        if not result:
            result = "Record Not found ....."
            searched_label = Label(search, text=result)
            searched_label.grid(row=2, column=0 ,padx=10) 
        else:
           r = result[0]
           os.startfile(r[0])

          
    # Entry box to search
    search_box =  Entry(search)
    search_box.grid(row=0, column=1, padx=10, pady=10)
    # Entry box label 
    search_box_label = Label(search, text=" Enter the Code :")
    search_box_label.grid(row=0, column=0, padx=10,pady=10)
    # Entry search button
    search_button = Button(search,text="Ouvrir", command= search_link)
    search_button.grid(row=1, column=0, padx=10)
def Refresh():
    refresh = Tk()
    refresh.title("Add")
    refresh.geometry("276x300")
    def ajouter():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        sqlite_insert_query = '''INSERT INTO LINKS (number, lien) VALUES (?,?)''' 
        #req = sqlite_insert_query + "("+str(f_num) +","+ str(f_link)+")" 
        n = f_num.get()
        l = f_link.get()
        data = (n,l)
        res = c.execute(sqlite_insert_query, data)
        print(res)
        conn.commit()

    f_num = Entry(refresh, width=30)
    f_num.grid(row=1, column=0, padx=20)
    f_link = Entry(refresh, width=30)
    f_link.grid(row=3, column=0, padx=20)

    f_num_label = Label(refresh, text="Archive N°")
    f_num_label.grid(row=0, column=0)
    f_link_label = Label(refresh, text="Repository link")
    f_link_label.grid(row=2, column=0)

    search_button = Button(refresh,text="Add", command= ajouter)
    search_button.grid(row=4, column=0, padx=10)

    

img = ImageTk.PhotoImage(Image.open("img.jpg"))
Label(root, image=img).grid(row=0, column=1,sticky = NW)

submit_button = Button(root, text="Access", command=submit)
submit_button.grid(row=8,column=0, columnspan=2, pady=10, padx=10, ipadx=100)

refresh_button = Button(root, text="Mise à jour", command=Refresh)
refresh_button.grid(row=9,column=0, columnspan=2, pady=10, padx=10, ipadx=96)



conn.commit()
conn.close()
root.mainloop()
