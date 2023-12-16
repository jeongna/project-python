import tkinter.font
from tkinter import *

from PIL import Image, ImageTk


import mediapipe as mp
import cv2

################################
import cv2
import dlib
import numpy as np

# Dlib의 얼굴 인식기와 특징점 모델 로드
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def get_face_landmarks(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)
        return np.array([[p.x, p.y] for p in landmarks.parts()])
    return None

def average_landmarks(images):
    all_landmarks = [get_face_landmarks(image) for image in images]
    return np.mean(all_landmarks, axis=0)

def align_and_blend_faces(images):
    avg_landmarks = average_landmarks(images)

    aligned_faces = []
    for image in images:
        landmarks = get_face_landmarks(image)
        transformation_matrix = cv2.estimateAffinePartial2D(landmarks, avg_landmarks)[0]
        aligned_face = cv2.warpAffine(image, transformation_matrix, (images[0].shape[1], images[0].shape[0]))
        aligned_faces.append(aligned_face)

    # 모든 정렬된 얼굴을 평균화
    blended_face = np.mean(aligned_faces, axis=0).astype(np.uint8)
    return blended_face                                                                                                                                                                  # 공통 경로 정의


base_path="image\\"

## image1 (Newjeans)
image_files1 = ['image1_1.jpg', 'image1_2.jpg', 'image1_3.jpg', 'image1_4.jpg', 'image1_5.jpg']
images1 = [cv2.imread(base_path + filename) for filename in image_files1]

## image2 (BTS)
image_files2 = ['image2_1.jpg', 'image2_2.jpg', 'image2_3.jpg', 'image2_4.jpg', 'image2_5.jpg']
images2 = [cv2.imread(base_path + filename) for filename in image_files2]

## image3 (BlackPink)
image_files3 = ['image3_1.jpg', 'image3_2.jpg', 'image3_3.jpg', 'image3_4.jpg']
images3 = [cv2.imread(base_path + filename) for filename in image_files3]

## image4 (Ive)
image_files4 = ['image4_1.jpg', 'image4_2.jpg', 'image4_3.jpg','image4_4.jpg','image4_5.jpg']
images4 = [cv2.imread(base_path + filename) for filename in image_files4]

## image5 (세븐틴)
image_files5 = ['image5_1.jpg','image5_2.jpg','image5_3.jpg','image5_4.jpg','image5_5.jpg','image5_6.jpg']
images5 = [cv2.imread(base_path + filename) for filename in image_files5]

## image6 (Twice)
image_files6 = ['image6_1.jpg','image6_2.jpg','image6_3.jpg','image6_4.jpg','image6_5.jpg','image6_6.jpg','image6_7.jpg','image6_8.jpg']
images6 = [cv2.imread(base_path + filename) for filename in image_files6]

## image7 (르세라핌)
image_files7 = ['image7_1.jpg','image7_2.jpg','image7_3.jpg','image7_4.jpg','image7_5.jpg']
images7 = [cv2.imread(base_path + filename) for filename in image_files7]

## image8 (에스파)
image_files8 = ['image8_1.jpg','image8_2.jpg','image8_3.jpg','image8_4.jpg']
images8 = [cv2.imread(base_path + filename) for filename in image_files8]

## image9 (엑소)
image_files9 = ['image9_1.jpg','image9_2.jpg','image9_3.jpg','image9_4.jpg','image9_5.jpg','image9_6.jpg']
images9 = [cv2.imread(base_path + filename) for filename in image_files9]

## image10 (소녀시대)
image_files10 = ['image10_1.jpg','image10_2.jpg','image10_3.jpg','image10_4.jpg','image10_5.jpg','image10_6.jpg']
images10 = [cv2.imread(base_path + filename) for filename in image_files10]

# 얼굴 합성
combined_face1 = align_and_blend_faces(images1)
combined_face2 = align_and_blend_faces(images2)
combined_face3 = align_and_blend_faces(images3)
combined_face4 = align_and_blend_faces(images4)
combined_face5 = align_and_blend_faces(images5)
combined_face6 = align_and_blend_faces(images6)
combined_face7 = align_and_blend_faces(images7)
combined_face8 = align_and_blend_faces(images8)
combined_face9 = align_and_blend_faces(images9)
combined_face10 = align_and_blend_faces(images10)

# 이미지 저장
cv2.imwrite(".\\combine\\face1.jpg", combined_face1)
cv2.imwrite(".\\combine\\face2.jpg", combined_face2)
cv2.imwrite(".\\combine\\face3.jpg", combined_face3)
cv2.imwrite(".\\combine\\face4.jpg", combined_face4)
cv2.imwrite(".\\combine\\face5.jpg", combined_face5)
cv2.imwrite(".\\combine\\face6.jpg", combined_face6)
cv2.imwrite(".\\combine\\face7.jpg", combined_face7)
cv2.imwrite(".\\combine\\face8.jpg", combined_face8)
cv2.imwrite(".\\combine\\face9.jpg", combined_face9)
cv2.imwrite(".\\combine\\face10.jpg", combined_face10)

#######################################################################

current_image_index = 0



window=Tk()
window.title("game")
window.geometry("600x600+300+0")

