#!/usr/bin/python
# -*- coding: latin-1 -*-
from Tkinter import *
import subprocess
import tkMessageBox
import ttk
import sqlite3


############################################ definition des fonctions ####################################
def displayLog(): # Affiche le fichier de log souhaité en récupérant le chemin dans la variable logPath


	logPrint = subprocess.Popen(["tail",logPath.get()], stdout=subprocess.PIPE)
	output = logPrint.communicate()[0]
	displayLogInLabel.set(output)

def getDBPath() : # récupére le chemin du fichier de log selectionné dans la base de donnée log.db

	connexion = sqlite3.connect("dataBase/log.db") #connexion à la base de donnée
	curseur = connexion.cursor()
	name = lb.get(lb.curselection())
	curseur.execute("SELECT chemin FROM logFiles WHERE nom LIKE '%s'" % name)
	record = curseur.fetchone()
	logPath.set(record[0]) 
	connexion.close()
	displayLog()

def databaseCreation () :# Création de la base de donnée si elle n'existe pas

	connexion = sqlite3.connect("dataBase/log.db") #connexion à la base de donnée
	curseur = connexion.cursor()
	curseur.execute('''CREATE TABLE IF NOT EXISTS logFiles (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, chemin TEXT, nom TEXT)''') # création de la table logFiles
	connexion.close()

def databaseAdd (): # Ajout d'une valeur dans la base de donnée ( chemin plus le nom associé )

	connexion = sqlite3.connect("dataBase/log.db") #connexion à la base de donnée
	curseur = connexion.cursor()
	donnees = (newLogPath.get(),logPathName.get())
	curseur.execute('''INSERT INTO logFiles (chemin, nom ) VALUES (?,?)''',donnees)
	connexion.commit()
	tkMessageBox.showinfo("Succes", "The log file is saved in the database")
	connexion.close()
	newLogPath.set("")
	logPathName.set("")
	listboxIntegration()



def listboxIntegration () : # Intégration des valeur de la base de donnée dans la listeBox

	connexion = sqlite3.connect("dataBase/log.db") #connexion à la base de donnée
	curseur = connexion.cursor()
	curseur.execute("SELECT nom FROM logFiles") # Récupération des valeurs "nom" dans la base de donnée pour l'insérer dans la listeBox
	i=0
	for row in curseur.fetchall():
		lb.insert(i,row[0])
		i=i+1
	connexion.close() # fermeture de la base de donnée

####################################### MAIN #######################################

		
winlog = Tk() # Les lignes suivantes définissent l'interface graphique de la fenêtre principale
displayLogInLabel = StringVar()
frame_down = Frame (winlog,height=800,width=1000,relief=RAISED,bd=8,bg="black")
frame_up = Frame (winlog,height=100,width=1000,bd=8,bg="white")
frame_down.grid(row=1,column=0)
frame_up.grid(row=0,column=0)
winlog.title("Configurer des routes")
winlog.configure(bg='#ffffff')
winlog.geometry("1000x500")
winlog.resizable(width=False,height=False)

### Définition des variables

newLogPath = StringVar()
newLogPath.set('')
logPathName = StringVar()
logPathName.set('')
logPath = StringVar()
logPath.set('')

### création de la listbox pour choisir le log à afficher ###

lb = Listbox(frame_up, height =2)
lb.grid(row=2,column=1)

### Dés le lancement de la fenêtre la base de donnée et la listBox se mettent à jour

databaseCreation ()
listboxIntegration ()


### ajout des label et des textbox

labelLog = Label(frame_up, text="Add the path to the log file to save :", foreground='white',bg='#1d83ff')
labelLog.grid(row=1,column=0)
entryLog = Entry(frame_up,textvariable=newLogPath)
entryLog.grid(row=1,column=1)
emptyLabel = Label(frame_up,text="  ",bg='#ffffff')
emptyLabel.grid(row=1,column=2)

labelName = Label(frame_up, text="Give it a name", foreground='white',bg='#1d83ff')
labelName.grid(row=1,column=3)
entryName = Entry(frame_up,textvariable=logPathName)
entryName.grid(row=1,column=4)

emptyLabel1 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les éléments
emptyLabel1.grid(row=1,column=5)

saveButton=Button(frame_up,command=databaseAdd)
saveButton.grid(row=1,column=6)
saveButtonImg = PhotoImage(file="pictures/buttonAdd2.gif")
saveButton.config(image=saveButtonImg)
saveButton.image = saveButtonImg

labelName = Label(frame_up, text="Choose the log file to show :", foreground='white',bg='#6a8bff')
labelName.grid(row=2,column=0)


displayButton=Button(frame_up, command=getDBPath)
displayButton.grid(row=2,column=2)
displayButtonImg = PhotoImage(file="pictures/afficher.gif")
displayButton.config(image=displayButtonImg)
displayButton.image = displayButtonImg

##################################### partie inférieure frame_up #######################################

labelDown = Label(frame_down,textvariable=displayLogInLabel)
labelDown.place(x=0,y=0)
labelDown.configure(foreground="white",bg='#000000')
displayLogInLabel.set("")

winlog.mainloop()	

		