from tkinter import *
from PIL import Image,ImageTk
import emoji
import keyboard
import time

root=Tk()

bot = "Eye: "

version = 1.0

def send():

    file = open("cerebro.txt",'r')

    send="Tu: "+a.get() 

    text.insert('end',"\n" + send)

    #Hola
    if(a.get()=='hi'):
        data = file.readlines()[0]   
        text.insert('end', '\n' + bot + data )
   
    elif(a.get()=='hola'):
        data = file.readlines()[1]   
        text.insert('end', '\n' + bot + data)
       
    elif(a.get()=='hola tambien'):
        data = file.readlines()[2]   
        text.insert('end', '\n' + bot + data) 

    elif(a.get()=='hola?'):
        data = file.readlines()[3]   
        text.insert('end', '\n' + bot + data)
    

    #Como estas?
    if(a.get()=='como estas?'):
        data = file.readlines()[5]   
        text.insert('end', '\n' + bot + data)

    elif(a.get()=='como te sentis?'):
        data = file.readlines()[6]   
        text.insert('end', '\n' + bot + data)

    elif(a.get()=='como te sientes?'):
        data = file.readlines()[7]   
        text.insert('end', '\n' + bot + data)

    elif(a.get()=='estas bien?'):
        data = file.readlines()[8]   
        text.insert('end', '\n' + bot + data)
    

    #Me siento bien
    if(a.get()=='bien'):
        data = file.readlines()[10]   
        text.insert('end', '\n' + bot + data)

    elif(a.get()=='muy bien'):
        data = file.readlines()[11]   
        text.insert('end', '\n' + bot + data)

    elif(a.get()=='me siento bien'):
        data = file.readlines()[12]   
        text.insert('end', '\n' + bot + data)

    elif(a.get()=='de maravilla'):
        data = file.readlines()[13]   
        text.insert('end', '\n' + bot + data)

    elif(a.get()=='feliz'):
        data = file.readlines()[14]   
        text.insert('end', '\n' + bot + data)

    elif(a.get()=='si'):
        data = file.readlines()[14]   
        text.insert('end', '\n' + bot + data) 



    #Tema (ella me dejo) version mujer

    if(a.get()=='ella me dejo'):
        data = file.readlines()[19]   
        text.insert('end', '\n' + bot + data)

    elif(a.get()=='estas ahi?'):
        data = file.readlines()[20]   
        text.insert('end', '\n' + bot + data)

    elif(a.get()=='me das un consejo?'):
        data = file.readlines()[21]   
        text.insert('end', '\n' + bot + data)

    elif(a.get()=='crees que no me vuelva a hablar?'):
        data = file.readlines()[22]   
        text.insert('end', '\n' + bot + data)

    elif(a.get()=='alguna vez tuvistes'):
        data = file.readlines()[23]   
        text.insert('end', '\n' + bot + data)

    elif(a.get()=='alguna vez tuvistes novia?'):
        data = file.readlines()[23]   
        text.insert('end', '\n' + bot + data) 


    

root.title("The eye " + str(version))
root.iconbitmap('Assets/Eye.ico')
root.geometry("700x700")
root.config(background_="Black")

text = Text(root, width=85, height=37, bg="black", fg= "light gray",borderwidth = 0, font=("Consolas", 11))
text.place(x=0, y=0)

BotLabel = Label(text = bot, fg="green", bg="black", font=("Consolas", 11))

a = Entry(root, width=80, bg="black", fg="light gray", font=("Consolas", 11))
a.config(insertbackground='white')

img = Image.open('Assets/Send.png')
img = img.resize((32, 32), Image.ANTIALIAS) # Redimension (Alto, Ancho)
img = ImageTk.PhotoImage(img)

Send = Button(root, bg='black', fg="dark gray", borderwidth = 0, image=img, text= "", width=50, height=25,command=send, font=("Consolas", 11))
Send.place(x=650, y=666)
a.place(x=0, y=670)
#a.grid(row=1, column=0)

text.insert('end', '\n' + "Escribe /help o di hola")
text.insert('end', '\n' + "")

root.wait_visibility(root)
root.wm_attributes('-alpha',0.9)   # transparent windows  0.9 - 9



root.mainloop()