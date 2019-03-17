#!/usr/bin/python
# -*- coding: latin-1 -
from Tkinter import *
import subprocess
import tkMessageBox
import ttk

############################################ definition des fonctions ####################################
def actualiser_phrase():
	phrase.set("") # réinitiali
	phrase.set("iptables -A "+input_B.get()+output_B.get()+interface.get()+protocol_M.get()+port_L.get()+status_M.get()+drop_B.get()+reject_B.get()+accept_B.get())
	
def udp_button():
	protocol_M.set(udp.get())
def tcp_button():
	protocol_M.set(tcp.get())
def icmp_button():
	protocol_M.set(icmp.get())
def newRE_button():
	status_M.set(newRE.get())
def relatedE_button():
	status_M.set(relatedE.get())
def new_button():
	status_M.set(new.get())
def related_button():
	status_M.set(related.get())
def estabish_button():
	status_M.set(estabish.get())
def accept_button():

	accept_B.set(" -j ACCEPT")

def reject_button():

	reject_B.set(" -j REJECT")

def drop_button():

	drop_B.set(" -j DROP")

def input_button():
	
	input_B.set(" INPUT ")

def output_button():
	
	input_B.set(" OUTPUT ")

def inscription_iptable_script():

	phrase.set("iptables -A "+input_B.get()+output_B.get()+interface.get()+protocol_M.get()+port_L.get()+status_M.get()+drop_B.get()+reject_B.get()+accept_B.get())
	file = open('scripts/iptable_init.sh','a')
	file.write("\n"+phrase.get())
	file.close()	
	input_B.set("") # Les 4 prochaines lignes réinitialisent les variables
	output_B.set("")
	interface.set("")
	protocol_M.get()
	port_L.set("")
	status_M.set("")
	drop_B.set("")
	reject_B.set("")
	accept_B.set("")
	phrase.set("")
	tkMessageBox.showinfo("Réussite", "Opération effectuée")

def ouvertureScript():

	odtPrint = subprocess.Popen(["loffice","scripts/iptable_init.sh"], stdout=subprocess.PIPE)
	output = odtPrint.communicate()[0]
	print(output)		

def sudo():	

	def closeWindow():

		sudoWindow.destroy()

	def variable():

		sudo_password.set(saisie.get())
		affichageReglesIptable()
		closeWindow()
	
	sudoWindow = Toplevel(win_iptable)
	sudoWindow.title("Authentification sudo")
	sudoWindow.lift(aboveThis=win_iptable)
	labelVide2 = Label(sudoWindow,text="veuillez saisir le mot de passe root :" ,font='Helvetica 14 bold') # Ces deux lignes permettent juste d'espacer les boutons
	labelVide2.grid(row=0,column=0)
	entryPort = Entry(sudoWindow, bd=5, width=20, show="*",textvariable=saisie)
	entryPort.grid(row=1,column=0)
	buttonEnregistrer=Button(sudoWindow,command=variable, text="Accepter", fg="white", bg="#c90000",font='Helvetica 14 bold')
	buttonEnregistrer.grid(row=2,column=0)

def affichageReglesIptable():
	
	
	command = "sudo iptables -L -n"
	command = command.split()
	
	cmd1 = subprocess.Popen(['echo',sudo_password.get()], stdout=subprocess.PIPE)
	cmd2 = subprocess.Popen(['sudo','-S'] + command, stdin=cmd1.stdout, stdout=subprocess.PIPE)
	output,error = cmd2.communicate()
	#output,error = cmd2.communicate() # Le paragraphe (if else) permet d'afficher des messagesBox en cas de bon ou mauvais mot de passe

	if output:
		sudo_password.set("")
		iptableResult.set(output)
	 	
	else:
		sudo_password.set("")
		tkMessageBox.showerror("Erreur","Mot de passe incorrect")
		
####################################### Fenêtre secondaire iptable #######################################

win_iptable = Tk()

### mise en forme de la fenêtre principale ###

frame_down = Frame (win_iptable,height=650,width=1000,relief=RAISED,bd=8,bg="black") # frame_down et frame_up vont permettre de scinder la fenêtre en deux parties
frame_up = Frame (win_iptable,height=900,width=1000,bd=8,bg="white")
frame_down.grid(row=1,column=0) # Placement des fenêtres
frame_up.grid(row=0,column=0) # Placement des fenêtres
win_iptable.title("Configuration des régles iptables") # définition du titre de la fenêtre
win_iptable.configure(bg='#ffffff') # définition de la couleur de fond de la fenêtre
win_iptable.geometry("1000x700") # définition de la taille de la fenêtre
win_iptable.resizable(width=False,height=False) # rend impossible le redimensionnement de la fenêtre

# définition des variables
iptableResult = StringVar()
affichage_label = StringVar()
sudo_password = StringVar()
saisie = StringVar()

#Variables de configuration
interface = StringVar()
interface.set("")
input_B = StringVar()
input_B.set("")
output_B = StringVar()
output_B.set("")
protocol_M = StringVar()
protocol_M.set("")
port_L = StringVar()
port_L.set("")
status_M = StringVar()
status_M.set("")
drop_B = StringVar()
drop_B.set("")
accept_B = StringVar()
accept_B.set("")
reject_B = StringVar()
reject_B.set("")
phrase = StringVar()
udp = StringVar()
udp.set(" -p udp ")
tcp = StringVar()
tcp.set(" -p tcp ")
icmp = StringVar()
icmp.set(" -p icmp ")
newRE = StringVar()
newRE.set(" -m state --state NEW,ESTABLISHED,RELATED")
relatedE = StringVar()
relatedE.set(" -m state --state RELATED,ESTABLISHED")
new = StringVar()
new.set(" -m state --state NEW")
related = StringVar()
related.set(" -m state --state RELATED")
estabish = StringVar()
estabish.set(" -m state --state ESTABLISHED")

