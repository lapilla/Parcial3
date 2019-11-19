import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from pyfirmata import Arduino, util
from tkinter import *
from PIL import Image
from PIL import ImageTk
import time

placa = Arduino ('COM3')
it = util.Iterator(placa)
it.start()

led1 = placa.get_pin('d:9:p')

time.sleep(0.1)
ventana = Tk()
ventana.geometry('800x600')
ventana.title("Parcial")

# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:/Users/Labing/Documents/Parcial/key/key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://parcial-314e7.firebaseio.com/'
})


frame1 = Frame(ventana, bg="pink", highlightthickness=1, width=1280, height=800, bd= 5)
frame1.place(x = 0,y = 0)

valor= Label(frame1, bg='cadet blue', font=("Arial Bold", 15), fg="white", width=5)
pot1=StringVar()
valor1= Label(frame1, bg='cadet blue', font=("Arial Bold", 15), fg="white", width=5)
pot2=StringVar()
valor2= Label(frame1, bg='cadet blue', font=("Arial Bold", 15), fg="white", width=5)
pot3=StringVar()

def pot_A0():
    ref = db.reference('sensor/sensor1')
    x=ref.get()  
    y=x.get('pot1')
    print('pot1:',y)
    led1.write(y)


def pot_A1():
    ref = db.reference('sensor/sensor1')
    x=ref.get()  
    y=x.get('pot2')
    print('pot2:',y)
    led1.write(y)


def pot_A2():
    ref = db.reference('sensor/sensor1')
    x=ref.get()  
    y=x.get('pot3')
    print('pot2:',y)
    led1.write(y)


valor.configure(textvariable=pot1)
valor.place(x=20, y=30)
adc1_update=Button(text="pot_A0",command=pot_A0)
adc1_update.place(x=120, y=36)

valor2.configure(textvariable=pot2)
valor2.place(x=20, y=60)
adc2_update=Button(text="pot_A1",command=pot_A1)
adc2_update.place(x=120, y=70)

valor1.configure(textvariable=pot3)
valor1.place(x=20, y=90)
adc3_update=Button(frame1,text="pot_A2",command=pot_A2)
adc3_update.place(x=114, y=94)


ventana.mainloop()
