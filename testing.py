from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("Rock Paper scisssor")
root.geometry("400x400")
root.configure(background="#96c4b2")

paper_image_user = PhotoImage(file="paper.png")

user_label = Label(root, image=paper_image_user)
user_label=Label(root,image="paper_image_user")
user_label.pack()

root.mainloop()