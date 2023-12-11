import tkinter.font
from tkinter import *
import tkinter.ttk as ttk
from turtle import Turtle
import cv2
import mediapipe as mp
#그리기 도구 지원해주는 서브 패키지
mp_drawing = mp.solutions.drawing_utils

#손 감지 모듈
mp_hands = mp.solutions.hands





window=Tk()
window.title("game")
window.geometry("600x600+300+0")




def createnewWindow():
    global newWindow
    newWindow=Toplevel(window)
    idol_image_label=Label(newWindow,text="아이돌 합성 이미지 사진")
    idol_image_label.pack()


    font1_1 = tkinter.font.Font(family="많은 고딕", size=20)


    button1=Button(newWindow,font=font1_1,text="1번")
    button2=Button(newWindow,font=font1_1,text="2번")
    button3 = Button(newWindow, font=font1_1, text="3번")
    button4 = Button(newWindow, font=font1_1, text="4번")

    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()

    # 캠 키기
    cap = cv2.VideoCapture(0)

    # mp_hands의 Hands 정보를 설정하고 읽어들임
    with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5,
                        min_tracking_confidence=0.5) as hands:

        # 캠이 켜져있을때
        while cap.isOpened():

            # 캠 읽기 성공여부 success와 읽은 이미지를 image에 저장
            success, mediaPipeimage = cap.read()

            # 캠 읽기 실패시 continue
            if not success:
                continue

            # 이미지 값 좌우반전 ( 캠 켰을때 반전된 이미지 보완 )
            # 이미지 값 순서를 BGR -> RGB로 변환
            # 이미지 순서가 RGB여야 Mediapipe 사용가능
            mediaPipeimage = cv2.cvtColor(cv2.flip(mediaPipeimage, 1), cv2.COLOR_BGR2RGB)

            # Image에서 손을 추적하고 결과를 result에 저장
            result = hands.process(mediaPipeimage)

            # 이미지 값 순서를 RGB에서 BGR로 다시 바꿈(mediaPipe에서는 BGR순서만 인식)
            mediaPipeimage = cv2.cvtColor(mediaPipeimage, cv2.COLOR_RGB2BGR)

            # 캠 화면에 띄울 텍스트 정의 ( 기본 값 )
            gesture_text = 'Cant found hand'

            # 결과 result가 제대로 추적이 되었을때
            if result.multi_hand_landmarks:
                # 첫 번째로 추적된 손을 hand_landmarks에 할당
                hand_landmarks = result.multi_hand_landmarks[0]

                # 검지 ~ 소지 까지의 다 펴져있는지에 대한 bool 변수들 선언
                finger_1 = False
                finger_2 = False
                finger_3 = False
                finger_4 = False
                finger_5 = False

                # 4번 마디가 2번 마디 보다 y값이 작으면 finger_1를 참
                if (hand_landmarks.landmark[4].y < hand_landmarks.landmark[2].y):
                    finger_1 = True

                # 8번 마디가 6번 마디 보다 y값이 작으면 finger_2를 참
                if (hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y):
                    finger_2 = True

                # 12번 마디가 10번 마디 보다 y값이 작으면 finger_3를 참
                if (hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y):
                    finger_3 = True

                # 16번 마디가 14번 마디 보다 y값이 작으면 finger_4를 참
                if (hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y):
                    finger_4 = True

                # 20번 마디가 18번 마디 보다 y값이 작으면 finger_5를 참
                if (hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y):
                    finger_5 = True

                if (finger_2 and finger_4 and finger_3):
                    gesture_text = 'three fingers'

                # 5손가락 다 펴져있으면 " 보 "
                elif (finger_1 and finger_2 and finger_3 and finger_4 and finger_5):
                    gesture_text = 'Bo'


                # 1, 2번 손가락이 펴져있으면 "가위 "
                elif (finger_1 and finger_2):
                    gesture_text = 'Gawi'

                # 모든 손가락이 안펴져있으면 " 바위 "
                elif ((not finger_2) and (not finger_3) and (not finger_4)
                      and (not finger_5)):
                    gesture_text = 'Bawi'



                # 모두 아닐시 모르겠다는 텍스트
                else:
                    gesture_text = 'Mo Ru Get Saw Yo'

                # 캠 화면에 손가락을 그림
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # 캠화면에 텍스트를 작성
            cv2.putText(image, text='223323 : {}'.format(gesture_text)
                        , org=(10, 30), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=1, color=(0, 0, 255), thickness=2)

            # 캠 화면 ( 이미지 )을 화면에 띄움
            cv2.imshow('image', image)

            # q입력시 종료
            if cv2.waitKey(1) == ord('q'):
                break

    # 캠 종료
    cap.release()
    cv2.destroyAllWindows()


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
start_button=Button(window,text="start",command=createnewWindow(),font=font3)

start_button['bg']='green'
start_button['fg']='black'

start_button.pack()





window.mainloop()