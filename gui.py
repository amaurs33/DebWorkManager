#!/usr/bin/python
# -*- coding: latin-1 -*-
from Tkinter import *
import subprocess


### definition des fonctions ###
### affichage commande ( route -n )
def route() :

	routePrint = subprocess.Popen(["route","-n"], stdout=subprocess.PIPE)
	output = routePrint.communicate()[0]
	print(output)
	route_label.set(output)
## définition des actions nouvelle fenêtre
## definition de la fenetre de configuration des routes ##
def win_route() :
	

	newwin = Toplevel()
	frame_down = Frame (newwin,height=200,width=800,relief=RAISED,bd=8,bg="black")
	frame_up = Frame (newwin,height=400,width=800,relief=SUNKEN,bd=8,bg="white")
	frame_down.grid(row=1,column=0)
	frame_up.grid(row=0,column=0)
	newwin.title("Configurer des routes")
	newwin.configure(bg='#ffffff')
	newwin.geometry("800x600")

	labelDown = Label(frame_down,textvariable=route_label)
	labelDown.place(x=0,y=0)
	labelDown.configure(foreground="white",bg='#000000')
	route_label.set("")

	buttonTest =Button(frame_down, text="Actualiser", foreground = "black", command=route)
	buttonTest.place(x=690,y=0)


# main 
window = Tk()
## définition des variables ##
route_label = StringVar()
### mise en forme de la fenêtre principale ###

window.title("titre de test")
window.geometry("400x170")
window.configure(bg='#ffffff')

### mise en place des "button" ###

buttonRoute =Button(window, text="Configurer des routes", foreground = "white", command =win_route)
buttonRoute.configure(bg='#850fef')
buttonRoute.place(x=115,y=30)

buttonIptable =Button(window, text="Configurer iptable", foreground = "white", command =win_route)
buttonIptable.configure(bg='#850fef')
buttonIptable.place(x=125,y=70)

buttonLog =Button(window, text="Afficher les logs", foreground = "white", command =win_route)
buttonLog.configure(bg='#850fef')
buttonLog.place(x=130,y=110)


window.mainloop()

