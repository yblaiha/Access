import sqlite3
import os
import webbrowser
import re

#Path to the repository of many repositories that will be in the database 
#For example :
#path = 'C:\\Users\\Joe\\Desktop\\Archive'
#Don't forget \\

path = ' XXXXX '
list_subfolders = [f.path for f in os.scandir(path) if f.is_dir()]

# List des liens
liens = []
# Les codes d'archives
codeArchive = []

for i in list_subfolders:
    list_subsub = [f.path for f in os.scandir(i) if f.is_dir()]
    for j in list_subsub:
        liens.append(j)
        n = [int(s) for s in re.findall(r'-?\d+\.?\d*',j)]
        newCode = n[4]*-1
        codeArchive.append(newCode)

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("""CREATE TABLE LINKS (
        number integer,
        lien text
        )""") 
count = 0
for i in liens:
    tmp2 = codeArchive[count]
    count += 1
    sqlite_insert_query = """INSERT INTO LINKS
                          (number, lien) 
                           VALUES 
                          (?,?);"""
    data = (tmp2,i)
    c.execute(sqlite_insert_query,data)
    conn.commit()

conn.commit()
conn.close()
