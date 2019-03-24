#!/usr/bin/python
# -*- coding: latin-1 -*-
from Tkinter import *
import subprocess
import tkMessageBox
import ttk
import sqlite3


############################################ definition des fonctions ####################################
def deployer():
	commande_1 = "scp -r scripts/iptable_init.sh root@"+cheminLog.get()+":etc/init.d/ "
	commande_2 = "&& scp -r scripts/route_init.sh root@"+cheminLog.get()+":etc/init.d/ "
	commande_3 = "ssh root@machine_distante 'update-rc.d /etc/init.d/iptable_init.sh defaults && update-rc.d /etc/init.d/route_init.sh defaults'"

	connexion_ssh = subprocess.Popen([commande_1,commande_2,commande_3], stdout=subprocess.PIPE)
	output = connexion_ssh.communicate()[0]

def recuperationCheminDB() :

	connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
	curseur = connexion.cursor()
	name = lb.get(lb.curselection())
	curseur.execute("SELECT IP FROM ip_ssh WHERE USER LIKE '%s'" % name)
	record = curseur.fetchone()
	cheminLog.set(record[0]) 
	connexion.close()
	deployer()

def creationBD () :
	connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
	curseur = connexion.cursor()
	curseur.execute('''CREATE TABLE IF NOT EXISTS ip_ssh (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, IP TEXT, USER TEXT)''') # création de la table logFiles
	connexion.close()

def ajoutDB ():
	## gestion de la base de donnée ip_ssh.db

	connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
	curseur = connexion.cursor()
	donnees = (adress_ip.get(),nom_user.get())
	curseur.execute('''INSERT INTO ip_ssh (IP, USER ) VALUES (?,?)''',donnees)
	connexion.commit()
	tkMessageBox.showinfo("Réussite", "Opération effectuée")
	connexion.close()
	adress_ip.set("")
	nom_user.set("")
	integrationListbox()


def integrationListbox () :
	connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
	curseur = connexion.cursor()
	curseur.execute("SELECT USER FROM ip_ssh") # Récupération des valeurs "nom" dans la base de donnée pour l'insérer dans la listeBox
	i=0
	for row in curseur.fetchall():
		lb.insert(i,row[0])
		i=i+1
	connexion.close()

####################################### Fenêtre secondaire log #######################################

		
winlog = Tk()
frame_down = Frame (winlog,height=650,width=1000,relief=RAISED,bd=8,bg="white") # frame_down et frame_up vont permettre de scinder la fenêtre en deux parties
frame_up = Frame (winlog,height=900,width=1000,bd=8,bg="white")
frame_down.grid(row=1,column=0) # Placement des fenêtres
frame_up.grid(row=0,column=0) # Placement des fenêtres
winlog.title("Configurer des routes")
winlog.configure(bg='#ffffff')
winlog.geometry("800x130")
winlog.resizable(width=False,height=False)

### Définition des variables
adress_ip = StringVar()
adress_ip.set('')
log_label = StringVar()
nom_user = StringVar()
nom_user.set('')

cheminLog = StringVar()
cheminLog.set('')

### création de la listbox pour choisir le log à afficher ###

lb = Listbox(frame_down, height =2)
lb.grid(row=2,column=3)

### gestion de la base de donnée
creationBD ()
integrationListbox ()

#recuperationCheminDB()

### ajout du label et du textbox

labelLog = Label(frame_up, text="Ajouter une adresse IP :", foreground='white',bg='#1d83ff')
labelLog.grid(row=1,column=0)
entryLog = Entry(frame_up,textvariable=adress_ip)
entryLog.grid(row=1,column=1)
labelVide = Label(frame_up,text="  ",bg='#ffffff')
labelVide.grid(row=1,column=2)

labelName = Label(frame_up, text="Associez-lui un nom d'utilisateur :", foreground='white',bg='#1d83ff')
labelName.grid(row=1,column=3)
entryName = Entry(frame_up,textvariable=nom_user)
entryName.grid(row=1,column=4)

labelVide = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les éléments
labelVide.grid(row=1,column=5)

buttonEnregistrer=Button(frame_up,command=ajoutDB)
buttonEnregistrer.grid(row=1,column=6)
buttonAddImg = PhotoImage(file="pictures/buttonAdd2.gif")
buttonEnregistrer.config(image=buttonAddImg)
buttonEnregistrer.image = buttonAddImg

labelName = Label(frame_down, text="Sélectionnez un utilisateur:", foreground='white',bg='#6a8bff')
labelName.grid(row=2,column=2)



buttonAfficher=Button(frame_down, command=recuperationCheminDB)
buttonAfficher.grid(row=2,column=4)
afficherImg = PhotoImage(file="pictures/deploiement.gif")
buttonAfficher.config(image=afficherImg)
buttonAfficher.image = afficherImg



winlog.mainloop()
