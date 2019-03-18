#!/usr/bin/python
# -*- coding: latin-1 -
from Tkinter import *
import subprocess
import tkMessageBox
import ttk

############################################ definition des fonctions ####################################
def write_script(filename,string,tag): # fonction qui va inscrire la régle iptables dans la table INPUT ou OUTPUT en fonction de la régle indiquée

	with open(filename,'r') as file:
		content = file.read()
		new = content.replace(tag,''.join([tag, string]))
	with open(filename,'w') as file:
		file.write(new)

def output_interface():

	interface_prefixe.set("-o ")
	actualiser_phrase()

def input_interface():

	interface_prefixe.set("-i ")
	actualiser_phrase()

def dest_def():

	destination.set("--dport ")
	actualiser_phrase()

def source_def():

	destination.set("--sport ")
	actualiser_phrase()

def reinit_tout():

	phrase.set('')
	protocol_M.set('')
	input_B.set("OUTPUT ")
	input_B.set("INPUT ")
	status_M.set("")
	autorisation.set("")
	destination.set("")
	port_L.set("")
	interface.set("")
	interface_prefixe.set("")

def actualiser_phrase():

	phrase.set("") # réinitialisation de la variable phrase
	phrase.set("iptables -A "+input_B.get()+output_B.get()+interface_prefixe.get()+interface.get()+protocol_M.get()+destination.get()+port_L.get()+status_M.get()+autorisation.get())
	
def udp_button():

	protocol_M.set(udp.get())
	actualiser_phrase()

def tcp_button():

	protocol_M.set(tcp.get())
	actualiser_phrase()

def icmp_button():

	protocol_M.set(icmp.get())
	actualiser_phrase()

def newRE_button():

	status_M.set(newRE.get())
	actualiser_phrase()

def relatedE_button():

	status_M.set(relatedE.get())
	actualiser_phrase()

def new_button():

	status_M.set(new.get())
	actualiser_phrase()

def related_button():

	status_M.set(related.get())
	actualiser_phrase()

def estabish_button():

	status_M.set(estabish.get())
	actualiser_phrase()

def accept_button():

	autorisation.set(" -j ACCEPT")
	actualiser_phrase()

def reject_button():

	autorisation.set(" -j REJECT")
	actualiser_phrase()

def drop_button():

	autorisation.set(" -j DROP")
	actualiser_phrase()

def input_button():
	
	input_B.set("INPUT ")
	actualiser_phrase()

def output_button():
	
	input_B.set("OUTPUT ")
	actualiser_phrase()

def inscription_iptable_script():

	phrase.set("iptables -A "+input_B.get()+output_B.get()+interface_prefixe.get()+interface.get()+protocol_M.get()+destination.get()+port_L.get()+status_M.get()+autorisation.get())
	
	if 'INPUT' in phrase.get():

	    write_script('scripts/iptable_init.sh', "\n"+phrase.get(), '#table_INPUT')

	if 'OUTPUT' in phrase.get():

	    write_script('scripts/iptable_init.sh', "\n"+phrase.get(), '#table_OUTPUT')

	reinit_tout()
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
autorisation = StringVar()
autorisation.set("")
#drop_B = StringVar()
#drop_B.set("")
#accept_B = StringVar()
#accept_B.set("")
#reject_B = StringVar()
#reject_B.set("")
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
destination = StringVar()
destination.set("")
interface_prefixe = StringVar()
interface_prefixe.set("")
##################################### création des boutons,label etc... ###############################
##################################### partie supérieur frame_up #######################################

mb3 = Menubutton(frame_up, text='Interface :') # Création d'un menu button qui va permettre de selectionner le protocol souhaité
mb3.grid(row=0,column=0)
mb3.menu = Menu(mb3)
mb3["menu"] = mb3.menu
mb3.menu.add_command(label='-o', command=output_interface)
mb3.menu.add_command(label='-i',command=input_interface)

labelVide = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les éléments
labelVide.grid(row=0,column=1)

entryName = Entry(frame_up,textvariable=interface)
entryName.grid(row=0,column=2)

labelVide1 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelVide1.grid(row=0,column=3)

buttonINPUT=Button(frame_up, command=input_button)
buttonINPUT.grid(row=0,column=4) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonAddImg = PhotoImage(file="pictures/INPUT.gif")
buttonINPUT.config(image=buttonAddImg)
buttonINPUT.image = buttonAddImg

