#!/usr/bin/python
# -*- coding: latin-1 -
from Tkinter import *
import subprocess
import tkMessageBox
import ttk
import sqlite3

############################################ definition des fonctions ####################################
def getSSHPasswd(): # Fenêtre permettant de se connecter en super-utilisateur
    
    def closeWindow():

        SSHpasswdWindows.destroy() # Fermeture de la fenêtre de mot de passe SSH

    def getInputPasswd():

        SSHpasswd.set(readInputSSHPasswd.get()) # On associe la valeur entrée au stringVar SSHpasswd
        closeWindow()
        getIptableRuleToUser() # Appelle de la méthode d'affichage des logs
    
    SSHpasswdWindows = Toplevel(iptable_window) # Composition graphique de la fenêtre

    SSHpasswdWindows.title("ssh connection authentification")
    SSHpasswdWindows.lift(aboveThis=iptable_window)
    labelSSHPasswd = Label(SSHpasswdWindows,text="Enter SSH password please :" ,font='Helvetica 14 bold') # Ces deux lignes permettent juste d'espacer les boutons
    labelSSHPasswd.grid(row=0,column=0)
    entrySSHPasswd = Entry(SSHpasswdWindows, bd=5, width=20, show="*",textvariable=readInputSSHPasswd)
    entrySSHPasswd.grid(row=1,column=0)
    saveButton=Button(SSHpasswdWindows,command=getInputPasswd, text="Accept", fg="white", bg="#c90000",font='Helvetica 14 bold') # Le bouton enregistré appelle la fonction getInputPasswd qui associe le mot de passe saisi au stringVar SSHpasswd
    saveButton.grid(row=2,column=0)


def getIptableRuleToUser(): # Fonction qui va déployer les fichier iptable_init.sh et route_init.sh grâce à une connection SSH

    iptableSSHCommand =  "sshpass -p "+SSHpasswd.get()+" ssh root@"+IpSelected.get()+" 'sudo iptables -L -n'" # commande qui affiche les régles iptables distantes
    
    
    SSHConnection = subprocess.Popen([iptableSSHCommand],shell=True, stdout=subprocess.PIPE) # Execution des commande dans le shell linux
    outputSSHConnection,error = SSHConnection.communicate()

    if outputSSHConnection: # gestion de l'exception de mauvais mot de passe ou d'une machine non connectée
        SSHpasswd.set('')
        iptableResult.set(outputSSHConnection)
        
    else:
        SSHpasswd.set('')
        tkMessageBox.showerror("Error","wrong password or host isn't connected, try again")


def databaseCreationIpUser () : # Création de la base de donnée IP - USER

    connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
    curseur = connexion.cursor()
    curseur.execute('''CREATE TABLE IF NOT EXISTS ip_ssh (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, IP TEXT, USER TEXT)''') # création de la table logFiles
    connexion.close() # Fermeture de la connection

def getIpInDatabase() : # Récupération de l'ip suivant l'utilisateur choisi dans la base de données

    connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
    curseur = connexion.cursor()
    getUserInListbox = listboxUserToIp.get(listboxUserToIp.curselection())
    curseur.execute("SELECT IP FROM ip_ssh WHERE USER LIKE '%s'" % getUserInListbox) # Récupération de l'IP suivant l'utilisateur selectionné dans la listbox
    record = curseur.fetchone()
    IpSelected.set(record[0]) 
    connexion.close() # Fermeture de la connexion SSH
    getSSHPasswd() # Appelle de la fonction getSSHPasswd afin de pouvoir authentifier la connection SSH

def listboxIntegration () : # Fonction qui va intégrer des valeurs dans la listBox

    connexion = sqlite3.connect("dataBase/ip_ssh.db") #connexion à la base de donnée
    curseur = connexion.cursor()
    curseur.execute("SELECT USER FROM ip_ssh") # Récupération des valeurs "nom" dans la base de donnée pour l'insérer dans la listeBox
    i=0
    for row in curseur.fetchall():
        listboxUserToIp.insert(i,row[0])
        i=i+1
    connexion.close() # Fermeture de la base de donnée

def writeIntoOutputOrInput(filename,string,tag): # fonction qui va inscrire la régle iptables dans la table INPUT ou OUTPUT en fonction de la régle indiquée

    with open(filename,'r') as file:
        content = file.read()
        new = content.replace(tag,''.join([tag, string]))
    with open(filename,'w') as file:
        file.write(new)

def outputInterface(): # Le préfix de l'interface sera -o

    interfacePrefix.set("-o ")
    ruleActualize()

