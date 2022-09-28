import pygame
from pygame.locals import *
import random
import math
import text_in_game as Text


windows_Hieght=500
windows_Widgh=700
Windows=pygame.display.set_mode((windows_Widgh,windows_Hieght))

clock=pygame.time.Clock()
FPS=40

die_=False
def die(e_x,e_y,b_x,b_y):
    global die_
    die=math.sqrt((math.pow(e_x-b_x,2))+(math.pow(e_y-b_y,2)))
    if die<=30:
        die_=True
    else:
        die_=False




# def MainGame():
# BACK-GROUND IMAGE
back=pygame.image.load("K:\my coding\contectus.jpg")
score=0
# variabal for ship
ship_x=random.randint(0,636)
ship_y=400
valosity_ship_x=0
initvalo=5
# IMAGES FOR PLAYER
def player(x,y):
    shipimg=pygame.image.load("K:\my coding\spaceship.png")
    Windows.blit(shipimg,[x,y])
 
# variabal for Enemy
Enemy_img=[]
Enemy_x=[]
Enemy_y=[]
valosity_Enemy_x=[]
valosity_Enemy_y=[]
num_enemy=4

for i in range(num_enemy):
    Enemy_img.append(pygame.image.load("K:\my coding\Enemy.png"))
    Enemy_x.append(random.randint(64,634))
    Enemy_y.append(random.randint(50,150))
    valosity_Enemy_x.append(5)
    valosity_Enemy_y.append(40)
# Enemy image
    def Enemy(x,y,i):
        Windows.blit(Enemy_img[i],[x,y])

# variabal for Bullet
Bullet_x=0
Bullet_y=400
valosity_Bullet_x=0
# Bullet_img=imutils.resize(Bullet_img,20,20,)
valosity_Bullet_y=10
Bullet_state=False
def Bullet(x,y):
    Bullet_img=pygame.image.load("K:\my coding\Bullet.png")
    global Bullet_state
    Bullet_state=True
    Windows.blit(Bullet_img,[x+24,y])
Exit_Game=False
gameover=False
while not Exit_Game:
        
    Windows.fill((255,255,0))
    Windows.blit(back,(0,0))
    if gameover:
        Text.Text(Windows,"ALGERIN",60,"game over",[0,0,0],100,100)

    for Event in pygame.event.get():
        if Event.type==QUIT:
            Exit_Game=True
        if Event.type==KEYDOWN:
            if Event.key==K_RIGHT:
                valosity_ship_x+=initvalo
            if Event.key==K_LEFT:
                valosity_ship_x-=initvalo
            
            if Event.key==K_SPACE:
                if Bullet_state==False:
                    Bullet_x=ship_x
                    Bullet(ship_x,Bullet_y)
        if Event.type==KEYUP:
            if Event.key==K_RIGHT or Event.key==K_LEFT:
                valosity_ship_x=0
        
    # borders for ship
    if ship_x<=0:
        ship_x=0
    elif ship_x>=636:
        ship_x=636
    # borders for Enemy
    for i in range(num_enemy):

        Enemy_x[i]+=valosity_Enemy_x[i]
        if Enemy_x[i]<=0:
            valosity_Enemy_x[i]=5
            Enemy_y[i]+=valosity_Enemy_y[i]
        elif Enemy_x[i]>=636:
            valosity_Enemy_x[i]=-5
            Enemy_y[i]+=valosity_Enemy_y[i]
        Enemy(Enemy_x[i],Enemy_y[i],i)
        

        die(Enemy_x[i],Enemy_y[i],Bullet_x,Bullet_y)
        if die_:
            Enemy_y[i]=-80
            score+=1
            # num_enemy+=1
            # TIG.Text(Windows,None,30,"Game over",[255,255,255],100,100)
            # Enemy_y=50
        if abs(Enemy_x[i]-ship_x)<0 or abs(Enemy_y[i]-ship_y)<0:
            gameover=True
    # Bullet Movment
    if Bullet_y<=0:
        Bullet_y=400
        Bullet_state=False
    if Bullet_state:
        Bullet_y-=valosity_Bullet_y
        Bullet(Bullet_x,Bullet_y)
        pygame.display.update()
    ship_x+=valosity_ship_x
    Text.Text(Windows,"Agency FB",40,"SCORE : "+str(score),[255,255,255],10,10)
    player(ship_x,ship_y)
    clock.tick(FPS)
    pygame.display.update()
pygame.quit()
quit()