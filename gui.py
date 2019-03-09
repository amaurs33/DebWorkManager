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

	print cheminLog
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
	buttonAddImg = PhotoImage(file="pictures/buttonAdd2.gif")
	buttonEnregistrer.config(image=buttonAddImg)
	buttonEnregistrer.image = buttonAddImg


	labelVide1 = Label(frame_up,text="  ",bg='#ffffff')
	labelVide1.grid(row=1,column=8)

	buttonDelete=Button(frame_up,command=route)
	buttonDelete.grid(row=1,column=9)
	deleteImg = PhotoImage(file="pictures/minus.gif")
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
	buttonAddImg = PhotoImage(file="pictures/buttonAdd2.gif")
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
	
	dc = {}
	dc['syslog'] = r'"/var/log/syslog"'
	dc['message'] = r'/var/log/message'

	selectItem = lb.get(lb.curselection())

	cheminLog=dc[selectItem]
	print cheminLog

	buttonAfficher=Button(frame_up, command=log)
	buttonAfficher.grid(row=2,column=2)
	afficherImg = PhotoImage(file="pictures/afficher.gif")
	buttonAfficher.config(image=afficherImg)
	buttonAfficher.image = afficherImg

### frame_down ###
	labelDown = Label(frame_down,textvariable=log_label)
	labelDown.place(x=0,y=0)
	labelDown.configure(foreground="white",bg='#000000')
	log_label.set("")

