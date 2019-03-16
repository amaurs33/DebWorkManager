#!/usr/bin/python
# -*- coding: latin-1 -
from Tkinter import *
import subprocess
import getpass # cacher le mot de passe
import tkMessageBox



############################################ definition des fonctions ####################################
	


def inscription_route_script():

	phrase.set("route add -net "+addresse.get()+" netmask "+masque.get()+" gw "+passerelle.get())
	file = open('scripts/route_init.sh','a')
	file.write("\n"+phrase.get())
	file.close()	
	masque.set("") # Les 4 prochaines lignes réinitialisent les variables
	passerelle.set("")
	addresse.set("")
	phrase.set("")
	tkMessageBox.showinfo("Réussite", "Opération effectuée")

def route() : # exécution de la commande : route -n afin d'afficher les routes définient

	routePrint = subprocess.Popen(["route","-n"], stdout=subprocess.PIPE)
	output = routePrint.communicate()[0]
	route_label.set(output)
	
def ouvertureScript():

	odtPrint = subprocess.Popen(["loffice","scripts/route_init.sh"], stdout=subprocess.PIPE)
	output = odtPrint.communicate()[0]
	print(output)		

####################################### Fenêtre secondaire route #######################################

newwin = Tk()


### mise en forme de la fenêtre principale ###

frame_down = Frame (newwin,height=200,width=850,relief=RAISED,bd=8,bg="black") # frame_down et frame_up vont permettre de scinder la fenêtre en deux parties
frame_up = Frame (newwin,height=400,width=850,bd=8,bg="white")
frame_down.grid(row=1,column=0) # Placement des fenêtres
frame_up.grid(row=0,column=0) # Placement des fenêtres
newwin.title("Configurer des routes") # définition du titre de la fenêtre
newwin.configure(bg='#ffffff') # définition de la couleur de fond de la fenêtre
newwin.geometry("850x250") # définition de la taille de la fenêtre
newwin.resizable(width=False,height=False) # rend impossible le redimensionnement de la fenêtre
	
# définition des variables

route_label = StringVar()
addresse = StringVar()
passerelle = StringVar()
masque = StringVar()
phrase = StringVar()


##################################### création des boutons,label etc... ###############################
##################################### partie supérieur frame_up #######################################
	
labelRoute = Label(frame_up, text="Route :", foreground='white',bg='#1d83ff')
labelRoute.grid(row=1,column=0)
entryRoute = Entry(frame_up,textvariable=addresse)  # va permettre de récupérer l'entrée "route" tapée par l'utilisateur
entryRoute.grid(row=1,column=1)

labelPasserelle = Label(frame_up, text="Passerelle :", foreground='white',bg='#1d83ff')
labelPasserelle.grid(row=1,column=2)
entryPasserelle = Entry(frame_up, textvariable=passerelle) # va permettre de récupérer l'entrée "passerelle" tapée par l'utilisateur
entryPasserelle.grid(row=1,column=3)

labelMasque = Label(frame_up, text="Masque :", foreground='white',bg='#1d83ff')
labelMasque.grid(row=1,column=4)
entryMasque = Entry(frame_up, textvariable=masque)  # va permettre de récupérer l'entrée "masque" tapée par l'utilisateur
entryMasque.grid(row=1,column=5)

labelVide = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les éléments
labelVide.grid(row=1,column=6)

buttonEnregistrer=Button(frame_up,command=inscription_route_script)
buttonEnregistrer.grid(row=1,column=7) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonAddImg = PhotoImage(file="pictures/buttonAdd2.gif")
buttonEnregistrer.config(image=buttonAddImg)
buttonEnregistrer.image = buttonAddImg


labelVide2 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les éléments
labelVide2.grid(row=1,column=10)

buttonFichier=Button(frame_up,command=ouvertureScript)
buttonFichier.grid(row=1,column=11) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
fichierImg = PhotoImage(file="pictures/fichier.gif")
buttonFichier.config(image=fichierImg)
buttonFichier.image = fichierImg


##################################### partie inférieure frame_down #######################################
	
labelDown = Label(frame_down,textvariable=route_label)
labelDown.place(x=150,y=10)
labelDown.configure(foreground="white",bg='#000000')
	
buttonActualiser=Button(frame_down, text="Actualiser", foreground = "black", command=route) # lorsque l'utilisateur clique sur le boutton il exécute la fonction "route" 
buttonActualiser.place(x=740,y=0)

newwin.mainloop()


