from tkinter import *

def click(event):
    global Value
    Text=event.widget.cget("text")
    if Text=="C":
        Value.set("")
    elif Text=="E":
        root.destroy()
    elif Text=="x":
        Value.set(Value.get()+"*")
    elif Text=="=":
        if Value.get().isdigit():
            value=float(Value.get())
        else:
            value=eval(screen.get())
        Value.set(value)
        screen.update()
    else:
        Value.set(Value.get()+Text)

#=====Create Screen======#
root=Tk()
root.geometry("350x500+300+100")
root.resizable(False,False)
#=====Create Frame for Claculater================#
Main_Frame=Frame(root,bg="white")
Main_Frame.pack(ipadx=40,ipady=200)
#======Create Entry Widget===========#
Value=StringVar()
Value.set("")
screen=Entry(Main_Frame,textvar=Value,bg="white",fg="black",font=("lusida",20,"bold"),bd=1,width=340)
screen.pack(padx=20,pady=20,ipady=5)
#=========First row of line==========#
f1=Label(Main_Frame,bg="white")
b=Button(f1,text="9",bg="white",fg="#d77337",font=("lusida  20 bold"),bd=1)
b.pack(padx=10,pady=10,side=LEFT,ipadx=10)
b.bind("<Button-1>",click)
b=Button(f1,text="8",bg="white",fg="#d77337",font=("lusida  20 bold"),bd=1)
b.pack(padx=10,pady=10,side=LEFT,ipadx=10)
b.bind("<Button-1>",click)
b=Button(f1,text="7",bg="white",fg="#d77337",font=("lusida  20 bold"),bd=1)
b.pack(padx=10,pady=10,side=LEFT,ipadx=10)
b.bind("<Button-1>",click)
b=Button(f1,text="C",bg="white",fg="#000000",font=("lusida  20 bold"),bd=1)
b.pack(padx=10,pady=10,side=LEFT,ipadx=10)
b.bind("<Button-1>",click)
f1.pack()
#=========Second row of line==========#
f1=Label(Main_Frame,bg="white")
b=Button(f1,text="6",bg="white",fg="#d77337",font=("lusida  20 bold"),bd=1)
b.pack(padx=10,pady=10,side=LEFT,ipadx=10)
b.bind("<Button-1>",click)
b=Button(f1,text="5",bg="white",fg="#d77337",font=("lusida  20 bold"),bd=1)
b.pack(padx=10,pady=10,side=LEFT,ipadx=10)
b.bind("<Button-1>",click)
b=Button(f1,text="4",bg="white",fg="#d77337",font=("lusida  20 bold"),bd=1)
b.pack(padx=10,pady=10,side=LEFT,ipadx=10)
b.bind("<Button-1>",click)
b=Button(f1,text="/",bg="white",fg="#000000",font=("lusida  20 bold"),bd=1)
b.pack(padx=10,pady=10,side=LEFT,ipadx=15)
b.bind("<Button-1>",click)
f1.pack()
#=========Third row of line==========#
f1=Label(Main_Frame,bg="white")
b=Button(f1,text="3",bg="white",fg="#d77337",font=("lusida  20 bold"),bd=1)
b.pack(padx=10,pady=10,side=LEFT,ipadx=10)
b.bind("<Button-1>",click)
b=Button(f1,text="2",bg="white",fg="#d77337",font=("lusida  20 bold"),bd=1)
b.pack(padx=10,pady=10,side=LEFT,ipadx=10)
b.bind("<Button-1>",click)
b=Button(f1,text="1",bg="white",fg="#d77337",font=("lusida  20 bold"),bd=1)
b.pack(padx=10,pady=10,side=LEFT,ipadx=10)
b.bind("<Button-1>",click)
b=Button(f1,text="x",bg="white",fg="#000000",font=("lusida  20 bold"),bd=1)
b.pack(padx=10,pady=10,side=LEFT,ipadx=10)
b.bind("<Button-1>",click)
f1.pack()
#=========Four row of line==========#
f1=Label(Main_Frame,bg="white")
b=Button(f1,text="0",bg="white",fg="#d77337",font=("lusida  20 bold"),bd=1)
b.pack(padx=10,pady=10,side=LEFT,ipadx=10)
b.bind("<Button-1>",click)
b=Button(f1,text="00",bg="white",fg="#d77337",font=("lusida  20 bold"),bd=1)
b.pack(padx=10,pady=10,side=LEFT,ipadx=5)
b.bind("<Button-1>",click)
b=Button(f1,text="%",bg="white",fg="black",font=("lusida  20 bold"),bd=1)
b.pack(padx=10,pady=10,side=LEFT,ipadx=6)
b.bind("<Button-1>",click)
b=Button(f1,text="+",bg="white",fg="#000000",font=("lusida  20 bold"),bd=1)
b.pack(padx=10,pady=10,side=LEFT,ipadx=10)
b.bind("<Button-1>",click)
f1.pack()
#========="Exit"o Button line==========#
f1=Label(Main_Frame,bg="white")
b=Button(f1,text="E",bg="red",fg="white",font=("lusida  20 bold"),bd=1)
b.pack(padx=20,pady=10,side=LEFT,ipadx=10)
b.bind("<Button-1>",click)
f1.pack(side=LEFT)
#========="Equal" button line==========#
f1=Label(Main_Frame,bg="white")
b=Button(f1,text="=",bg="white",fg="black",font=("lusida  20 bold"),bd=1)
b.pack(padx=20,pady=10,side=LEFT,ipadx=10)
b.bind("<Button-1>",click)
f1.pack(side=RIGHT)


root.mainloop()