
import pygame
import pygame.locals  
import pylint
import random
import time
import os
import squr
import text_in_game as TIG
from pygame.mixer import stop
# import imutils
# import pyttsx3
# engine=pyttsx3.init('sapi5')
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)

# def speak(audio):
#     '''
#     this func for speak by computer
#     '''
#     engine.say(audio)
#     engine.runAndWait()



pygame.mixer.init()

#______________________________ variables__________________________________________#
white = (255,255, 255) 
black = (0,0,0)
red=(255,0,0)
green=(0,255,0)
ret=(77, 78, 80)
Screen_hight=500
Screen_widgh=600
pygame.init()
window=pygame.display.set_mode((Screen_widgh,Screen_hight))
pygame.display.set_caption("Game")

clock=pygame.time.Clock()
if not os.path.exists("K:\python\_H_SCORE.txt"):
    with open("K:\python\_H_SCORE.txt", "w") as f:
        f.write(str(0))
with open("K:\python\_H_SCORE.txt", "r") as f:
    _H_SCORE=f.read()

def stop():
    stop=True
    while stop:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    print(stop)
                    stop=False
                if event.key==pygame.K_h:
                    _help()
                
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        # window.fill(white)
        # text_any("Pausd",white, 109,10)
        pygame.display.update()
        TIG.Text(window,'ALGERIN',40,"Stoped",red,240,100)
        # _help("Stoped")
        clock.tick(30)
        pygame.display.update()
def _help(Stoped,):
    # global stop
    help=True
    while help:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    help=False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        window.fill(white)
        TIG.Text(window,"Algerian",30,"Welcome To Krish community",black,70,5)
        TIG.Text(window,"Algerian",30,"_________________________________________",black,0,10)
        TIG.Text(window,"Agency FB",35,"Help Center",red,240,45)
        TIG.Text(window,"Algerian",35,"_______",black,240,50)

        TIG.Text(window,"Comic Sans MS",25,"*"+"Press 'space' bar to pause and start The game ",black,23,95)
        TIG.Text(window,"Comic Sans MS",25,"*"+"Press 'q' to QUIT The game ",black,23,140)
        TIG.Text(window,"Comic Sans MS",20,"*"+"Press 'Right arrow' to change snak direcshion to right ",black,25,185)
        TIG.Text(window,"Comic Sans MS",20,"*"+"Press 'Left arrow' to change snak direcshion to left ",black,25,220)
        TIG.Text(window,"Comic Sans MS",20,"*"+"Press 'Up arrow' to change snak direcshion to Up ",black,25,250)
        TIG.Text(window,"Comic Sans MS",20,"*"+"Press 'Down arrow' to change snak direcshion to Down ",black,25,280)
        TIG.Text(window,'Algerian',50,Stoped,red,220,450)
        pygame.display.update()



    
    pygame.display.update()
font=pygame.font.SysFont(None,45)
def text_any(text,color,x,y):
    var=font.render(text,True,color)
    window.blit(var,[x,y])

