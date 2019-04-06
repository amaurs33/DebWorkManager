#!/usr/bin/python
# -*- coding: latin-1 -*-
from Tkinter import *
import subprocess
import tkMessageBox
import ttk
import sqlite3


############################################ definition des fonctions ####################################
def getSSHPasswd():	# Fenêtre permettant de se connecter en super-utilisateur

	def closeWindow():

		SSHpasswdWindows.destroy() # Fermeture de la fenêtre de mot de passe SSH

	def getInputPasswd():

		SSHpasswd.set(readInputSSHPasswd.get()) # On associe la valeur entrée au stringVar SSHpasswd
		closeWindow()
		getLogToUser() # Appelle de la méthode d'affichage des logs
	
	SSHpasswdWindows = Toplevel(winlog) # Composition graphique de la fenêtre

	SSHpasswdWindows.title("ssh connection authentification")
	SSHpasswdWindows.lift(aboveThis=winlog)
	labelSSHPasswd = Label(SSHpasswdWindows,text="Enter SSH password please :" ,font='Helvetica 14 bold') # Ces deux lignes permettent juste d'espacer les boutons
	labelSSHPasswd.grid(row=0,column=0)
	entrySSHPasswd = Entry(SSHpasswdWindows, bd=5, width=20, show="*",textvariable=readInputSSHPasswd)
	entrySSHPasswd.grid(row=1,column=0)
	saveButton=Button(SSHpasswdWindows,command=getInputPasswd, text="Accept", fg="white", bg="#c90000",font='Helvetica 14 bold') # Le bouton enregistré appelle la fonction getInputPasswd qui associe le mot de passe saisi au stringVar SSHpasswd
	saveButton.grid(row=2,column=0)


def getLogToUser(): # Fonction qui va déployer les fichier iptable_init.sh et route_init.sh grâce à une connection SSH

	logSSHCommand =  "sshpass -p "+SSHpasswd.get()+" ssh root@"+IpSelected.get()+" tail "+logPath.get()
	
	
	SSHConnection = subprocess.Popen([logSSHCommand],shell=True, stdout=subprocess.PIPE) # Execution des commande dans le shell linux
	outputSSHConnection,error = SSHConnection.communicate()

	if outputSSHConnection:
		SSHpasswd.set('')
		displayLogInLabel.set(outputSSHConnection)
	 	
	else:
		SSHpasswd.set('')
		tkMessageBox.showerror("Error","wrong password, try again")
	
	
########

def databaseCreationIpUser () : # Création de la base de donnée IP - USER

	connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
	curseur1 = connexion.cursor()
	curseur1.execute('''CREATE TABLE IF NOT EXISTS ip_ssh (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, IP TEXT, USER TEXT)''') # création de la table logFiles
	connexion.close() # Fermeture de la connection

def getIpInDatabase() : # Récupération de l'ip suivant l'utilisateur choisi dans la base de données

	connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
	curseur2 = connexion.cursor()
	getUserInListbox = listboxUserToIp.get(listboxUserToIp.curselection())
	curseur2.execute("SELECT IP FROM ip_ssh WHERE USER LIKE '%s'" % getUserInListbox) # Récupération de l'IP suivant l'utilisateur selectionné dans la listbox
	record = curseur2.fetchone()
	IpSelected.set(record[0]) 
	connexion.close() # Fermeture de la connexion SSH
	getSSHPasswd() # Appelle de la fonction getSSHPasswd afin de pouvoir authentifier la connection SSH

def listboxIntegrationUserIpSSH () : # Fonction qui va intégrer des valeurs dans la listBox

	connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
	curseur3= connexion.cursor()
	curseur3.execute("SELECT USER FROM ip_ssh") # Récupération des valeurs "nom" dans la base de donnée pour l'insérer dans la listeBox
	i=0
	for row in curseur3.fetchall():
		listboxUserToIp.insert(i,row[0])
		i=i+1
	connexion.close() # Fermeture de la base de donnée

def getDBPath() : # récupére le chemin du fichier de log selectionné dans la base de donnée log.db

	connexion = sqlite3.connect("dataBase/log.db") #connexion à la base de donnée
	curseur = connexion.cursor()
	name = lb.get(lb.curselection())
	curseur.execute("SELECT chemin FROM logFiles WHERE nom LIKE '%s'" % name)
	record = curseur.fetchone()
	logPath.set(record[0]) 
	connexion.close()
	getIpInDatabase()
	

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

frame_down = Frame (winlog,height=800,width=1000,relief=RAISED,bd=8,bg="black")
frame_up = Frame (winlog,height=100,width=1000,bd=8,bg="white")
frame_down.grid(row=1,column=0)
frame_up.grid(row=0,column=0)
winlog.title("Configurer des logs")
winlog.configure(bg='#ffffff')
winlog.geometry("1000x500")
winlog.resizable(width=False,height=False)

### Définition des variables
displayLogInLabel = StringVar()
newLogPath = StringVar()
newLogPath.set('')
logPathName = StringVar()
logPathName.set('')
logPath = StringVar()
logPath.set('')

ipAddress = StringVar() # Variable "adresse IP"
ipAddress.set('')
userName = StringVar() # Variable "nom d'utilisateur"
userName.set('')
readInputSSHPasswd = StringVar() # Variable d'entrée de mot de passe dans la textbox
SSHpasswd = StringVar() # Variable de mot de passe SSH
IpSelected = StringVar() # Variable de l'IP selectionnée dans la listbox par rapport à l'utilisateur
IpSelected.set('')

### création de la listbox pour choisir le log à afficher ###

lb = Listbox(frame_up, height =2,exportselection=False)
lb.grid(row=2,column=1)

### Dés le lancement de la fenêtre la base de donnée et la listBox se mettent à jour

databaseCreation ()
listboxIntegration ()


### ajout des label et des textbox

labelLog = Label(frame_up, text="Add the path to the log file to save :", foreground='white',bg='#1d83ff')
labelLog.grid(row=1,column=0)
entryLog = Entry(frame_up,textvariable=newLogPath)
entryLog.grid(row=1,column=1)

labelName = Label(frame_up, text="Give it a name", foreground='white',bg='#1d83ff')
labelName.grid(row=1,column=2)
entryName = Entry(frame_up,textvariable=logPathName)
entryName.grid(row=1,column=3)

saveButton=Button(frame_up,command=databaseAdd)
saveButton.grid(row=1,column=4)
saveButtonImg = PhotoImage(file="pictures/buttonAdd2.gif")
saveButton.config(image=saveButtonImg)
saveButton.image = saveButtonImg

labelName = Label(frame_up, text="Choose the log file to show :", foreground='white',bg='#6a8bff')
labelName.grid(row=2,column=0)

labelName = Label(frame_up, text="Select one user :", foreground='white',bg='#6a8bff')
labelName.grid(row=2,column=2)

listboxUserToIp = Listbox(frame_up,height=2,exportselection=False) # création de la listbox pour choisir vers quelle adresse IP/USER la connexion SSH doit être effectuée 
listboxUserToIp.grid(row=2,column=3)

databaseCreationIpUser()
listboxIntegrationUserIpSSH()

displayButton=Button(frame_up, command=getDBPath)
displayButton.grid(row=2,column=4)
displayButtonImg = PhotoImage(file="pictures/afficher.gif")
displayButton.config(image=displayButtonImg)
displayButton.image = displayButtonImg

##################################### partie inférieure frame_up #######################################

labelDown = Label(frame_down,textvariable=displayLogInLabel)
labelDown.place(x=0,y=0)
labelDown.configure(foreground="white",bg='#000000')
displayLogInLabel.set("")

winlog.mainloop()	

		