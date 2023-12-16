import tkinter.font
from tkinter import *
from turtle import Turtle
from PIL import Image, ImageTk


window=Tk()
window.title("game")
window.geometry("600x600+300+0")
















#버튼 클릭 시 삭제
def on_button_click1(button):
    button.destroy()

    new_image_path ="C:\\Users\\user\Desktop\OIP.jpeg"
    new_image = Image.open(new_image_path)

    new_tk_image = ImageTk.PhotoImage(new_image)

    w.config(image=new_tk_image)
    w.image = new_tk_image

    font3 = tkinter.font.Font(family="많은 고딕", size=13)





    new_label1=Label(window,text='1번 아이브',font=font3)
    new_label1['fg'] = "black"
    new_label1['bg'] = "green"
    new_label1.pack()

    new_label2 = Label(window, text='2번 블랙핑크',font=font3)
    new_label2['fg'] = "black"
    new_label2['bg'] = "green"
    new_label2.pack()

    new_label3 = Label(window, text='3번 트와이스',font=font3)
    new_label3['fg'] = "black"
    new_label3['bg'] = "green"
    new_label3.pack()

    new_label4 = Label(window, text='4번 있지',font=font3)
    new_label4['fg'] = "black"
    new_label4['bg'] = "green"
    new_label4.pack()

    new_label5 = Label(window, text='5번 뉴진스',font=font3)
    new_label5['fg'] = "black"
    new_label5['bg'] = "green"
    new_label5.pack()

    new_answer_button = Button(window, text='정답입력', font=font3)
    new_answer_button ['fg'] = "black"
    new_answer_button ['bg'] = "yellow"
    new_answer_button .pack()




    new_problem2=Button(window,text='다음문제',font=font3)

    new_problem2['fg'] = "black"
    new_problem2['bg'] = "yellow"

    new_problem2.pack()

















font1=tkinter.font.Font(family="많은 고딕",size=20)
label=Label(window,text="IDOL-FACE-Game",width=40,height=3,font=font1)
label['fg']="black"
label['bg']="green"



label.pack()

click_count = IntVar()
click_count.set(0)

#이미지를 넣어야 함
image_path = "C:\\Users\\user\Desktop\png-clipart-kakaotalk-kakao-friends-sticker-iphone-iphone-electronics-smiley.png"
image = Image.open(image_path)
original_image = Image.open(image_path)

new_size = (300, 300)
resized_image = original_image.resize(new_size)
tk_image = ImageTk.PhotoImage(resized_image)


w=Label(window,width=new_size[0], height=new_size[1],image=tk_image)
w.image=tk_image


w.pack()

font3=tkinter.font.Font(family="많은 고딕",size=30)
start_button=Button(window,text="start",command=lambda:on_button_click1(start_button),font=font3)

start_button['bg']='green'
start_button['fg']='black'

start_button.pack()
window.mainloop()