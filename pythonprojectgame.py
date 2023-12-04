import pygame
import pygame as pg

#캐릭터 클래스 구현
class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y





pg.init()

#게임창 옵션 설정-창 설정
size=[900,600]

WHITE=(255,255,255)
BLACK=(0,0,0)

screen=pg.display.set_mode(size)

#배경색깔 설정
screen.fill(WHITE)

#블루마블 판 구현
pg.draw.rect(screen,BLACK,[100,50,100,100],1)
pg.draw.rect(screen,BLACK,[200,50,100,100],1)
pg.draw.rect(screen,BLACK,[300,50,100,100],1)
pg.draw.rect(screen,BLACK,[400,50,100,100],1)
pg.draw.rect(screen,BLACK,[500,50,100,100],1)
pg.draw.rect(screen,BLACK,[600,50,100,100],1)
pg.draw.rect(screen,BLACK,[700,50,100,100],1)

pg.draw.rect(screen,BLACK,[100,150,100,100],1)
pg.draw.rect(screen,BLACK,[700,150,100,100],1)

pg.draw.rect(screen,BLACK,[100,250,100,100],1)
pg.draw.rect(screen,BLACK,[700,250,100,100],1)

pg.draw.rect(screen,BLACK,[100,350,100,100],1)
pg.draw.rect(screen,BLACK,[700,350,100,100],1)

pg.draw.rect(screen,BLACK,[100,450,100,100],1)
pg.draw.rect(screen,BLACK,[200,450,100,100],1)
pg.draw.rect(screen,BLACK,[300,450,100,100],1)
pg.draw.rect(screen,BLACK,[400,450,100,100],1)
pg.draw.rect(screen,BLACK,[500,450,100,100],1)
pg.draw.rect(screen,BLACK,[600,450,100,100],1)
pg.draw.rect(screen,BLACK,[700,450,100,100],1)


#지구 사진 load
earth_image=pg.image.load("C:\\Users\\user\\Desktop\\project-python\\project-python\\지구.jpeg")

#지구 사진 크기 조절
earth_image=pg.transform.scale(earth_image,(200,200))

#지구 사진 위치 조절
earth_rect=earth_image.get_rect()
earth_rect.topleft=(350,200)




#게임 title
title="idol_bluemarble"
pg.display.set_caption(title)

#플레이어 생성
rabbit_image=pg.image.load("C:\\Users\\user\\Desktop\\project-python\\project-python\\rabbit1.jpg")
fox_image=pg.image.load("C:\\Users\\user\\Desktop\\project-python\\project-python\\fox.jpeg")



character1 = Character(600, 600, rabbit_image)
character2 = Character(650, 650, fox_image)

rabbit_image=pg.transform.scale(rabbit_image,(10,10))
fox_image=pg.transform.scale(fox_image,(10,10))
#게임

running=True
#무한 루프
while running:
    #게임 내에서 일어나는 event를 얻음
    for event in pg.event.get():

        answer1=True

        character1.moving(False)
        character1.moving(True)


        #게임을 종료하는 경우
        if event.type==pg.QUIT:
            running=False

    screen.blit(earth_image,earth_rect)

    pg.display.update()


pygame.quit()
