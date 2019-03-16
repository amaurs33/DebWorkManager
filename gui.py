#!/usr/bin/python
# -*- coding: latin-1 -*-
from Tkinter import *
import os
import sys
import subprocess


############################################ definition des fonctions ####################################

## fonction qui va afficher la fenêtre de configuration des routes ##

def route():
	os.system('python scripts/route.py') # On appelle le script python route.py
	
## fonction qui va afficher la fenêtre de configuration des logs  ##

def log():
	os.system('python scripts/log.py') # On appelle le script python log.py

## fonction qui va afficher la fenêtre de configuration de iptable  ##

def iptable():
	os.system('python scripts/iptable.py') # On appelle le script python iptable.py

## fonction qui va afficher la documentation d'aide pour l'application ##

def odt():

	odtPrint = subprocess.Popen(["loffice","aide.odt"], stdout=subprocess.PIPE)
	output = odtPrint.communicate()[0]
	print(output)
	
################################################ Fenêtre principale ###################################################
	
window = Tk()

### mise en forme de la fenêtre principale ###

window.title("Grub") # définition du titre de la fenêtre
window.geometry("465x230") # définition de la taille de la fenêtre
window.configure(bg='#000000') # définition de la couleur de fond de la fenêtre
window.resizable(width=False,height=False) # rend impossible le redimensionnement de la fenêtre

#*********************************** mise en place du bouton de configuration des routes ****************************#

labelVide2 = Label(window,text="  ",bg='#000000') # Ces deux lignes permettent juste d'espacer les boutons
labelVide2.grid(row=0,column=0)

buttonRoute =Button(window,command =route) # Lorsque l'utilisateur va cliquer sur le bouton il va "lancer" la fonction route
routeImg = PhotoImage(file="pictures/road.gif") # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonRoute.config(image=routeImg)
buttonRoute.image = routeImg
buttonRoute.grid(row=1,column=0)

labelVide = Label(window,text="  ",bg='#000000') # Ces deux lignes permettent juste d'espacer les boutons
labelVide.grid(row=1,column=1)

#******************************** mise en place du bouton de configuration des régles iptable ************************#

buttonIptable =Button(window, command =iptable) # Lorsque l'utilisateur va cliquer sur le bouton il va "lancer" la fonction iptable
firewallImg = PhotoImage(file="pictures/firewall.gif") # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonIptable.config(image=firewallImg)
buttonIptable.image = firewallImg
buttonIptable.grid(row=1,column=2)

labelVide1 = Label(window,text="  ",bg='#000000') # Ces deux lignes permettent juste d'espacer les boutons
labelVide1.grid(row=1,column=3)

#*********************************** mise en place du bouton de configuration des logs ********************************#

buttonLog =Button(window, command = log) # Lorsque l'utilisateur va cliquer sur le bouton il va "lancer" la fonction log
logImg = PhotoImage(file="pictures/log.gif") # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonLog.config(image=logImg)
buttonLog.image = logImg
buttonLog.grid(row=1,column=4)

labelVide2 = Label(window,text="  ",bg='#000000') # Ces deux lignes permettent juste d'espacer les boutons
labelVide2.grid(row=1,column=5)

#******************************* mise en place du bouton d'affichage de la documentation'*******************************#

buttonAide =Button(window, command =odt) # Lorsque l'utilisateur va cliquer sur le bouton il va "lancer" la fonction odt
aideImg = PhotoImage(file="pictures/aide.gif") # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonAide.config(image=aideImg)
buttonAide.image = aideImg
buttonAide.grid(row=1,column=6)

buttonDeployer =Button(window, command =odt) # Lorsque l'utilisateur va cliquer sur le bouton il va "lancer" la fonction odt
deployerImg = PhotoImage(file="pictures/deployer.gif") # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonDeployer.config(image=deployerImg)
buttonDeployer.image = deployerImg
buttonDeployer.place(x=130,y=135)

window.mainloop()

