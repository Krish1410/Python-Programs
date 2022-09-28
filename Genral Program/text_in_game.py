import pygame
from pygame.locals import *

pygame.init()

def Text(surface,Font_type,font_size,text,color,x,y):
    font=pygame.font.SysFont(Font_type,font_size)
    var=font.render(text,True,color)
    surface.blit(var,[x,y])

if __name__ == "__main__":
    exit=False
    white = (255,255, 255) 
    window=pygame.display.set_mode([600,600])

    while not exit:
        for even in pygame.event.get():
            if even.type==QUIT:
                exit=True
        Text(window,"Agency FB",50,"I am a Krish",white,5,5)
        pygame.display.update()


    