#!/usr/bin/python
# -*- coding: latin-1 -*-
from Tkinter import *
import subprocess
import tkMessageBox
import ttk
import sqlite3
import os

############################################ definition des fonctions #############################################

def getSSHPasswd():	# Fenêtre permettant de se connecter en super-utilisateur

	def closeWindow():

		SSHpasswdWindows.destroy() # Fermeture de la fenêtre de mot de passe SSH

	def getInputPasswd():

		SSHpasswd.set(readInputSSHPasswd.get()) # On associe la valeur entrée au stringVar SSHpasswd
		closeWindow() 
		deployment() # Appelle de la méthode de deploiement
	
	SSHpasswdWindows = Toplevel(windowDeployment) # Composition graphique de la fenêtre

	SSHpasswdWindows.title("ssh connection authentification")
	SSHpasswdWindows.lift(aboveThis=windowDeployment)
	labelSSHPasswd = Label(SSHpasswdWindows,text="Enter SSH password please :" ,font='Helvetica 14 bold') # Ces deux lignes permettent juste d'espacer les boutons
	labelSSHPasswd.grid(row=0,column=0)
	entrySSHPasswd = Entry(SSHpasswdWindows, bd=5, width=20, show="*",textvariable=readInputSSHPasswd)
	entrySSHPasswd.grid(row=1,column=0)
	saveButton=Button(SSHpasswdWindows,command=getInputPasswd, text="Accept", fg="white", bg="#c90000",font='Helvetica 14 bold') # Le bouton enregistré appelle la fonction getInputPasswd qui associe le mot de passe saisi au stringVar SSHpasswd
	saveButton.grid(row=2,column=0)


def deployment(): # Fonction qui va déployer les fichier iptable_init.sh et route_init.sh grâce à une connection SSH

	copySSHcommand =  "sshpass -p "+ SSHpasswd.get() +" scp -r scripts/iptable_init.sh root@"+IpSelected.get()+":/etc/init.d/ && sshpass -p "+SSHpasswd.get()+" scp -r scripts/route_init.sh root@"+IpSelected.get()+":/etc/init.d/ " # copie des scripts vers l'ordinateur cible par SSH
	updateRcSSHCommand = "&& sshpass -p "+SSHpasswd.get()+" ssh root@"+IpSelected.get()+" 'update-rc.d iptable_init.sh defaults && update-rc.d route_init.sh defaults'" # Mise à jours,par SSH, du rc.d afin que les scripts s'éxecutent au démarrage.
	
	SSHConnection = subprocess.Popen([copySSHcommand,updateRcSSHCommand],shell=True, stdout=subprocess.PIPE) # Execution des commande dans le shell linux
	outputSSHConnection,error = SSHConnection.communicate()

	if outputSSHConnection: # gestion de l'exception de mauvais mot de passe ou d'une machine non connectée
		SSHpasswd.set('')
		tkMessageBox.showinfo("Success", "Completed deployment") # Message d'information sur la réussite du déploiement
	 	
	else:
		SSHpasswd.set('')
		tkMessageBox.showerror("Error","wrong password or host isn't connected, try again")
	

def getIpInDatabase() : # Récupération de l'ip suivant l'utilisateur choisi dans la base de données

	connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
	curseur = connexion.cursor()
	getUserInListbox = listboxUserToIp.get(listboxUserToIp.curselection())
	curseur.execute("SELECT IP FROM ip_ssh WHERE USER LIKE '%s'" % getUserInListbox) # Récupération de l'IP suivant l'utilisateur selectionné dans la listbox
	record = curseur.fetchone()
	IpSelected.set(record[0]) 
	connexion.close() # Fermeture de la connexion SSH
	getSSHPasswd() # Appelle de la fonction getSSHPasswd afin de pouvoir authentifier la connection SSH

def databaseCreationIpUser () : # Création de la base de donnée IP - USER

	connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
	curseur = connexion.cursor()
	curseur.execute('''CREATE TABLE IF NOT EXISTS ip_ssh (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, IP TEXT, USER TEXT)''') # création de la table logFiles
	connexion.close() # Fermeture de la connection

