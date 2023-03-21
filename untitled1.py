from tkinter import *
from PIL import ImageTk, Image

import random 


root =Tk()
root.geometry("500x500")
root.config(bg="green")

img=ImageTk.PhotoImage(Image.open ("dice1.4.jpg"))



label_1=Label(root , text="Jugador 1")
label_1.place(relx=0.2 , rely=0.5 )

label_2=Label(root , text="Jugador 2")
label_2.place(relx=0.8 , rely=0.5)

label_3=Label(root , text="a")
label_3.place(relx=0.2 , rely=0.6)

label_4=Label(root , text="b")
label_4.place(relx=0.8 , rely=0.6)

button_1=Button(root , image=img)

root.mainloop()