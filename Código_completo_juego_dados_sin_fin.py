from tkinter import *
from PIL import ImageTk, Image
import random

root=Tk()
root.title("Juego de dados sin fin")
root.geometry("600x400")
root.configure(background="yellow2")

img=ImageTk.PhotoImage(Image.open ("dice1.4.jpg"))


root.mainloop()