def databaseAdd (): # Ajout de données dans la base de donnée IP - USER
	
	if ipAddress.get() != "" and userName.get() != "" : # Gestion de l'exception si l'un des widget entry n'est pas rempli

		connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
		curseur = connexion.cursor()
		entriesIpUser = (ipAddress.get(),userName.get()) # Récupération des valeurs entrées dans les textBox : IP et USER
		curseur.execute('''INSERT INTO ip_ssh (IP, USER ) VALUES (?,?)''',entriesIpUser) # Insertion dans la base de donnée
		connexion.commit() # Fermeture de la connection
		tkMessageBox.showinfo("Success", "add to database")
		connexion.close() # Fermeture de la connection
		ipAddress.set("") # Réinitialisation de l'adresse IP
		userName.set("") # Réinitialisation du nom de l'utilisateur
		listboxIntegration() # Fonction qui va intégrer les nouvelles valeurs dans la listbox
		
	else :
		tkMessageBox.showerror("Error","All entry wdigets are not filed")


def listboxIntegration () : # Fonction qui va intégrer des valeurs dans la listBox

	connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
	curseur = connexion.cursor()
	curseur.execute("SELECT USER FROM ip_ssh") # Récupération des valeurs "nom" dans la base de donnée pour l'insérer dans la listeBox
	i=0
	for row in curseur.fetchall():
		listboxUserToIp.insert(i,row[0])
		i=i+1
	connexion.close() # Fermeture de la base de donnée


################################### MAIN #########################################
		
windowDeployment = Tk() # Les lignes suivantes définissent l'interface graphique de la fenêtre principale
frame_down = Frame (windowDeployment,height=650,width=1000,relief=RAISED,bd=8,bg="white") 
frame_up = Frame (windowDeployment,height=900,width=1000,bd=8,bg="white")
frame_down.grid(row=1,column=0) # Placement des fenêtres
frame_up.grid(row=0,column=0) # Placement des fenêtres
windowDeployment.title("road configuration")
windowDeployment.configure(bg='#ffffff')
windowDeployment.geometry("800x130")
windowDeployment.resizable(width=False,height=False)

### Définition des variables

ipAddress = StringVar() # Variable "adresse IP"
ipAddress.set('')
userName = StringVar() # Variable "nom d'utilisateur"
userName.set('')
readInputSSHPasswd = StringVar() # Variable d'entrée de mot de passe dans la textbox
SSHpasswd = StringVar() # Variable de mot de passe SSH
IpSelected = StringVar() # Variable de l'IP selectionnée dans la listbox par rapport à l'utilisateur
IpSelected.set('')

### Mise en place des éléments dans la fenêtre windows deployment

labelIpAdd = Label(frame_up, text="Add the new IP address :", foreground='white',bg='#1d83ff') 
labelIpAdd.grid(row=1,column=0)
entryIp = Entry(frame_up,textvariable=ipAddress) # Textbox d'entrée d'adresse IP dans le srtingVar ipAdress
entryIp.grid(row=1,column=1)

emptyLabel = Label(frame_up,text="  ",bg='#ffffff') # Label vide pour l'espacement
emptyLabel.grid(row=1,column=2)

labelName = Label(frame_up, text="Give it a username :", foreground='white',bg='#1d83ff') 
labelName.grid(row=1,column=3)
entryName = Entry(frame_up,textvariable=userName) #Textbox d'entrée du nom d'utilisateur dans le srtingVar userName
entryName.grid(row=1,column=4)

emptyLabel1 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les éléments
emptyLabel1.grid(row=1,column=5)

saveButton=Button(frame_up,command=databaseAdd) # Bouton d'enregistrement qui va renvoyer vers la méthode databaseAdd
saveButton.grid(row=1,column=6) # Les lignes suivantes mettent en place l'interface graphique du bouton
buttonAddImg = PhotoImage(file="pictures/buttonAdd2.gif")
saveButton.config(image=buttonAddImg)
saveButton.image = buttonAddImg

labelName = Label(frame_down, text="Select one user :", foreground='white',bg='#6a8bff')
labelName.grid(row=2,column=2)

listboxUserToIp = Listbox(frame_down, height =2) # création de la listbox pour choisir vers quelle adresse IP/USER la connexion SSH doit être effectuée 
listboxUserToIp.grid(row=2,column=3)

buttonDeployment=Button(frame_down, command=getIpInDatabase) # Bouton de deploiement final en passant par la méthode getIpInDatabase
buttonDeployment.grid(row=2,column=4)
afficherImg = PhotoImage(file="pictures/deploiement.gif")
buttonDeployment.config(image=afficherImg)
buttonDeployment.image = afficherImg

### Excecution des méthodes de création de la base de donnée et de mise en place de la listbox suivant la base de donnée

databaseCreationIpUser ()
listboxIntegration ()

windowDeployment.mainloop()