##################################### création des boutons,label etc... ###############################
##################################### partie supérieur frame_up #######################################

labelName = Label(frame_up, text="Nom (ex :-i/-o eth0) :", foreground='white',bg='#6a8bff') 
labelName.grid(row=0,column=0)

labelVide = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les éléments
labelVide.grid(row=0,column=1)

entryName = Entry(frame_up,textvariable=interface)
entryName.grid(row=0,column=3)

labelVide1 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelVide1.grid(row=0,column=4)

buttonINPUT=Button(frame_up, command=input_button)
buttonINPUT.grid(row=0,column=5) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonAddImg = PhotoImage(file="pictures/INPUT.gif")
buttonINPUT.config(image=buttonAddImg)
buttonINPUT.image = buttonAddImg

labelVide2 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelVide2.grid(row=0,column=6)

buttonOUTPUT=Button(frame_up,command=output_button)
buttonOUTPUT.grid(row=0,column=7) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonAddImg1 = PhotoImage(file="pictures/OUTPUT.gif")
buttonOUTPUT.config(image=buttonAddImg1)
buttonOUTPUT.image = buttonAddImg1

labelVide2 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelVide2.grid(row=0,column=8)

mb = Menubutton(frame_up, text='protocol') # Création d'un menu button qui va permettre de selectionner le protocol souhaité
mb.grid(row=0,column=9)
mb.menu = Menu(mb)
mb["menu"] = mb.menu
mb.menu.add_command(label='udp', command=udp_button)
mb.menu.add_command(label='tcp',command=tcp_button)
mb.menu.add_command(label='icmp',command=icmp_button)

labelVide3 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelVide3.grid(row=0,column=10)

labelName = Label(frame_up, text="Port:", foreground='white',bg='#6a8bff')
labelName.grid(row=0,column=11)

labelVide4 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelVide4.grid(row=0,column=12)

entryPort = Entry(frame_up,textvariable=port_L)
entryPort.grid(row=0,column=13)

labelVide5 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelVide5.grid(row=0,column=14)

mb = Menubutton(frame_up, text='status') # Création d'un menu button qui va permettre de selectionner le status souhaité
mb.grid(row=0,column=9)
mb.grid(row=0,column=15)
mb.menu = Menu(mb)
mb["menu"] = mb.menu
mb.menu.add_command(label='NEW,RELATED,ESTABLISHED', command=newRE_button)
mb.menu.add_command(label='RELATED,ESTABLISHED', command=relatedE_button)
mb.menu.add_command(label='NEW', command=new_button)
mb.menu.add_command(label='RELATED', command=related_button)
mb.menu.add_command(label='ESTABLISHED', command=estabish_button)

labelName1 = Label(frame_up, text=" ", foreground='white',bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelName1.grid(row=0,column=16)

buttonACCEPT=Button(frame_up,command=accept_button)
buttonACCEPT.grid(row=0,column=17) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonAddImg2 = PhotoImage(file="pictures/accept.gif")
buttonACCEPT.config(image=buttonAddImg2)
buttonACCEPT.image = buttonAddImg2

labelName2 = Label(frame_up, text=" ", foreground='white',bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelName2.grid(row=0,column=18)

buttonDROP=Button(frame_up,command=drop_button)
buttonDROP.grid(row=0,column=19) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonAddImg3 = PhotoImage(file="pictures/DROP.gif")
buttonDROP.config(image=buttonAddImg3)
buttonDROP.image = buttonAddImg3

labelName3 = Label(frame_up, text=" ", foreground='white',bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelName3.grid(row=0,column=20)

buttonREJECT=Button(frame_up,command=reject_button)
buttonREJECT.grid(row=0,column=21) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonAddImg4 = PhotoImage(file="pictures/reject.gif")
buttonREJECT.config(image=buttonAddImg4)
buttonREJECT.image = buttonAddImg4

labelName4 = Label(frame_up, text="         ", foreground='white',bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelName4.grid(row=0,column=22)


buttonEnregistrer=Button(frame_up,command=inscription_iptable_script)
buttonEnregistrer.grid(row=0,column=23) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonAddImg = PhotoImage(file="pictures/buttonAdd2.gif")
buttonEnregistrer.config(image=buttonAddImg)
buttonEnregistrer.image = buttonAddImg



buttonActualiser_phrase=Button(frame_up,command=actualiser_phrase)
buttonActualiser_phrase.grid(row=1,column=0) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonActualiserImg = PhotoImage(file="pictures/afficher.gif")
buttonActualiser_phrase.config(image=buttonActualiserImg)
buttonActualiser_phrase.image = buttonActualiserImg

entryPort = Entry(frame_up, bd=5, width=90,textvariable=phrase,foreground='red',font='Helvetica 14 bold')
entryPort.place(x=130,y=38)

##################################### partie inférieure frame_down #######################################

labelDown = Label(frame_down,textvariable= iptableResult)
labelDown.place(x=150,y=10)
labelDown.configure(foreground="white",bg='#000000')
iptableResult.set("")

buttonFichier=Button(frame_down,command=ouvertureScript)
buttonFichier.place(x=0,y=0) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
fichierImg = PhotoImage(file="pictures/fichier.gif")
buttonFichier.config(image=fichierImg)
buttonFichier.image = fichierImg

buttonActualiser=Button(frame_down, text="Actualiser", foreground = "black", command=sudo)#, command=route)
buttonActualiser.place(x=890,y=0)


win_iptable.mainloop()