labelVide2 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelVide2.grid(row=0,column=5)

buttonOUTPUT=Button(frame_up,command=output_button)
buttonOUTPUT.grid(row=0,column=6) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonAddImg1 = PhotoImage(file="pictures/OUTPUT.gif")
buttonOUTPUT.config(image=buttonAddImg1)
buttonOUTPUT.image = buttonAddImg1

labelVide2 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelVide2.grid(row=0,column=7)

mb = Menubutton(frame_up, text='protocol') # Création d'un menu button qui va permettre de selectionner le protocol souhaité
mb.grid(row=0,column=8)
mb.menu = Menu(mb)
mb["menu"] = mb.menu
mb.menu.add_command(label='udp', command=udp_button)
mb.menu.add_command(label='tcp',command=tcp_button)
mb.menu.add_command(label='icmp',command=icmp_button)

labelVide3 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelVide3.grid(row=0,column=9)

mb1 = Menubutton(frame_up, text='Port :') # Création d'un menu button qui va permettre de selectionner le protocol souhaité
mb1.grid(row=0,column=10)
mb1.menu = Menu(mb1)
mb1["menu"] = mb1.menu
mb1.menu.add_command(label='destination', command=dest_def)
mb1.menu.add_command(label='source',command=source_def)

labelVide4 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelVide4.grid(row=0,column=11)

entryPort = Entry(frame_up,textvariable=port_L)
entryPort.grid(row=0,column=12)

labelVide5 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelVide5.grid(row=0,column=13)

mb2 = Menubutton(frame_up, text='status') # Création d'un menu button qui va permettre de selectionner le status souhaité
mb2.grid(row=0,column=14)
mb2.menu = Menu(mb2)
mb2["menu"] = mb2.menu
mb2.menu.add_command(label='NEW,RELATED,ESTABLISHED', command=newRE_button)
mb2.menu.add_command(label='RELATED,ESTABLISHED', command=relatedE_button)
mb2.menu.add_command(label='NEW', command=new_button)
mb2.menu.add_command(label='RELATED', command=related_button)
mb2.menu.add_command(label='ESTABLISHED', command=estabish_button)

labelName1 = Label(frame_up, text=" ", foreground='white',bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelName1.grid(row=0,column=15)

buttonACCEPT=Button(frame_up,command=accept_button)
buttonACCEPT.grid(row=0,column=16) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonAddImg2 = PhotoImage(file="pictures/accept.gif")
buttonACCEPT.config(image=buttonAddImg2)
buttonACCEPT.image = buttonAddImg2

labelName2 = Label(frame_up, text=" ", foreground='white',bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelName2.grid(row=0,column=17)

buttonDROP=Button(frame_up,command=drop_button)
buttonDROP.grid(row=0,column=18) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonAddImg3 = PhotoImage(file="pictures/DROP.gif")
buttonDROP.config(image=buttonAddImg3)
buttonDROP.image = buttonAddImg3

labelName3 = Label(frame_up, text=" ", foreground='white',bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelName3.grid(row=0,column=19)

buttonREJECT=Button(frame_up,command=reject_button)
buttonREJECT.grid(row=0,column=20) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonAddImg4 = PhotoImage(file="pictures/reject.gif")
buttonREJECT.config(image=buttonAddImg4)
buttonREJECT.image = buttonAddImg4

labelName4 = Label(frame_up, text="              ", foreground='white',bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
labelName4.grid(row=0,column=21)

buttonEnregistrer=Button(frame_up,command=inscription_iptable_script)
buttonEnregistrer.grid(row=0,column=22) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonAddImg = PhotoImage(file="pictures/buttonAdd2.gif")
buttonEnregistrer.config(image=buttonAddImg)
buttonEnregistrer.image = buttonAddImg

buttonActualiser_phrase=Button(frame_up,command=reinit_tout)
buttonActualiser_phrase.grid(row=1,column=0) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonActualiserImg = PhotoImage(file="pictures/afficher.gif")
buttonActualiser_phrase.config(image=buttonActualiserImg)
buttonActualiser_phrase.image = buttonActualiserImg

entryPort = Entry(frame_up, bd=5, width=90,textvariable=phrase,foreground='red',font='Helvetica 14 bold')
entryPort.place(x=75,y=38)

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