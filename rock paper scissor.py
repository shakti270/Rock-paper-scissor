from tkinter import *
from PIL import Image,ImageTk
from random import randint


#main window
root = Tk()
root.title("Rock Paper scisssor")
root.configure(background="#667589")
#root.geometry("1100x400")

#pictures
rock_image_user=ImageTk.PhotoImage(Image.open("rockk.png"))
paper_image_user=ImageTk.PhotoImage(Image.open("paper.png"))
scissor_image_user=ImageTk.PhotoImage(Image.open("scissor.png"))
rock_image_comp=ImageTk.PhotoImage(Image.open("rockku.png"))
paper_image_comp=ImageTk.PhotoImage(Image.open("paperu.png"))
scissor_image_comp=ImageTk.PhotoImage(Image.open("scissoru.png"))

#dispaying pictures
user_label=Label(root,image=rock_image_user,bg="#667589")
comp_label=Label(root,image=rock_image_comp,bg="#667589")

comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores
comp_score= Label(root,text=0,font=100,bg="#667589",fg="white")
user_score= Label(root,text=0,font=100,bg="#667589",fg="white")
comp_score.grid(row=1,column=1)
user_score.grid(row=1,column=3)

#indicators
user_indicator=Label(root,font=50,text="USER",background="#667589")
comp_indicator=Label(root,font=50,text="COMPUTER",background="#667589")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg=Label(root,font=50,fg="white",bg="#667589")
msg.grid(row=3,column=2)

#update message
def updatemsg(text):
    msg["text"] = text 
   
#update user score
def updateuserscore():
   score = int(user_score.cget("text")) 
   score +=1
   user_score["text"]=str(score)

#update computer score
def updatecompscore():
   score = int(comp_score.cget("text")) 
   score +=1
   comp_score["text"]=str(score)  

#check winner
def check(player,computer):
   if player == computer:
      updatemsg("it is a tie")
   elif player=="rock":  
      if computer=="paper":
         updatemsg("you loose")
         updatecompscore()
      else:
         updatemsg("you win")
         updateuserscore()
   elif player=="paper":
      if computer=="scissor":
         updatemsg("you loose")
         updatecompscore()
      else  :
         updatemsg("you win")
         updateuserscore()
   elif player=="scissor":
      if computer=="paper":
         updatemsg("you win")
         updateuserscore()
      else  :
         updatemsg("you loose")
         updatecompscore()   
   else :
      pass    

#function for decisons
choices=["rock" , "paper" , "scissor"]
def dec(x):
    #for comp
    compchoice=choices[randint(0,2)]
    if compchoice=="rock":
      comp_label.configure(image=rock_image_comp)
    elif compchoice=="paper":
      comp_label.configure(image=paper_image_comp)
    else:
      comp_label.configure(image=scissor_image_comp)        

     #for user
    if x =="rock":
        user_label.configure(image=rock_image_user)
    elif x=="paper":
        user_label.configure(image=paper_image_user)
    else:
        user_label.configure(image=scissor_image_user)

    check(x,compchoice)

#button
rock=Button(root,width=20,height=2,text="ROCK",bg="#102d55",fg="white",command=lambda:dec("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="#102d55",fg="white",command=lambda:dec("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="#102d55",fg="white",command=lambda:dec("scissor")).grid(row=2,column=3)


root.mainloop()