def win_iptable() :

	win_iptable2 = Toplevel()
	frame_down = Frame (win_iptable2,height=800,width=1000,relief=RAISED,bd=8,bg="black")
	frame_up = Frame (win_iptable2,height=800,width=1000,bd=8,bg="white")
	frame_down.grid(row=1,column=0)
	frame_up.grid(row=0,column=0)
	win_iptable2.title("Configuration des régles iptables")
	win_iptable2.configure(bg='#ffffff')
	win_iptable2.geometry("1000x850")
	win_iptable2.resizable(width=False,height=False)


	labelName = Label(frame_up, text="Nom (ex : eth0) :", foreground='white',bg='#6a8bff')
	labelName.grid(row=0,column=0)

	labelVide = Label(frame_up,text="  ",bg='#ffffff')
	labelVide.grid(row=0,column=1)

	entryName = Entry(frame_up)
	entryName.grid(row=0,column=3)

	labelVide1 = Label(frame_up,text="  ",bg='#ffffff')
	labelVide1.grid(row=0,column=4)

	buttonINPUT=Button(frame_up)
	buttonINPUT.grid(row=0,column=5)
	buttonAddImg = PhotoImage(file="pictures/INPUT.gif")
	buttonINPUT.config(image=buttonAddImg)
	buttonINPUT.image = buttonAddImg

	labelVide2 = Label(frame_up,text="  ",bg='#ffffff')
	labelVide2.grid(row=0,column=6)

	buttonOUTPUT=Button(frame_up)
	buttonOUTPUT.grid(row=0,column=7)
	buttonAddImg1 = PhotoImage(file="pictures/OUTPUT.gif")
	buttonOUTPUT.config(image=buttonAddImg1)
	buttonOUTPUT.image = buttonAddImg1

	labelVide2 = Label(frame_up,text="  ",bg='#ffffff')
	labelVide2.grid(row=0,column=8)

	mb = Menubutton(frame_up, text='protocol')
	mb.grid(row=0,column=9)
	mb.menu = Menu(mb)
	mb["menu"] = mb.menu
	mb.menu.add_command(label='udp')
	mb.menu.add_command(label='tcp')
	mb.menu.add_command(label='icmp')

	labelVide3 = Label(frame_up,text="  ",bg='#ffffff')
	labelVide3.grid(row=0,column=10)

	labelName = Label(frame_up, text="Port:", foreground='white',bg='#6a8bff')
	labelName.grid(row=0,column=11)

	labelVide4 = Label(frame_up,text="  ",bg='#ffffff')
	labelVide4.grid(row=0,column=12)

	entryPort = Entry(frame_up)
	entryPort.grid(row=0,column=13)

	labelVide5 = Label(frame_up,text="  ",bg='#ffffff')
	labelVide5.grid(row=0,column=14)

	mb = Menubutton(frame_up, text='status')
	mb.grid(row=0,column=15)
	mb.menu = Menu(mb)
	mb["menu"] = mb.menu
	mb.menu.add_command(label='NEW,RELATED,ESTABLISHED')
	mb.menu.add_command(label='RELATED,ESTABLISHED')
	mb.menu.add_command(label='NEW')
	mb.menu.add_command(label='RELATED')
	mb.menu.add_command(label='ESTABLISHED')

	labelName1 = Label(frame_up, text=" ", foreground='white',bg='#ffffff')
	labelName1.grid(row=0,column=16)

	buttonACCEPT=Button(frame_up)
	buttonACCEPT.grid(row=0,column=17)
	buttonAddImg2 = PhotoImage(file="pictures/accept.gif")
	buttonACCEPT.config(image=buttonAddImg2)
	buttonACCEPT.image = buttonAddImg2

	labelName2 = Label(frame_up, text=" ", foreground='white',bg='#ffffff')
	labelName2.grid(row=0,column=18)

	buttonDROP=Button(frame_up)
	buttonDROP.grid(row=0,column=19)
	buttonAddImg3 = PhotoImage(file="pictures/DROP.gif")
	buttonDROP.config(image=buttonAddImg3)
	buttonDROP.image = buttonAddImg3
	
	labelName3 = Label(frame_up, text=" ", foreground='white',bg='#ffffff')
	labelName3.grid(row=0,column=20)

	buttonREJECT=Button(frame_up)
	buttonREJECT.grid(row=0,column=21)
	buttonAddImg4 = PhotoImage(file="pictures/reject.gif")
	buttonREJECT.config(image=buttonAddImg4)
	buttonREJECT.image = buttonAddImg4

	labelName4 = Label(frame_up, text="         ", foreground='white',bg='#ffffff')
	labelName4.grid(row=0,column=22)
	
	buttonEnregistrer=Button(frame_up)
	buttonEnregistrer.grid(row=0,column=23)
	buttonAddImg = PhotoImage(file="pictures/buttonAdd2.gif")
	buttonEnregistrer.config(image=buttonAddImg)
	buttonEnregistrer.image = buttonAddImg

	labelDown = Label(frame_down,textvariable=route_label)
	labelDown.place(x=150,y=10)
	labelDown.configure(foreground="white",bg='#000000')
	route_label.set("")

	buttonActualiser=Button(frame_down, text="Actualiser", foreground = "black", command=route)
	buttonActualiser.place(x=890,y=0)

# main 
window = Tk()
## définition des variables ##
route_label = StringVar()
log_label = StringVar()
cheminLog = StringVar()
#cheminLog = r'/var/log/syslog'



### mise en forme de la fenêtre principale ###

window.title("Grub")
window.geometry("465x140")
window.configure(bg='#ffffff')
window.resizable(width=False,height=False)



### mise en place des "button" ###
labelVide2 = Label(window,text="  ",bg='#ffffff')
labelVide2.grid(row=0,column=0)

buttonRoute =Button(window,command =win_route)
routeImg = PhotoImage(file="pictures/road.gif")
buttonRoute.config(image=routeImg)
buttonRoute.image = routeImg
buttonRoute.grid(row=1,column=0)

labelVide = Label(window,text="  ",bg='#ffffff')
labelVide.grid(row=1,column=1)

buttonIptable =Button(window, command =win_iptable)
firewallImg = PhotoImage(file="pictures/firewall.gif")
buttonIptable.config(image=firewallImg)
buttonIptable.image = firewallImg
buttonIptable.grid(row=1,column=2)

labelVide1 = Label(window,text="  ",bg='#ffffff')
labelVide1.grid(row=1,column=3)

buttonLog =Button(window, command =win_log)
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