def plot_snake(window,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.circle(window , white ,(x,y),snake_size,snake_size)


def welcome():
    exit_game=False

    welcome=pygame.image.load("K:\my coding\singup.jpg")
    window.fill(black)
    # window.blit(welcome,[0,0])
    welcome1=pygame.image.load("K:\my coding\snake.png")
    window.blit(welcome1,[100,00])

    pygame.display.update()
    text_any(" WELCOME THE MY GAME",[200,200,200],100,200)

    TIG.Text(window,"Stencil",30,"Prees" ,white,50,250)
    pygame.display.update()

    TIG.Text(window,"Showcard Gothic",30,"'SPACE'",[240,240,240],150,250)
    pygame.display.update()

    TIG.Text(window,"Stencil",30,"Bar TO Start Game",white,270,250)
    pygame.display.update()


    TIG.Text(window,"Segoe Script",35,"Your Hightscor : "+ str(_H_SCORE),[0,255,255],90,300)
    pygame.display.update()

    squr.speak("welcome to our game")
    squr.speak("Yor hightscore is "+str(_H_SCORE))

    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game=True
                quit()
            if event.type== pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
                if event.key==pygame.K_h:
                    _help("")
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                else:
                    return
    clock.tick(50)

def gameloop():
    back=pygame.image.load("K:\my coding\snkback.jpg")
    over=pygame.image.load("K:\my coding\main1.jpg")
    



    exit_game=False
    game_over=False
    snake_x=random.randint(11,580)
    snake_y=90
    snake_size=10

    valosity_x=0
    valosity_y=0
    initvalosity=6

    fod_x=random.randint(100,580)
    fod_y=random.randint(100,200)
    fod_size=10
    scoor=0

    snake_lenth=1
    snake_list=[]

    fps=20   
    with open("K:\python\_H_SCORE.txt", "r") as f:
        _H_SCORE=f.read()
    # color
    while not exit_game:
        window.fill(white)
        window.blit(back,[0,0])
        if game_over:
            # time.sleep(1)
            # speak("game over")
            with open("K:\python\_H_SCORE.txt", "w") as f:
                f.write(str(_H_SCORE))
            window.fill(black)
            window.blit(over,[0,0])
            font=pygame.font.SysFont("Segoe Script",30)
            pygame.display.update()
            snake_lenth=0
            snake_size=0
            pygame.display.update()
            var=font.render("SCORE : "+ str(scoor)+"  HIGHTSCORE:" + str(_H_SCORE),True,white)
            window.blit(var,[30,30])
            pygame.display.update()
            text_any("                   GAME OVER!" ,white, 30,200)
            text_any("   PREES 'ENTER' TO CONTINEU",green,20,300 )
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        valosity_x= initvalosity
                        valosity_y=0
                    if event.key == pygame.K_LEFT:
                        valosity_x=-initvalosity
                        valosity_y=0
                    if event.key == pygame.K_UP:
                        valosity_x=0
                        valosity_y=-initvalosity
                    if event.key == pygame.K_DOWN:
                        valosity_x=0
                        valosity_y=initvalosity
                    if event.key==pygame.K_PAGEUP:
                        if initvalosity>=0:
                            initvalosity+=1
                    if event.key==pygame.K_PAGEDOWN:
                        if initvalosity>0:
                            initvalosity-=1
                        else:
                            TIG.Text(window,"Agenesy FB",40,"You Speed is alredy 0",white,30,100)
                        # _help("")
                    if event.key==pygame.K_SPACE:
                        stop()
                    if event.key==pygame.K_h:
                        _help("")
                    if event.key==pygame.K_q:
                        pygame.quit()
                        quit()
            snake_x=snake_x + valosity_x
            snake_y=snake_y + valosity_y
            if abs(snake_x - fod_x) < 15 and abs(snake_y - fod_y)<15:
                pygame.mixer.music.load("K:\my coding\s_beep.mp3")
                pygame.mixer.music.play()
                scoor += 1
                initvalosity += int(.5)
                fod_x=random.randint(50,580)
                fod_y=random.randint(50,500)
                snake_lenth +=1.5
                game_over=True
            pygame.draw.rect(window,ret,[0,0,600,50])
            pygame.display.update()
            text_any("SCORE :"+ str(scoor) + "    HIGHTSCORE:" + str(_H_SCORE)+"   Speed:"+str(initvalosity) ,white,5,10)
            if int(_H_SCORE) <= scoor:
                _H_SCORE=scoor  
                TIG.Text(window,"A rial",30,"You Breck The HightScore",[255,255,255],150,450)
            pygame.display.update()

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_lenth:
                del snake_list[0]
            
            if head in snake_list[:-1]:
                pygame.mixer.music.load("K:\my coding\gameover.mp3")
                pygame.mixer.music.play()
                game_over=True
            if snake_x<=0 or snake_x>=Screen_widgh or snake_y<=30 or snake_y>=Screen_hight:
                pygame.mixer.music.load("K:\my coding\gameover.mp3")
                pygame.mixer.music.play()
                game_over=True
        plot_snake(window, white,snake_list,snake_size)
        pygame.draw.circle(window,black,(snake_x,snake_y),9,9)
        pygame.display.update()
        pygame.draw.circle(window , black ,(fod_x,fod_y),fod_size)
        pygame.display.update()
        clock.tick(fps)
welcome()
pygame.quit()
quit()