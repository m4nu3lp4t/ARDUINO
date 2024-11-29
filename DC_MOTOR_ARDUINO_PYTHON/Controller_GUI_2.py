from tkinter import *
import tkinter as tk
#from tkinter import ttk
import serial, time
from functools import partial

encendido = '0'
velocidad = '200'
rot = '1,0'

izq = '1,0'
der = '0,1'
comando = encendido +','+ velocidad +','+ rot
comando += str('\n')

puerto = "COM6"
baud_rate = 9600
board = serial.Serial(puerto,baud_rate,timeout=1)
board.close()

#################################################################################################

def button_start(dat):
    encendido = '1'
    velocidad = str(sca.get())
    rot = rotacion.get()
    comando = encendido +','+ velocidad +','+ rot
    print(comando)
    board.open()
    time.sleep(1.8)                                                         #Se tiene que agregar este delay !!!
    board.write(comando.encode(encoding = 'ascii', errors = 'strict'))
    board.close()

def button_stop(dat):
    comando = '0,0,0,0'
    board.open()
    board.write(comando.encode(encoding = 'ascii', errors = 'strict'))
    board.close()

def button_update(dat):
    encendido = '1'
    velocidad = str(sca.get())
    rot = rotacion.get()
    comando = encendido +','+ velocidad +','+ rot
    print(comando)
    board.open()
    time.sleep(1.8)                                                         #Se tiene que agregar este delay !!!
    board.write(comando.encode(encoding = 'ascii', errors = 'strict'))
    board.close()
 
def callback(selection):
    print(selection)

def scale_vel(self, _event=None):
    velocidad = str(sca.get())
    rot = rotacion.get()
    comando = encendido+','+velocidad+','+ rot
    #print(comando)

#################################################################################################

root = Tk()
root.geometry('400x500')
root.title("DC Motor Controller")
label_0 = Label(root, text="DC Motor Controller",width=20,font=("bold", 20))
label_0.place(x=50,y=53)

#################################################################################################

label_1 = Label(root, text="Port",width=20, font=("bold", 10))
label_1.place(x=60,y=135)
list1 = ['COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8']
pt=StringVar(root)
pt.set('Select Port') 
droplist1=OptionMenu(root,pt, *list1, command=callback)
droplist1.pack() 
puerto = pt.get()
droplist1.config(width=15)
droplist1.place(x=170,y=130)

#################################################################################################

label_2 = Label(root, text="Baud Rate",width=20,font=("bold", 10))
label_2.place(x=50,y=185)

list2 = [4800,9600,14400,19200,38400,57600,115200,128000]
br=StringVar()
br.set('Select Baud Rate') 
droplist2=OptionMenu(root,br, *list2, command=callback) 
droplist2.pack() 
baud_rate = br.get()
droplist2.config(width=15)
droplist2.place(x=170,y=180)

#################################################################################################

label_3 = Label(root, text="Rotation",width=20,font=("bold", 10))
label_3.place(x=55,y=240)
rotacion = StringVar(value=',1,0')
BUTTON_OPTS = dict(variable=rotacion, command=lambda: print(rotacion.get()))
Radiobutton(root, text='CW', value=izq, **BUTTON_OPTS).place(x=185,y=240)
Radiobutton(root, text='CWW', value=der, **BUTTON_OPTS).place(x=240,y=240)
rotacion.set(value=izq)

#################################################################################################

sca = tk.Scale(root, bd=1, from_=150, to=250, orient=HORIZONTAL,length=180,width=20,command=scale_vel)
sca.pack()
sca.place(x=100,y=270) #x=120,y=370
# Label widget
tk.Label(root, text="SPEED  ").place(x=50,y=290)   #x=50,y=390

##############################################################################################################

btn3 = Button(root, bd=2,text='UPDATE',width=10,bg='grey',fg='white',  command=partial(button_update, comando))
btn3.pack()
btn3.place(x=300,y=290) #x=130,y=440

##############################################################################################################

btn1 = Button(root, bd=2,text='START',width=20,bg='green',fg='white',  command=partial(button_start, comando))
btn1.pack()
btn1.place(x=130,y=350) #x=130,y=290

##############################################################################################################

btn2 = Button(root, bd=2,text='STOP',width=20,bg='brown',fg='white',  command=partial(button_stop, comando))
btn2.pack()
btn2.place(x=130,y=400) #x=130,y=340

##############################################################################################################



root.mainloop()
