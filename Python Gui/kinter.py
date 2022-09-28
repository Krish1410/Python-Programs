import tkinter 
import cv2
import imutils
import PIL.Image , PIL.ImageTk
from functools import partial

# import PIL
stream=cv2.VideoCapture("testtkinter.mp4")
flag=True
def play(speed):
    global flag
    # print(f"You clicked on play. Speed is {speed}")

    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=1000, height=600)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
    flag = not flag

def image(src,IMG_POSI_X,IMG_POSI_Y):
    frame = cv2.cvtColor(cv2.imread(src), cv2.COLOR_BGR2RGB)
    # frame = imutils.resize(frame, width=800, height=800)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(IMG_POSI_X,IMG_POSI_Y, image=frame, anchor=tkinter.NW)
    canvas.pack()

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=1000, height=200)
window.title("Krish First GUI")
# cv_img = cv2.cvtColor(cv2.imread("Myimg.png"), cv2.COLOR_BGR2RGB)
# photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
# image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()
# cv_img=imutils.resize(cv_img,width=600,height=400

buttan=tkinter.Button(window,text="first",width=40,height=1,fg="red",font="lucida 10 bold",command=partial(play,-20))
buttan.pack(padx=10,pady=10)
buttan=tkinter.Button(window,text="second",width=40,height=1,fg="red",font="lucida 10 bold",command=partial(play,-10))
buttan.pack(padx=10,pady=10)
buttan=tkinter.Button(window,text="third",width=40,height=1,fg="red",font="lucida 10 bold",command=partial(play,0))
buttan.pack(padx=10,pady=10)
buttan=tkinter.Button(window,text="for",width=40,height=1,fg="red",font="lucida 10 bold",command=partial(play,10))
buttan.pack(padx=10,pady=10)
buttan=tkinter.Button(window,text="five",width=40,height=1,fg="red",font="lucida 10 bold",command=partial(play,13))
buttan.pack(padx=10,pady=10)
buttan=tkinter.Button(window,text="six",width=40,height=1,fg="red",font="lucida 10 bold",command=partial(play,19))
buttan.pack(padx=10,pady=10)

window.mainloop()