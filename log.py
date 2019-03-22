#!/usr/bin/python
# -*- coding: latin-1 -*-
from Tkinter import *
import subprocess
import sqlite3


############################################ definition des fonctions ####################################
def ajoutDB ():
	## gestion de la base de donnée log.db

	connexion = sqlite3.connect("dataBase/log.db") #connexion à la base de donnée
	donnees = (nouveau_chemin_log.get(),nom_chemin_log.get())
	curseur.execute('''INSERT INTO logFiles (chemin, nom ) VALUES (?,?)''',donnees)
	connexion.close()
	
def log() :


	logPrint = subprocess.Popen(["tail",cheminLog], stdout=subprocess.PIPE)
	output = logPrint.communicate()[0]
	print(output)
	log_label.set(output)


####################################### Fenêtre secondaire log #######################################

		
winlog = Tk()

log_label = StringVar()
frame_down = Frame (winlog,height=800,width=1000,relief=RAISED,bd=8,bg="black")
frame_up = Frame (winlog,height=100,width=1000,bd=8,bg="white")
frame_down.grid(row=1,column=0)
frame_up.grid(row=0,column=0)
winlog.title("Configurer des routes")
winlog.configure(bg='#ffffff')
winlog.geometry("1000x500")
winlog.resizable(width=False,height=False)

### Définition des variables
nouveau_chemin_log = StringVar()
nouveau_chemin_log.set('')

nom_chemin_log = StringVar()
nom_chemin_log.set('')

### gestion de la base de donnée
connexion = sqlite3.connect("dataBase/log.db") #connexion à la base de donnée

curseur.execute('''CREATE TABLE IF NOT EXISTS logFiles (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, chemin TEXT, nom TEXT)''') # création de la table logFiles
connexion.close()

### ajout du label et du textbox

labelLog = Label(frame_up, text="Ajouter un fichier de log :", foreground='white',bg='#1d83ff')
labelLog.grid(row=1,column=0)
entryLog = Entry(frame_up,textvariable=nouveau_chemin_log)
entryLog.grid(row=1,column=1)
labelVide = Label(frame_up,text="  ",bg='#ffffff')
labelVide.grid(row=1,column=2)

labelName = Label(frame_up, text="Donnez-lui un nom", foreground='white',bg='#1d83ff')
labelName.grid(row=1,column=3)
entryName = Entry(frame_up,textvariable=nom_chemin_log)
entryName.grid(row=1,column=4)

labelVide = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les éléments
labelVide.grid(row=1,column=5)

buttonEnregistrer=Button(frame_up,command=ajoutDB)
buttonEnregistrer.grid(row=1,column=6)
buttonAddImg = PhotoImage(file="pictures/buttonAdd2.gif")
buttonEnregistrer.config(image=buttonAddImg)
buttonEnregistrer.image = buttonAddImg

labelName = Label(frame_up, text="Sélectionnez un Log:", foreground='white',bg='#6a8bff')
labelName.grid(row=2,column=0)

### création de la listbox pour choisir le log à afficher ###


lb = Listbox(frame_up, height =2)
lb.insert(0, "syslog")
lb.insert(1,"message")
lb.select_set(0)
lb.grid(row=2,column=1)


selectItem = lb.get(lb.curselection())

cheminLog=dc[selectItem]
print cheminLog

buttonAfficher=Button(frame_up, command=log)
buttonAfficher.grid(row=2,column=2)
afficherImg = PhotoImage(file="pictures/afficher.gif")
buttonAfficher.config(image=afficherImg)
buttonAfficher.image = afficherImg

##################################### partie inférieure frame_up #######################################

labelDown = Label(frame_down,textvariable=log_label)
labelDown.place(x=0,y=0)
labelDown.configure(foreground="white",bg='#000000')
log_label.set("")

winlog.mainloop()	

		