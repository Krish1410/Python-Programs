from tkinter import *

if __name__ == "__main__":
    root=Tk()
    root.geometry("1100x600")
    # Create a label for Entry Wegit
    entry=Label(root,bg="white")
    entry.pack(side=TOP)
    Name=Entry(entry,bg="black")
    Name.pack(side=TOP)
    root.mainloop()