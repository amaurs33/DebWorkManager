#!/usr/bin/python
# -*- coding: latin-1 -
from Tkinter import *
import subprocess
import getpass # cacher le mot de passe
import tkMessageBox
import sqlite3


############################################ definition des fonctions ####################################
def getSSHPasswd():	# Fenêtre permettant de se connecter en super-utilisateur

	def closeWindow():

		SSHpasswdWindows.destroy() # Fermeture de la fenêtre de mot de passe SSH

	def getInputPasswd():

		SSHpasswd.set(readInputSSHPasswd.get()) # On associe la valeur entrée au stringVar SSHpasswd
		closeWindow()
		getRoadToUser() # Appelle de la méthode d'affichage des logs
	
	SSHpasswdWindows = Toplevel(roadConfigurationWindow) # Composition graphique de la fenêtre

	SSHpasswdWindows.title("ssh connection authentification")
	SSHpasswdWindows.lift(aboveThis=roadConfigurationWindow)
	labelSSHPasswd = Label(SSHpasswdWindows,text="Enter SSH password please :" ,font='Helvetica 14 bold') # Ces deux lignes permettent juste d'espacer les boutons
	labelSSHPasswd.grid(row=0,column=0)
	entrySSHPasswd = Entry(SSHpasswdWindows, bd=5, width=20, show="*",textvariable=readInputSSHPasswd)
	entrySSHPasswd.grid(row=1,column=0)
	saveButton=Button(SSHpasswdWindows,command=getInputPasswd, text="Accept", fg="white", bg="#c90000",font='Helvetica 14 bold') # Le bouton enregistré appelle la fonction getInputPasswd qui associe le mot de passe saisi au stringVar SSHpasswd
	saveButton.grid(row=2,column=0)


def getRoadToUser(): # Fonction qui va déployer les fichier iptable_init.sh et route_init.sh grâce à une connection SSH

	roadSSHCommand =  "sshpass -p "+SSHpasswd.get()+" ssh root@"+IpSelected.get()+" 'route -n'" # affiche des routes selectionné sur l'utilisateur cible
	
	
	SSHConnection = subprocess.Popen([roadSSHCommand], shell = True,stdout=subprocess.PIPE) # Execution des commande dans le shell linux
	outputSSHConnection,error = SSHConnection.communicate()

	if outputSSHConnection:
		SSHpasswd.set('')
		raodLabel.set(outputSSHConnection)
	 	
	else:
		SSHpasswd.set('')
		tkMessageBox.showerror("Error","wrong password, try again")
	
def databaseCreationIpUser () : # Création de la base de donnée IP - USER

	connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
	curseur = connexion.cursor()
	curseur.execute('''CREATE TABLE IF NOT EXISTS ip_ssh (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, IP TEXT, USER TEXT)''') # création de la table logFiles
	connexion.close() # Fermeture de la connection

def getIpInDatabase() : # Récupération de l'ip suivant l'utilisateur choisi dans la base de données

	connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
	curseur = connexion.cursor()
	getUserInListbox = listboxUserToIp.get(listboxUserToIp.curselection())
	curseur.execute("SELECT IP FROM ip_ssh WHERE USER LIKE '%s'" % getUserInListbox) # Récupération de l'IP suivant l'utilisateur selectionné dans la listbox
	record = curseur.fetchone()
	IpSelected.set(record[0]) 
	connexion.close() # Fermeture de la connexion SSH
	getSSHPasswd() # Appelle de la fonction getSSHPasswd afin de pouvoir authentifier la connection SSH

def listboxIntegration () : # Fonction qui va intégrer des valeurs dans la listBox

	connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
	curseur = connexion.cursor()
	curseur.execute("SELECT USER FROM ip_ssh") # Récupération des valeurs "nom" dans la base de donnée pour l'insérer dans la listeBox
	i=0
	for row in curseur.fetchall():
		listboxUserToIp.insert(i,row[0])
		i=i+1
	connexion.close() # Fermeture de la base de donnée

def writeRoadToScript(): # Inscription de la nouvelle route dans le fichier route_init.sh

	newRoad.set("route add -net "+address.get()+" netmask "+mask.get()+" gw "+gateway.get()) # Création du string route
	file = open('scripts/route_init.sh','a') # Ouverture puis inscription dans le fichier route_init.sh
	file.write("\n"+newRoad.get())
	file.close()

	mask.set("") # Les 4 prochaines lignes réinitialisent les variables
	gateway.set("")
	address.set("")
	newRoad.set("")

	tkMessageBox.showinfo("Succes", "New road is saved in the script") # Affichage de la réussite de l'enregistrement