def inputInterface(): # Le préfix de l'interface sera -i

    interfacePrefix.set("-i ")
    ruleActualize()

def portDestination(): # Le port sera positionné en destination --dport

    destination.set("--dport ")
    ruleActualize()

def sourceDestination(): # Le port sera positionné en source --sport

    destination.set("--sport ")
    ruleActualize()

def resetAll(): # Réinitialise toute les valeurs des différentes composantes de la régle iptable

    rule.set('')
    protocol_M.set('')
    trafficDirection.set("")
    state.set("")
    autorisation.set("")
    destination.set("")
    port_L.set("")
    interface.set("")
    interfacePrefix.set("")

def ruleActualize(): # Actualise la régle iptable en cour de création

    rule.set("") 
    rule.set("iptables -A "+trafficDirection.get()+output_B.get()+interfacePrefix.get()+interface.get()+protocol_M.get()+destination.get()+port_L.get()+state.get()+autorisation.get())
    
def udp_button(): # Positionne la valeur du protocol sur UDP

    protocol_M.set(udp.get())
    ruleActualize()

def tcp_button(): # Positionne la valeur du protocol sur TCP

    protocol_M.set(tcp.get())
    ruleActualize()

def icmp_button(): # Positionne la valeur du protocol sur ICMP

    protocol_M.set(icmp.get())
    ruleActualize()

def newRelatedEstablished_button(): # Positionne le status sur new,related,established

    state.set(newRelatedEstablished.get())
    ruleActualize()

def RelatedEstablished_button(): # Positionne le status sur related,established

    state.set(relatedE.get())
    ruleActualize()

def new_button(): # Positionne le status sur new

    state.set(new.get())
    ruleActualize()

def related_button():# Positionne le status sur related

    state.set(related.get())
    ruleActualize()

def establish_button(): # Positionne le status sur established

    state.set(estabish.get())
    ruleActualize()

def accept_button(): # La régle iptable sera en -j ACCEPT

    autorisation.set(" -j ACCEPT")
    ruleActualize()

def reject_button(): # La régle iptable sera en -j REJECT

    autorisation.set(" -j REJECT")
    ruleActualize()

def drop_button(): # La régle iptable sera en -j DROP

    autorisation.set(" -j DROP")
    ruleActualize()

def trafficDirection_Button(): # La régle iptable concernera le traffic en entrée
    
    trafficDirection.set("INPUT ")
    ruleActualize()

def output_button(): # La régle iptable concernera le traffic en sortie
    
    trafficDirection.set("OUTPUT ")
    ruleActualize()

def writeIntoScript(): # Inscrit la régle iptable dans le script iptable_init.sh et appelle la fonction "writIntoOutputOrInput" de façon à la positionner au bon endroit
    
    ruleConcatenation = trafficDirection.get()+output_B.get()+interfacePrefix.get()+interface.get()+protocol_M.get()+destination.get()+port_L.get()+state.get()+autorisation.get()
    
    if ruleConcatenation != "": # Gestion de l'exception si rien n'a été renseigné dans la chaine iptable
        rule.set("iptables -A "+ ruleConcatenation)

        if 'INPUT' in rule.get():

                writeIntoOutputOrInput('scripts/iptable_init.sh', "\n"+rule.get(), '#table_INPUT')
                tkMessageBox.showinfo("Succes", "The rule is saved in the script")
                resetAll()
                rule.set("")

        elif 'OUTPUT' in rule.get():

                writeIntoOutputOrInput('scripts/iptable_init.sh', "\n"+rule.get(), '#table_OUTPUT')
                tkMessageBox.showinfo("Succes", "The rule is saved in the script")
                resetAll()
                rule.set("")


        else: # Gestion de l'exception si l'option INPUT ou OUTPUT est manquante
            tkMessageBox.showerror("Error","Enter INPUT or OUTPUT") 
    else :
        tkMessageBox.showerror("Error","Rule is empty")
    
    

def scriptLoad(): # Ouvre le script iptabl_init.sh de façon à pouvoir faire des modification directement

    odtPrint = subprocess.Popen(["loffice","scripts/iptable_init.sh"], stdout=subprocess.PIPE)
    output = odtPrint.communicate()[0]
    print(output)       


####################################### MAIN #######################################

