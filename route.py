#!/usr/bin/python
# -*- coding: latin-1 -*-
from Tkinter import *
import subprocess



	
def route() :

	routePrint = subprocess.Popen(["route","-n"], stdout=subprocess.PIPE)
	output = routePrint.communicate()[0]
	#print(output)
	route_label.set(output)
	
	#route_label.set(output)



newwin = Tk()
	#route_label = ""

route_label = StringVar()

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
	#route_label.set("")
buttonActualiser=Button(frame_down, text="Actualiser", foreground = "black", command=route)
buttonActualiser.place(x=690,y=0)
newwin.mainloop()


