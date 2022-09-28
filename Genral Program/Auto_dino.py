import pyautogui
import time
import PIL  

def hit(key):
    pyautogui.keyDown(key)


def isCollide(data):
    # bird
    for i in range(200,300):
        
        for j in range(300,500):
            if data[i,j] < 100:
                hit("down")
                return


    for i in range(200,300):

        for j in range(510,600):
            if data[i,j] < 100:
                hit("up")
                return

if __name__ == "__main__":
    print("2second")
    time.sleep(2)
    hit("up")
    while True:
        image=PIL.ImageGrab.grab().convert('L')
        data=image.load()

        isCollide(data)
    # bird
'''
    for i in range(200,300):
        for j in range(300,500):
            data[i,j]=100
    # cactes
    for i in range(200,300):
        for j in range(600,710):
            data[i,j]=86
    image.show()
'''