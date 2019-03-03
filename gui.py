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

def log() :
	logPrint = subprocess.Popen(["tail",cheminLog], stdout=subprocess.PIPE)
	output = logPrint.communicate()[0]
	print(output)
	log_label.set(output)

def odt():

	odtPrint = subprocess.Popen(["loffice","aide.odt"], stdout=subprocess.PIPE)
	output = odtPrint.communicate()[0]
	print(output)
	

#def getLog() :
	
## définition des actions nouvelle fenêtre
## definition de la fenetre de configuration des routes ##
def win_route() :
	

	newwin = Toplevel()
	frame_down = Frame (newwin,height=200,width=800,relief=RAISED,bd=8,bg="black")
	frame_up = Frame (newwin,height=400,width=800,bd=8,bg="white")
	frame_down.grid(row=1,column=0)
	frame_up.grid(row=0,column=0)
	newwin.title("Configurer des routes")
	newwin.configure(bg='#ffffff')
	newwin.geometry("800x250")
	newwin.resizable(width=False,height=False)
	
	### frame up ###
	labelRoute = Label(frame_up, text="Route :", foreground='white',bg='#1d83ff')
	labelRoute.grid(row=1,column=0)
	entryRoute = Entry(frame_up)
	entryRoute.grid(row=1,column=1)

	labelPasserelle = Label(frame_up, text="Passerelle :", foreground='white',bg='#1d83ff')
	labelPasserelle.grid(row=1,column=2)
	entryPasserelle = Entry(frame_up)
	entryPasserelle.grid(row=1,column=3)

	labelMasque = Label(frame_up, text="Masque :", foreground='white',bg='#1d83ff')
	labelMasque.grid(row=1,column=4)
	entryMasque = Entry(frame_up)
	entryMasque.grid(row=1,column=5)

	labelVide = Label(frame_up,text="  ",bg='#ffffff')
	labelVide.grid(row=1,column=6)

	buttonEnregistrer=Button(frame_up,command=route)
	buttonEnregistrer.grid(row=1,column=7)
	buttonAddImg = PhotoImage(file="buttonAdd2.gif")
	buttonEnregistrer.config(image=buttonAddImg)
	buttonEnregistrer.image = buttonAddImg


	labelVide1 = Label(frame_up,text="  ",bg='#ffffff')
	labelVide1.grid(row=1,column=8)

	buttonDelete=Button(frame_up,command=route)
	buttonDelete.grid(row=1,column=9)
	deleteImg = PhotoImage(file="minus.gif")
	buttonDelete.config(image=deleteImg)
	buttonDelete.image = deleteImg

	### frame down ###

	labelDown = Label(frame_down,textvariable=route_label)
	labelDown.place(x=150,y=10)
	labelDown.configure(foreground="white",bg='#000000')
	route_label.set("")

	buttonActualiser=Button(frame_down, text="Actualiser", foreground = "black", command=route)
	buttonActualiser.place(x=690,y=0)

def win_log() :

	winlog = Toplevel()
	frame_down = Frame (winlog,height=800,width=1000,relief=RAISED,bd=8,bg="black")
	frame_up = Frame (winlog,height=100,width=1000,bd=8,bg="white")
	frame_down.grid(row=1,column=0)
	frame_up.grid(row=0,column=0)
	winlog.title("Configurer des routes")
	winlog.configure(bg='#ffffff')
	winlog.geometry("1000x500")
	winlog.resizable(width=False,height=False)