def roadScriptOpening(): # Lancement du script de configuration des routes pour une modification en direct

	odtPrint = subprocess.Popen(["loffice","scripts/route_init.sh"], stdout=subprocess.PIPE)
	output = odtPrint.communicate()[0]
			
####################################### MAIN #######################################

roadConfigurationWindow = Tk() # Les lignes suivantes définissent l'interface graphique de la fenêtre principale
frame_down = Frame (roadConfigurationWindow,height=200,width=850,relief=RAISED,bd=8,bg="black")
frame_up = Frame (roadConfigurationWindow,height=400,width=850,bd=8,bg="white")
frame_down.grid(row=1,column=0) 
frame_up.grid(row=0,column=0) 
roadConfigurationWindow.title("Road configuration") 
roadConfigurationWindow.configure(bg='#ffffff') 
roadConfigurationWindow.geometry("850x250") 
roadConfigurationWindow.resizable(width=False,height=False)
	
# définition des variables

raodLabel = StringVar()
address = StringVar()
gateway = StringVar()
mask = StringVar()
newRoad = StringVar()

ipAddress = StringVar() # Variable "adresse IP"
ipAddress.set('')
userName = StringVar() # Variable "nom d'utilisateur"
userName.set('')
readInputSSHPasswd = StringVar() # Variable d'entrée de mot de passe dans la textbox
SSHpasswd = StringVar() # Variable de mot de passe SSH
IpSelected = StringVar() # Variable de l'IP selectionnée dans la listbox par rapport à l'utilisateur
IpSelected.set('')

##################################### création des boutons,label etc... ###############################
##################################### partie supérieur frame_up #######################################
	
roadLabel = Label(frame_up, text="Road :", foreground='white',bg='#1d83ff')
roadLabel.grid(row=1,column=0)
addressEntry = Entry(frame_up,textvariable=address)  # va permettre de récupérer l'entrée "road" tapée par l'utilisateur
addressEntry.grid(row=1,column=1)

gatewayLabel = Label(frame_up, text="gateway :", foreground='white',bg='#1d83ff')
gatewayLabel.grid(row=1,column=2)
gatewayEntry = Entry(frame_up, textvariable=gateway) # va permettre de récupérer l'entrée "gateway" tapée par l'utilisateur
gatewayEntry.grid(row=1,column=3)

maskLabel = Label(frame_up, text="mask :", foreground='white',bg='#1d83ff')
maskLabel.grid(row=1,column=4)
maskEntry = Entry(frame_up, textvariable=mask)  # va permettre de récupérer l'entrée "mask" tapée par l'utilisateur
maskEntry.grid(row=1,column=5)

emptyLabel = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les éléments
emptyLabel.grid(row=1,column=6)

SaveButton=Button(frame_up,command=writeRoadToScript) # Bouton qui va lancer la méthode writeRoadToScript 
SaveButton.grid(row=1,column=7) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
SaveButtonImg = PhotoImage(file="pictures/buttonAdd2.gif")
SaveButton.config(image=SaveButtonImg)
SaveButton.image = SaveButtonImg


emptyLabel1 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les éléments
emptyLabel1.grid(row=1,column=10)

buttonRoadScriptOpening=Button(frame_up,command=roadScriptOpening)
buttonRoadScriptOpening.grid(row=1,column=11) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonRoadScriptImg = PhotoImage(file="pictures/fichier.gif")
buttonRoadScriptOpening.config(image=buttonRoadScriptImg)
buttonRoadScriptOpening.image = buttonRoadScriptImg


##################################### partie inférieure frame_down #######################################
	
labelDown = Label(frame_down,textvariable=raodLabel)
labelDown.place(x=150,y=10)
labelDown.configure(foreground="white",bg='#000000')

labelName = Label(frame_down, text="Select one user :", foreground='black',bg='#dad6d5')
labelName.place(x=550,y=160)

listboxUserToIp = Listbox(frame_down,height=2) # création de la listbox pour choisir vers quelle adresse IP/USER la connexion SSH doit être effectuée 
listboxUserToIp.place(x=670,y=140)

databaseCreationIpUser()
listboxIntegration ()
	
displayButton=Button(frame_down, text="Actualize", foreground = "black", command=getIpInDatabase) # lorsque l'utilisateur clique sur le boutton il exécute la fonction "route" 
displayButton.place(x=740,y=0)

roadConfigurationWindow.mainloop()


