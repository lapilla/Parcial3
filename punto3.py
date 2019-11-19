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

led6 = placa.get_pin('d:8:o')
led1 = placa.get_pin('d:9:p')
led2 = placa.get_pin('d:10:p')
led3 = placa.get_pin('d:11:p')
led4 = placa.get_pin('d:12:o')
led5 = placa.get_pin('d:13:o')

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
texto = Label(ventana, text="ingresa un valor de 8 - 13", bg='cadet blue1', font=("Arial Bold", 14), fg="white")
texto.place(x=20, y=20)
texto1 = Label(ventana, text="ingresa 0 para apagar y 1 para encender los leds", bg='cadet blue1', font=("Arial Bold", 14), fg="white")
texto1.place(x=20, y=100)
def led(input):
    content = dato1.get()
    dato1.delete(0, END)
    if int(content)== 1:
        led1.write(1)
        led2.write(1)
        led3.write(1)
        led4.write(1)
        led5.write(1)
        led6.write(1)
    if int(content)== 0:
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)
        led6.write(0)
    
def entrada(input):
    content = dato.get()
    dato.delete(0, END)
    if int(content)== 8:
        led1.write(1)
        time.sleep(2)
        led1.write(0)
    if int(content)== 9:
        led2.write(1)
        time.sleep(2)
        led2.write(0)
    if int(content)== 10:
        led3.write(1)
        time.sleep(2)
        led3.write(0)
    if int(content)== 11:
        led4.write(1)
        time.sleep(2)
        led4.write(0)
    if int(content)== 12:
        led5.write(1)
        time.sleep(2)
        led5.write(0)
    if int(content)== 13:
        led6.write(1)
        time.sleep(2)
        led6.write(0)
        
    print(content)
    if (int(content)< 8):
        print('Ingrese un nuevo numero entre 8 y 13')
    if (int(content)> 13):
        print('Ingrese un nuevo numero entre 8 y 13')
    
Label(ventana, text="Entrada: ").place(x=20, y=60)
dato = Entry(ventana)
dato.place(x=90, y=60)
dato.bind('<Return>', entrada) 
dato1 = Entry(ventana)
dato1.place(x=90, y=140)
dato1.bind('<Return>', led)
bot1=Button(ventana, text ="Guardar", font=("Times New Roman",15), command=led)
bot1.place(x=90,y=200)
bot2=Button(ventana, text ="Actualizar", font=("Times New Roman",15), command=led)
bot2.place(x=200,y=200)
ventana.mainloop()


