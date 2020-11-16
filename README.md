# Access
Access DB [ PK - Repository link ]
To try this code you will have to have an archive repository with folders 
inside that seperates folders depending on numbers for example : 
/Folder 00 - 40 
  ../Foldername-2020-01
  ../Foldername-2020-20
  ../Foldername-2020-39
/Folder 41 - 70 
  ../Foldername-2020-50
  ../Foldername-2020-65
  ../Foldername-2020-69
/Folder 71 - 100
  ../Foldername-2020-86
***************************************************************************
Anyway first you start by making your database of links and special numbers 
by launching "base.py"
/> python base.py
This will make a "database.db" 
***************************************************************************
Now you can launch app.py and access any folder of those in the database.
In case you have a new folder you can manually add the link to the repository
and it's number.
/> python app.py

To convert the app to .exe you will have to download pyinstaller and add noconsole
option and there you go.
