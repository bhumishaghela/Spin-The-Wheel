import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
import random
def rotate():
    startlist=[0,60,120,180,240,300]
    placelist=[(0.475,0.45),(0.39,0.37),(0.31,0.45),(0.31,0.54),(0.39,0.61),(0.47,0.53)]
    while startlist[len(startlist)-1]!=0:
        startlist = startlist[-1:] + startlist[:-1]
        placelist = placelist[-1:] + placelist[:-1]
        for i in range(0,len(startlist)):
            canvas.itemconfig(listarc[i],start=startlist[i])
            listtext[i].place(relx=placelist[i][0],rely=placelist[i][1])    
        canvas.pack()
        root.update()
        time.sleep(0.3)
    
        
def winner():
    won_discount=random.choice(listtext)
    messagebox.showinfo("Congratulations You Won A Discount!",listtextdic[won_discount])
    
    
    
def spin():
    count=0
    while count<=5:
        rotate()
        
        count+=1
    winner()
    
root=tk.Tk()
title=root.title("SPIN THE WHEEL AND GET DISCOUNT")
root.resizable(0,0)
canvas=tk.Canvas(root, width=1000, height=871)
coord = 300,300,590,590
arc1=canvas.create_arc(coord, start=0, extent=60, fill="blue")
text1 = Label(canvas, text="Get 500 Rs Off",bg="blue",font="Arial 9 bold")
text1.place(relx=0.475,rely=0.45)


arc2=canvas.create_arc(coord, start=60, extent=60,fill="orange")
text2 = Label(canvas, text="Get 50% discount",bg="orange",font="Arial 9 bold")
text2.place(relx=0.39,rely=0.37)

arc3=canvas.create_arc(coord, start=120, extent=60,fill="red")
text3 = Label(canvas, text="Money Back offer",bg="red",font="Arial 9 bold")
text3.place(relx=0.31,rely=0.45)

arc4=canvas.create_arc(coord, start=180, extent=60,fill="green")
text4 = Label(canvas, text="Free Membership",bg="green",font="Arial 9 bold")
text4.place(relx=0.31,rely=0.54)


arc5=canvas.create_arc(coord, start=240, extent=60, fill="yellow")
text5 = Label(canvas, text="Buy 1 Get 1 Free",bg="yellow",font="Arial 9 bold")
text5.place(relx=0.39,rely=0.61)

arc6=canvas.create_arc(coord, start=300, extent=60, fill="purple")
text6 = Label(canvas, text="250 Rs cashback",bg="purple",font="Arial 9 bold")
text6.place(relx=0.47,rely=0.53)


start=Button(text="Spin",command=spin,bd=5,font="comicsansms 15")
listarc=[arc1,arc2,arc3,arc4,arc5,arc6]
listtextdic={text1:"Get 500 Rs Off on purchase above Rs 1200",text2:"Get 50% discount on orders over 3000 Rs",text3:"Money Back offer on Payment with Debit Card",text4:"Free Membership on order over 5000rs",text5:"Buy 1 Get 1 Free on order over 500 rs",text6:"250 Rs cashback on PayPal  purchase"}
listtext=list(listtextdic.keys())
start.place(relx=.41, rely=.48)
canvas.pack()
root.mainloop()