def fingerfuction():

    import mediapipe as mp

    # 그리기 도구 지원해주는 서브 패키지
    mp_drawing = mp.solutions.drawing_utils

    # 손 감지 모듈
    mp_hands = mp.solutions.hands

    # 캠 키기
    cap = cv2.VideoCapture(0)

    # mp_hands의 Hands 정보를 설정하고 읽어들임
    with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5,
                        min_tracking_confidence=0.5) as hands:

        # 캠이 켜져있을때
        while cap.isOpened():

            # 캠 읽기 성공여부 success와 읽은 이미지를 image에 저장
            success, image = cap.read()

            # 캠 읽기 실패시 continue
            if not success:
                continue

            # 이미지 값 좌우반전 ( 캠 켰을때 반전된 이미지 보완 )
            # 이미지 값 순서를 BGR -> RGB로 변환
            # 이미지 순서가 RGB여야 Mediapipe 사용가능
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

            # Image에서 손을 추적하고 결과를 result에 저장
            result = hands.process(image)

            # 이미지 값 순서를 RGB에서 BGR로 다시 바꿈(mediaPipe에서는 BGR순서만 인식)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

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
                if (hand_landmarks.landmark[4].y < hand_landmarks.landmark[3].y):
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

                list_finger = [finger_1, finger_2, finger_3, finger_4, finger_5]
                fingernum = 0
                for i in list_finger:
                    if i is True:
                        fingernum = fingernum + 1

                if (fingernum == 5):
                    gesture_text = '5번'


                elif (fingernum == 4):
                    gesture_text = '4번'

                elif (fingernum == 3):
                    gesture_text = '3번'

                elif (fingernum == 2):
                    gesture_text = '2번'

                elif (fingernum == 1):
                    gesture_text = '1번'



                # 모두 아닐시 모르겠다는 텍스트
                else:
                    gesture_text = 'Mo Ru Get Saw Yo'

                # 캠 화면에 손가락을 그림
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # 캠화면에 텍스트를 작성
            cv2.putText(image, text='Hand shape : {}'.format(gesture_text)
                        , org=(10, 30), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=1, color=(0, 0, 255), thickness=2)

            # 캠 화면 ( 이미지 )을 화면에 띄움
            cv2.imshow('image', image)

            # 3번입력시 종료
            if gesture_text=='3번':
                break

            if cv2.waitKey(1) == ord('q'):
                break

    # 캠 종료
    cap.release()
    cv2.destroyAllWindows()

def change_label_image():
    global current_image_index

    # 이미지 파일 경로의 리스트 (자신의 이미지 경로로 바꾸세요)
    image_paths = [".\\combine\\face2.jpg",".\\combine\\face3.jpg",
                   ".\\combine\\face4.jpg",".\\combine\\face5.jpg",
                   ".\\combine\\face6.jpg",".\\combine\\face7.jpg",
                   ".\\combine\\face8.jpg",".\\combine\\face9.jpg",
                   ".\\combine\\face10.jpg"]

    # Change the index to the next image
    current_image_index = (current_image_index + 1) % len(image_paths)

    # Load the new image
    new_image_path = image_paths[current_image_index]
    new_image = Image.open(new_image_path)
    new_tk_image = ImageTk.PhotoImage(new_image)

    # Update the label image
    w.config(image=new_tk_image)
    w.image = new_tk_image

    new_label1_paths=['1번 아이브','1번 nct','1번 nct127 ','1번 블랙핑크','1번 nct dream','1번 아이브','1번 몬스타엑스','1번 씨스타','1번 시크릿']
    new_label1.config(text=new_label1_paths[current_image_index])

    new_label2_paths = ['2번 블랙핑크', '2번  nct127 ', '2번 블랙핑크', '2번 nct127 ','2번 씨스타','2번 레드벨벳','2번 아이브','2번 레드벨벳','2번 에프엑스']
    new_label2.config(text=new_label2_paths[current_image_index])

    new_label3_paths = ['3번 BTS', '3번 BlackPink', '3번Ive ', '3번  세븐틴 ','3번 Twice','3번 르세라핌','3번 에스파','3번엑소','3번 소녀시대']
    new_label3.config(text=new_label3_paths[current_image_index])

    new_label4_paths = ['4번  nct127 ', '4번 아이브', '4번  nct ', '4번 아이즈원','4번 키스오프라이프','4번 ses','4번 트와이스','4번 아이즈원','4번 아이즈원']
    new_label4.config(text=new_label4_paths[current_image_index])

    new_label5_paths = ['5번 펑크펑크', '5번 소녀시대', '5번 소년시대', '5번  nct u ' ,'5번  nct ', '5번  nct127 ', '5번  키스오프라이프 ', '5번  nct 도재정 ', '5번  nct u ']
    new_label5.config(text=new_label5_paths[current_image_index])




font1=tkinter.font.Font(family="많은 고딕",size=20)
label=Label(window,text="IDOL-FACE-Game",width=40,height=3,font=font1)
label['fg']="black"
label['bg']="green"

label.pack()



#이미지를 넣어야 함
image_path = ".\\combine\\face1.jpg"
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

new_label3 = Label(window, text='3번 뉴진스',font=font3)
new_label3['fg'] = "black"
new_label3['bg'] = "green"
new_label3.pack()

new_label4 = Label(window, text='4번 있지',font=font3)
new_label4['fg'] = "black"
new_label4['bg'] = "green"
new_label4.pack()

new_label5 = Label(window, text='5번 트와이스',font=font3)
new_label5['fg'] = "black"
new_label5['bg'] = "green"
new_label5.pack()

new_answer_button = Button(window, text='정답입력',command=fingerfuction, font=font3)
new_answer_button ['fg'] = "black"
new_answer_button ['bg'] = "yellow"
new_answer_button .pack()




new_problem2=Button(window,text='다음문제',command=change_label_image,font=font3)

new_problem2['fg'] = "black"
new_problem2['bg'] = "yellow"

new_problem2.pack()



window.mainloop()
