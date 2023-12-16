import tkinter.font
from tkinter import *
from turtle import Turtle
from PIL import Image, ImageTk

current_image_index = 0

window=Tk()
window.title("game")
window.geometry("600x600+300+0")

def change_label_image():
    global current_image_index

    # 이미지 파일 경로의 리스트 (자신의 이미지 경로로 바꾸세요)
    image_paths = ["C:\\Users\\user\Desktop\OIP (1).jpeg", "C:\\Users\\user\Desktop\OIP.jpeg"]

    # Change the index to the next image
    current_image_index = (current_image_index + 1) % len(image_paths)

    # Load the new image
    new_image_path = image_paths[current_image_index]
    new_image = Image.open(new_image_path)
    new_tk_image = ImageTk.PhotoImage(new_image)

    # Update the label image
    w.config(image=new_tk_image)
    w.image = new_tk_image

    new_label1_paths=['1번 남돌2','1번 남돌3','1번 남돌4','1번 남돌5']
    new_label1.config(text=new_label1_paths[current_image_index])

    new_label2_paths = ['2번 2남돌2', '2번 남돌23', '2번 남돌24', '2번 남돌25']
    new_label2.config(text=new_label2_paths[current_image_index])

    new_label3_paths = ['3번 남돌32', '3번 남돌33', '3번 남돌34', '3번 남돌35']
    new_label3.config(text=new_label3_paths[current_image_index])

    new_label4_paths = ['4번 남돌42', '4번 남돌43', '4번 남돌44', '4번 남돌45']
    new_label4.config(text=new_label4_paths[current_image_index])

    new_label5_paths = ['5번 남돌52', '5번 남돌53', '5번 남돌54', '5번 남돌55']
    new_label5.config(text=new_label5_paths[current_image_index])




font1=tkinter.font.Font(family="많은 고딕",size=20)
label=Label(window,text="IDOL-FACE-Game",width=40,height=3,font=font1)
label['fg']="black"
label['bg']="green"

label.pack()



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




new_problem2=Button(window,text='다음문제',command=change_label_image,font=font3)

new_problem2['fg'] = "black"
new_problem2['bg'] = "yellow"

new_problem2.pack()



window.mainloop()