### ajout du label et du textbox

	labelLog = Label(frame_up, text="Ajouter un fichier de log :", foreground='white',bg='#1d83ff')
	labelLog.grid(row=1,column=0)
	entryLog = Entry(frame_up)
	entryLog.grid(row=1,column=1)

	labelVide = Label(frame_up,text="  ",bg='#ffffff')
	labelVide.grid(row=1,column=2)

	labelName = Label(frame_up, text="Donnez-lui un nom", foreground='white',bg='#1d83ff')
	labelName.grid(row=1,column=3)
	entryName = Entry(frame_up)
	entryName.grid(row=1,column=4)

	labelVide = Label(frame_up,text="  ",bg='#ffffff')
	labelVide.grid(row=1,column=5)

	buttonEnregistrer=Button(frame_up)
	buttonEnregistrer.grid(row=1,column=6)
	buttonAddImg = PhotoImage(file="buttonAdd2.gif")
	buttonEnregistrer.config(image=buttonAddImg)
	buttonEnregistrer.image = buttonAddImg

	labelName = Label(frame_up, text="Sélectionnez un Log:", foreground='white',bg='#6a8bff')
	labelName.grid(row=2,column=0)

	### création de la listbox pour choisir le log à afficher ###
	lb = Listbox(frame_up, height =2)
	lb.insert(0, "syslog")
	lb.insert(1,"message")
	lb.select_set(0)
	lb.grid(row=2,column=1)
	
	selected_item = StringVar()

	

	buttonAfficher=Button(frame_up, command=log)
	buttonAfficher.grid(row=2,column=2)
	afficherImg = PhotoImage(file="afficher.gif")
	buttonAfficher.config(image=afficherImg)
	buttonAfficher.image = afficherImg

### frame_down ###
	labelDown = Label(frame_down,textvariable=log_label)
	labelDown.place(x=0,y=0)
	labelDown.configure(foreground="white",bg='#000000')
	log_label.set("")
	winlog.mainloop()

def win_iptable() :
	

	win_iptable = Toplevel()
	win_iptable.title("Configurer iptable")
	win_iptable.configure(bg='#000000')
	win_iptable.geometry("360x150")
	win_iptable.resizable(width=False,height=False)

	labelPres = Label(win_iptable, text="Bienvenue dans l'assistant de configuration \n des régles iptables, en cliquant sur suivant \n vous acceptez de créer un script qui automatisera vos \n régles iptables", foreground='white',bg='#000000')
	labelPres.place(x=0,y=0)

	buttonSuivant=Button(win_iptable,text="suivant",command=log)
	buttonSuivant.place(x=85,y=100)

	buttonSuivant=Button(win_iptable,text="annuler",command=log)
	buttonSuivant.place(x=175,y=100)





# main 
window = Tk()
## définition des variables ##
route_label = StringVar()
log_label = StringVar()

#cheminLog = r'/var/log/syslog'



### mise en forme de la fenêtre principale ###

window.title("Grub")
window.geometry("465x140")
window.configure(bg='#ffffff')
window.resizable(width=False,height=False)

cheminLog=r'/var/log/syslog'

### mise en place des "button" ###
labelVide2 = Label(window,text="  ",bg='#ffffff')
labelVide2.grid(row=0,column=0)

buttonRoute =Button(window,command =win_route)
routeImg = PhotoImage(file="road.gif")
buttonRoute.config(image=routeImg)
buttonRoute.image = routeImg
buttonRoute.grid(row=1,column=0)

labelVide = Label(window,text="  ",bg='#ffffff')
labelVide.grid(row=1,column=1)

buttonIptable =Button(window, command =win_iptable)
firewallImg = PhotoImage(file="firewall.gif")
buttonIptable.config(image=firewallImg)
buttonIptable.image = firewallImg
buttonIptable.grid(row=1,column=2)

labelVide1 = Label(window,text="  ",bg='#ffffff')
labelVide1.grid(row=1,column=3)

buttonLog =Button(window, command =win_log)
logImg = PhotoImage(file="log.gif")
buttonLog.config(image=logImg)
buttonLog.image = logImg
buttonLog.grid(row=1,column=4)

labelVide2 = Label(window,text="  ",bg='#ffffff')
labelVide2.grid(row=1,column=5)

buttonAide =Button(window, command =odt)
aideImg = PhotoImage(file="aide.gif")
buttonAide.config(image=aideImg)
buttonAide.image = aideImg
buttonAide.grid(row=1,column=6)


window.mainloop()

