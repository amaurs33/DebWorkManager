#!/usr/bin/pythconcatenation_finalon
# -*- coding: latin-1 -*-
from Tkinter import *
import os
import sys
import subprocess


############################################ definition des fonctions ####################################


def deploymentScriptLoad(): # fonction qui va afficher la fenêtre de déploiement en lançant le script deploiement.py

	os.system('python scripts/deploiement.py') 

def roadScriptLoad(): # fonction qui va afficher la fenêtre de configuration des routes en lançant le script route.py

	os.system('python scripts/route.py') 
	
def logScriptLoad(): # fonction qui va afficher la fenêtre de configuration des logs en lançant le script log.py

	os.system('python scripts/log.py') 

def iptableScriptLoad(): # fonction qui va afficher la fenêtre de configuration de iptable en lançant le script iptable.py

	os.system('python scripts/iptable.py') 

## fonction qui va afficher la documentation d'aide pour l'application ##

def helpLoad():

	lofficeCommandLine = subprocess.Popen(["loffice","aide.odt"], stdout=subprocess.PIPE)
	output = lofficeCommandLine.communicate()[0]

################################################ MAIN ###################################################
	
window = Tk() # Les lignes suivantes définissent l'interface graphique de la fenêtre principale
window.title("Grub") 
window.geometry("465x220") 
window.configure(bg='#000000') 
window.resizable(width=False,height=False) 

#*********************************** mise en place du bouton de configuration des routes ****************************#

emptyLabel = Label(window,text="  ",bg='#000000') # Ces deux lignes permettent juste d'espacer les boutons
emptyLabel.grid(row=0,column=0)

roadButton =Button(window,command =roadScriptLoad) # Lorsque l'utilisateur va cliquer sur le bouton il va "lancer" la fonction roadScriptLoad
routeImg = PhotoImage(file="pictures/road.gif") # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
roadButton.config(image=routeImg)
roadButton.image = routeImg
roadButton.grid(row=1,column=0)

emptyLabel1 = Label(window,text="  ",bg='#000000') # Ces deux lignes permettent juste d'espacer les boutons
emptyLabel1.grid(row=1,column=1)

#******************************** mise en place du bouton de configuration des régles iptable ************************#

iptableButton =Button(window, command =iptableScriptLoad) # Lorsque l'utilisateur va cliquer sur le bouton il va "lancer" la fonction iptableScriptLoad
iptableButtonImg = PhotoImage(file="pictures/firewall.gif") # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
iptableButton.config(image=iptableButtonImg)
iptableButton.image = iptableButtonImg
iptableButton.grid(row=1,column=2)

emptyLabel2 = Label(window,text="  ",bg='#000000') # Ces deux lignes permettent juste d'espacer les boutons
emptyLabel2.grid(row=1,column=3)

#*********************************** mise en place du bouton de configuration des logs ********************************#

buttonLog =Button(window, command =logScriptLoad) # Lorsque l'utilisateur va cliquer sur le bouton il va "lancer" la fonction logScriptLoad
logImg = PhotoImage(file="pictures/log.gif") # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonLog.config(image=logImg)
buttonLog.image = logImg
buttonLog.grid(row=1,column=4)

emptyLabel3 = Label(window,text="  ",bg='#000000') # Ces deux lignes permettent juste d'espacer les boutons
emptyLabel3.grid(row=1,column=5)

#******************************* mise en place du bouton d'affichage de la documentation'*******************************#

buttonAide =Button(window, command =helpLoad) # Lorsque l'utilisateur va cliquer sur le bouton il va "lancer" la fonction helpLoad
aideImg = PhotoImage(file="pictures/aide.gif") # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonAide.config(image=aideImg)
buttonAide.image = aideImg
buttonAide.grid(row=1,column=6)

buttonDeployer =Button(window, command =deploymentScriptLoad) # Lorsque l'utilisateur va cliquer sur le bouton il va "lancer" la fonction odt
deployerImg = PhotoImage(file="pictures/deployer.gif") # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonDeployer.config(image=deployerImg)
buttonDeployer.image = deployerImg
buttonDeployer.place(x=135,y=135)

window.mainloop()

