#!/usr/bin/python
# -*- coding: latin-1 -
from Tkinter import *
import subprocess
import getpass # cacher le mot de passe


def variable():

	sudo_password.set(saisie.get())
	root_login()
def sudo():	

	sudo = Toplevel(newwin)
	sudo.lift(aboveThis=newwin)

	entryPort = Entry(sudo, bd=5, width=20, show="*",textvariable=saisie)
	entryPort.grid(row=0,column=0)
	buttonEnregistrer=Button(sudo,command=variable)
	buttonEnregistrer.grid(row=1,column=0)

	

############################################ definition des fonctions ####################################
	
def route() : # exécution de la commande : route -n afin d'afficher les routes définient

	routePrint = subprocess.Popen(["sudo","route","-n"], stdout=subprocess.PIPE)
	output = routePrint.communicate()[0]
	route_label.set(output)
	
def root_login():
	
	command = 'sudo apt-get update'
	command = command.split()

	cmd1 = subprocess.Popen(['echo',sudo_password.get()], stdout=subprocess.PIPE)
	cmd2 = subprocess.Popen(['sudo','-S'] + command, stdin=cmd1.stdout, stdout=subprocess.PIPE)
	output = cmd2.stdout.read().decode() 
	

####################################### Fenêtre secondaire route #######################################

newwin = Tk()
sudo_password = StringVar()
saisie = StringVar()
### mise en forme de la fenêtre principale ###

frame_down = Frame (newwin,height=200,width=800,relief=RAISED,bd=8,bg="black") # frame_down et frame_up vont permettre de scinder la fenêtre en deux parties
frame_up = Frame (newwin,height=400,width=800,bd=8,bg="white")
frame_down.grid(row=1,column=0) # Placement des fenêtres
frame_up.grid(row=0,column=0) # Placement des fenêtres
newwin.title("Configurer des routes") # définition du titre de la fenêtre
newwin.configure(bg='#ffffff') # définition de la couleur de fond de la fenêtre
newwin.geometry("800x250") # définition de la taille de la fenêtre
newwin.resizable(width=False,height=False) # rend impossible le redimensionnement de la fenêtre
	
# définition des variables

route_label = StringVar()


##################################### création des boutons,label etc... ###############################
##################################### partie supérieur frame_up #######################################
	
labelRoute = Label(frame_up, text="Route :", foreground='white',bg='#1d83ff')
labelRoute.grid(row=1,column=0)
entryRoute = Entry(frame_up)  # va permettre de récupérer l'entrée "route" tapée par l'utilisateur
entryRoute.grid(row=1,column=1)

labelPasserelle = Label(frame_up, text="Passerelle :", foreground='white',bg='#1d83ff')
labelPasserelle.grid(row=1,column=2)
entryPasserelle = Entry(frame_up) # va permettre de récupérer l'entrée "passerelle" tapée par l'utilisateur
entryPasserelle.grid(row=1,column=3)

labelMasque = Label(frame_up, text="Masque :", foreground='white',bg='#1d83ff')
labelMasque.grid(row=1,column=4)
entryMasque = Entry(frame_up)  # va permettre de récupérer l'entrée "masque" tapée par l'utilisateur
entryMasque.grid(row=1,column=5)

labelVide = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les éléments
labelVide.grid(row=1,column=6)

buttonEnregistrer=Button(frame_up,command=sudo)
buttonEnregistrer.grid(row=1,column=7) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonAddImg = PhotoImage(file="pictures/buttonAdd2.gif")
buttonEnregistrer.config(image=buttonAddImg)
buttonEnregistrer.image = buttonAddImg

labelVide1 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les éléments
labelVide1.grid(row=1,column=8)

buttonDelete=Button(frame_up,command=route)
buttonDelete.grid(row=1,column=9) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
deleteImg = PhotoImage(file="pictures/minus.gif")
buttonDelete.config(image=deleteImg)
buttonDelete.image = deleteImg

##################################### partie inférieure frame_down #######################################
	
labelDown = Label(frame_down,textvariable=route_label)
labelDown.place(x=150,y=10)
labelDown.configure(foreground="white",bg='#000000')
	
buttonActualiser=Button(frame_down, text="Actualiser", foreground = "black", command=route) # lorsque l'utilisateur clique sur le boutton il exécute la fonction "route" 
buttonActualiser.place(x=690,y=0)
newwin.mainloop()