### mise en forme de la fenêtre principale ###
iptable_window = Tk() # Le paragraphe suivant va déterminé les régles de configurationd e la fenêtre principale
frame_down = Frame (iptable_window,height=650,width=1000,relief=RAISED,bd=8,bg="black") # frame_down et frame_up vont permettre de scinder la fenêtre en deux parties
frame_up = Frame (iptable_window,height=900,width=1000,bd=8,bg="white")
frame_down.grid(row=1,column=0) # Placement des fenêtres
frame_up.grid(row=0,column=0) # Placement des fenêtres
iptable_window.title("Iptable rules configuration") # définition du titre de la fenêtre
iptable_window.configure(bg='#ffffff') # définition de la couleur de fond de la fenêtre
iptable_window.geometry("1000x700") # définition de la taille de la fenêtre
iptable_window.resizable(width=False,height=False) # rend impossible le redimensionnement de la fenêtre

# définition des variables
iptableResult = StringVar()
sudo_password = StringVar()
saisie = StringVar()
interface = StringVar()
interface.set("")
trafficDirection = StringVar()
trafficDirection.set("")
output_B = StringVar()
output_B.set("")
protocol_M = StringVar()
protocol_M.set("")
port_L = StringVar()
port_L.set("")
state = StringVar()
state.set("")
autorisation = StringVar()
autorisation.set("")
rule = StringVar()
udp = StringVar()
udp.set(" -p udp ")
tcp = StringVar()
tcp.set(" -p tcp ")
icmp = StringVar()
icmp.set(" -p icmp ")
newRelatedEstablished = StringVar()
newRelatedEstablished.set(" -m state --state NEW,ESTABLISHED,RELATED")
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
interfacePrefix = StringVar()
interfacePrefix.set("")

ipAddress = StringVar() # Variable "adresse IP"
ipAddress.set('')
userName = StringVar() # Variable "nom d'utilisateur"
userName.set('')
readInputSSHPasswd = StringVar() # Variable d'entrée de mot de passe dans la textbox
SSHpasswd = StringVar() # Variable de mot de passe SSH
IpSelected = StringVar() # Variable de l'IP selectionnée dans la listbox par rapport à l'utilisateur
IpSelected.set('')
##################################### création des boutons,label etc... ###############################
##################################### partie supérieur frame_up #######################################

menuinputButtonOrOutput = Menubutton(frame_up, text='Interface :') # Création d'un menu button qui va permettre de selectionner le protocol souhaité
menuinputButtonOrOutput.grid(row=0,column=0)
menuinputButtonOrOutput.menu = Menu(menuinputButtonOrOutput)
menuinputButtonOrOutput["menu"] = menuinputButtonOrOutput.menu
menuinputButtonOrOutput.menu.add_command(label='-o', command=outputInterface)
menuinputButtonOrOutput.menu.add_command(label='-i',command=inputInterface)

emptyLabel = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les éléments
emptyLabel.grid(row=0,column=1)

entryInterface = Entry(frame_up,textvariable=interface)
entryInterface.grid(row=0,column=2)

emptyLabel1 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
emptyLabel1.grid(row=0,column=3)

inputButton=Button(frame_up, command=trafficDirection_Button)
inputButton.grid(row=0,column=4) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
inputButtonImg = PhotoImage(file="pictures/INPUT.gif")
inputButton.config(image=inputButtonImg)
inputButton.image = inputButtonImg

emptyLabel2 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
emptyLabel2.grid(row=0,column=5)

outputbutton=Button(frame_up,command=output_button)
outputbutton.grid(row=0,column=6) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
outputButtonImg = PhotoImage(file="pictures/OUTPUT.gif")
outputbutton.config(image=outputButtonImg)
outputbutton.image = outputButtonImg

emptyLabel2 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
emptyLabel2.grid(row=0,column=7)

menuButtonProtocol = Menubutton(frame_up, text='protocol') # Création d'un menu button qui va permettre de selectionner le protocol souhaité
menuButtonProtocol.grid(row=0,column=8)
menuButtonProtocol.menu = Menu(menuButtonProtocol)
menuButtonProtocol["menu"] = menuButtonProtocol.menu
menuButtonProtocol.menu.add_command(label='udp', command=udp_button)
menuButtonProtocol.menu.add_command(label='tcp',command=tcp_button)
menuButtonProtocol.menu.add_command(label='icmp',command=icmp_button)

emptyLabel3 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
emptyLabel3.grid(row=0,column=9)

menuButtonPort = Menubutton(frame_up, text='Port :') # Création d'un menu button qui va permettre de selectionner le protocol souhaité
menuButtonPort.grid(row=0,column=10)
menuButtonPort.menu = Menu(menuButtonPort)
menuButtonPort["menu"] = menuButtonPort.menu
menuButtonPort.menu.add_command(label='destination', command=portDestination)
menuButtonPort.menu.add_command(label='source',command=sourceDestination)

