#!/usr/bin/python
# -*- coding: latin-1 -*-
from Tkinter import *
import os
import sys
import subprocess


### definition des fonctions ###
### affichage commande ( route -n )

def route():
	os.system('python route.py')
	
def log():
	os.system('python log.py')

def iptable():
	os.system('python iptable.py')

def odt():

	odtPrint = subprocess.Popen(["loffice","aide.odt"], stdout=subprocess.PIPE)
	output = odtPrint.communicate()[0]
	print(output)
	

#def getLog() :
	
## définition des actions nouvelle fenêtre
## definition de la fenetre de configuration des routes ##



	

# main 
window = Tk()
## définition des variables ##
log_label = StringVar()
cheminLog = StringVar()



### mise en forme de la fenêtre principale ###

window.title("Grub")
window.geometry("465x140")
window.configure(bg='#ffffff')
window.resizable(width=False,height=False)



### mise en place des "button" ###
labelVide2 = Label(window,text="  ",bg='#ffffff')
labelVide2.grid(row=0,column=0)

buttonRoute =Button(window,command =route)
routeImg = PhotoImage(file="pictures/road.gif")
buttonRoute.config(image=routeImg)
buttonRoute.image = routeImg
buttonRoute.grid(row=1,column=0)

labelVide = Label(window,text="  ",bg='#ffffff')
labelVide.grid(row=1,column=1)

buttonIptable =Button(window, command =iptable)
firewallImg = PhotoImage(file="pictures/firewall.gif")
buttonIptable.config(image=firewallImg)
buttonIptable.image = firewallImg
buttonIptable.grid(row=1,column=2)

labelVide1 = Label(window,text="  ",bg='#ffffff')
labelVide1.grid(row=1,column=3)

buttonLog =Button(window, command = log)
logImg = PhotoImage(file="pictures/log.gif")
buttonLog.config(image=logImg)
buttonLog.image = logImg
buttonLog.grid(row=1,column=4)

labelVide2 = Label(window,text="  ",bg='#ffffff')
labelVide2.grid(row=1,column=5)

buttonAide =Button(window, command =odt)
aideImg = PhotoImage(file="pictures/aide.gif")
buttonAide.config(image=aideImg)
buttonAide.image = aideImg
buttonAide.grid(row=1,column=6)


window.mainloop()

