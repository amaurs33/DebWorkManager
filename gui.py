#!/usr/bin/python
# -*- coding: latin-1 -*-
from Tkinter import *

## définition des actions nouvelle fenêtre

def win_route() :
	newwin = Toplevel(window)
	display = Label(newwin, text="définiton nouvelle route")
	display.pack()

# main 
window = Tk()

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