emptyLabel4 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
emptyLabel4.grid(row=0,column=11)

entryPort = Entry(frame_up,textvariable=port_L)
entryPort.grid(row=0,column=12)

emptyLabel5 = Label(frame_up,text="  ",bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
emptyLabel5.grid(row=0,column=13)

menuButtonstate = Menubutton(frame_up, text='state') # Création d'un menu button qui va permettre de selectionner le status souhaité
menuButtonstate.grid(row=0,column=14)
menuButtonstate.menu = Menu(menuButtonstate)
menuButtonstate["menu"] = menuButtonstate.menu
menuButtonstate.menu.add_command(label='NEW,RELATED,ESTABLISHED', command=newRelatedEstablished_button)
menuButtonstate.menu.add_command(label='RELATED,ESTABLISHED', command=RelatedEstablished_button)
menuButtonstate.menu.add_command(label='NEW', command=new_button)
menuButtonstate.menu.add_command(label='RELATED', command=related_button)
menuButtonstate.menu.add_command(label='ESTABLISHED', command=establish_button)

emptyLabel6 = Label(frame_up, text=" ", foreground='white',bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
emptyLabel6.grid(row=0,column=15)

acceptButton=Button(frame_up,command=accept_button)
acceptButton.grid(row=0,column=16) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
acceptButtonImg = PhotoImage(file="pictures/accept.gif")
acceptButton.config(image=acceptButtonImg)
acceptButton.image = acceptButtonImg

emptyLabel7 = Label(frame_up, text=" ", foreground='white',bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
emptyLabel7.grid(row=0,column=17)

dropbutton=Button(frame_up,command=drop_button)
dropbutton.grid(row=0,column=18) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
dropbuttonImg = PhotoImage(file="pictures/DROP.gif")
dropbutton.config(image=dropbuttonImg)
dropbutton.image = dropbuttonImg

emptyLabel8 = Label(frame_up, text=" ", foreground='white',bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
emptyLabel8.grid(row=0,column=19)

rejectButton=Button(frame_up,command=reject_button)
rejectButton.grid(row=0,column=20) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
rejectButtonImg = PhotoImage(file="pictures/reject.gif")
rejectButton.config(image=rejectButtonImg)
rejectButton.image = rejectButtonImg

emptyLabel9 = Label(frame_up, text="              ", foreground='white',bg='#ffffff') # Ces deux lignes permettent juste d'espacer les élements
emptyLabel9.grid(row=0,column=21)

saveButton=Button(frame_up,command=writeIntoScript)
saveButton.grid(row=0,column=22) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
inputButtonImg = PhotoImage(file="pictures/buttonAdd2.gif")
saveButton.config(image=inputButtonImg)
saveButton.image = inputButtonImg

buttonruleActualize=Button(frame_up,command=resetAll)
buttonruleActualize.grid(row=1,column=0) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
buttonActualizeImg = PhotoImage(file="pictures/afficher.gif")
buttonruleActualize.config(image=buttonActualizeImg)
buttonruleActualize.image = buttonActualizeImg

entryRule = Entry(frame_up, bd=5, width=90,textvariable=rule,foreground='red',font='Helvetica 14 bold')
entryRule.place(x=75,y=38)

##################################### partie inférieure frame_down #######################################


labelDown = Label(frame_down,textvariable= iptableResult)
labelDown.place(x=150,y=10)
labelDown.configure(foreground="white",bg='#000000')
iptableResult.set("")

buttonFichier=Button(frame_down,command=scriptLoad)
buttonFichier.place(x=0,y=0) # Les quatres prochaines lignes sont relatives à la mise en forme du bouton
fichierImg = PhotoImage(file="pictures/fichier.gif")
buttonFichier.config(image=fichierImg)
buttonFichier.image = fichierImg

labelName = Label(frame_down, text="Select one user :", foreground='black',bg='#dad6d5')
labelName.place(x=602,y=0)

listboxUserToIp = Listbox(frame_down, height =2) # création de la listbox pour choisir vers quelle adresse IP/USER la connexion SSH doit être effectuée 
listboxUserToIp.place(x=720,y=0)

databaseCreationIpUser()
listboxIntegration ()

actualizeButton=Button(frame_down, text="Actualize", foreground = "black", command=getIpInDatabase)
actualizeButton.place(x=890,y=0)

iptable_window.mainloop()