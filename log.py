#!/usr/bin/python
# -*- coding: latin-1 -*-
from Tkinter import *
import subprocess





def log() :


	logPrint = subprocess.Popen(["tail",cheminLog], stdout=subprocess.PIPE)
	output = logPrint.communicate()[0]
	print(output)
	log_label.set(output)




		
winlog = Tk()

log_label = StringVar()
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
dc['syslog'] = r'/var/log/syslog'
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

winlog.mainloop()	

		