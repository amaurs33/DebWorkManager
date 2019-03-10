#!/usr/bin/python
# -*- coding: latin-1 -
from Tkinter import *
import subprocess



win_iptable = Tk()
iptableResult = StringVar()
frame_down = Frame (win_iptable,height=800,width=1000,relief=RAISED,bd=8,bg="black")
frame_up = Frame (win_iptable,height=800,width=1000,bd=8,bg="white")
frame_down.grid(row=1,column=0)
frame_up.grid(row=0,column=0)
win_iptable.title("Configuration des régles iptables")
win_iptable.configure(bg='#ffffff')
win_iptable.geometry("1000x850")
win_iptable.resizable(width=False,height=False)


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

labelDown = Label(frame_down,textvariable= iptableResult)
labelDown.place(x=150,y=10)
labelDown.configure(foreground="white",bg='#000000')
iptableResult.set("")

buttonActualiser=Button(frame_down, text="Actualiser", foreground = "black")#, command=route)
buttonActualiser.place(x=890,y=0)
win_iptable.mainloop()