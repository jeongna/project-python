import tkinter.font
from tkinter import *
from turtle import Turtle


window=Tk()
window.title("game")
window.geometry("600x600+300+0")




def createNewWindow():
    newWindow=Toplevel(window)


font1=tkinter.font.Font(family="많은 고딕",size=20)
label=Label(window,text="IDOL-FACE-Game",width=40,height=5,font=font1)
label['fg']="black"
label['bg']="green"



label.pack()

#이미지를 넣어야 함
font2=tkinter.font.Font(family="많은 고딕",size=30)
w=Label(window,text="연예인 사진 불러올자리",width=20,height=8,font=font2)
w['fg']="black"
w['bg']="green"
w.pack()

font3=tkinter.font.Font(family="많은 고딕",size=30)
start_button=Button(window,text="start",command=createNewWindow(),font=font3)

start_button['bg']='green'
start_button['fg']='black'

start_button.pack()
window.mainloop()