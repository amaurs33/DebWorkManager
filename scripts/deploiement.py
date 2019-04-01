#!/usr/bin/python
# -*- coding: latin-1 -*-
from Tkinter import *
import subprocess
import tkMessageBox
import ttk
import sqlite3
import sys
import os



############################################ definition des fonctions ####################################
def sudo():	

	def closeWindow():

		sudoWindow.quit()

	def variable():

		sudo_password.set(saisie.get())
		
		closeWindow()
		deployer()
	
	sudoWindow = Toplevel(winlog)
	sudoWindow.title("Authentification sudo")
	sudoWindow.lift(aboveThis=winlog)
	labelVide2 = Label(sudoWindow,text="veuillez saisir le mot de passe root :" ,font='Helvetica 14 bold') # Ces deux lignes permettent juste d'espacer les boutons
	labelVide2.grid(row=0,column=0)
	entryPort = Entry(sudoWindow, bd=5, width=20, show="*",textvariable=saisie)
	entryPort.grid(row=1,column=0)
	buttonEnregistrer=Button(sudoWindow,command=variable, text="Accepter", fg="white", bg="#c90000",font='Helvetica 14 bold')
	buttonEnregistrer.grid(row=2,column=0)

def chemin_script() : # exécution de la commande : route -n afin d'afficher les routes définient

	cheminIptable = subprocess.Popen(["locate","iptable_init.sh"], stdout=subprocess.PIPE)
	outputIptable = cheminIptable.communicate()[0]
	iptable_label.set(outputIptable)

	cheminRoute = subprocess.Popen(["locate","route_init.sh"], stdout=subprocess.PIPE)
	outputRoute = cheminRoute.communicate()[0]
	route_label.set(outputRoute)
	

def deployer():

	sudo()
	chemin_script()
	commande_1 =  "sshpass -p "+ sudo_password.get() +" scp -r scripts/iptable_init.sh root@"+cheminLog.get()+":/etc/init.d/ && sshpass -p "+sudo_password.get()+" scp -r scripts/route_init.sh root@"+cheminLog.get()+":/etc/init.d/ "
	commande_2 = "&& sshpass -p "+sudo_password.get()+" ssh root@"+cheminLog.get()+" 'update-rc.d iptable_init.sh defaults && update-rc.d route_init.sh defaults'"
	
	connexion_ssh = subprocess.Popen([commande_1,commande_2],shell=True, stdout=subprocess.PIPE)
	output = connexion_ssh.communicate()[0]
	sudo_password.set('')
	tkMessageBox.showinfo("Réussite", "Opération effectuée")

def recuperationCheminDB() :

	connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
	curseur = connexion.cursor()
	name = lb.get(lb.curselection())
	curseur.execute("SELECT IP FROM ip_ssh WHERE USER LIKE '%s'" % name)
	record = curseur.fetchone()
	cheminLog.set(record[0]) 
	connexion.close()
	sudo()
	
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
saisie = StringVar()
sudo_password = StringVar()
route_label = StringVar()
route_label.set('')
iptable_label = StringVar()
iptable_label.set('')
cheminLog = StringVar()
cheminLog.set('')
concatenation_final = StringVar()

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
