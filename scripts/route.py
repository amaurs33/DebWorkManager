#!/usr/bin/python
# -*- coding: latin-1 -
from Tkinter import *
import subprocess
import getpass # cacher le mot de passe
import tkMessageBox



############################################ definition des fonctions ####################################
	


def writeRoadToScript(): # Inscription de la nouvelle route dans le fichier route_init.sh

	newRoad.set("route add -net "+address.get()+" netmask "+mask.get()+" gw "+gateway.get()) # Création du string route
	file = open('scripts/route_init.sh','a') # Ouverture puis inscription dans le fichier route_init.sh
	file.write("\n"+newRoad.get())
	file.close()

	mask.set("") # Les 4 prochaines lignes réinitialisent les variables
	gateway.set("")
	address.set("")
	newRoad.set("")

	tkMessageBox.showinfo("Réussite", "Opération effectuée") # Affichage de la réussite de l'enregistrement

def route() : # exécution de la commande : route -n afin d'afficher les routes définient

	raodDisplayCommandLine = subprocess.Popen(["route","-n"], stdout=subprocess.PIPE) # Exécution de la commande route -n
	output = raodDisplayCommandLine.communicate()[0]
	raodLabel.set(output)
	
def roadScriptOpening(): # Lancement du script de configuration des routes pour une modification en direct

	odtPrint = subprocess.Popen(["loffice","scripts/route_init.sh"], stdout=subprocess.PIPE)
	output = odtPrint.communicate()[0]
			
####################################### MAIN #######################################

roadConfigurationWindow = Tk() # Les lignes suivantes définissent l'interface graphique de la fenêtre principale
frame_down = Frame (roadConfigurationWindow,height=200,width=850,relief=RAISED,bd=8,bg="black")
frame_up = Frame (roadConfigurationWindow,height=400,width=850,bd=8,bg="white")
frame_down.grid(row=1,column=0) 
frame_up.grid(row=0,column=0) 
roadConfigurationWindow.title("Configurer des routes") 
roadConfigurationWindow.configure(bg='#ffffff') 
roadConfigurationWindow.geometry("850x250") 
roadConfigurationWindow.resizable(width=False,height=False)
	
# définition des variables

raodLabel = StringVar()
address = StringVar()
gateway = StringVar()
mask = StringVar()
newRoad = StringVar()


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
	
buttonActualiser=Button(frame_down, text="Actualiser", foreground = "black", command=route) # lorsque l'utilisateur clique sur le boutton il exécute la fonction "route" 
buttonActualiser.place(x=740,y=0)

roadConfigurationWindow.mainloop()


