from tkinter import *
from tkinter import ttk
from tkinter import font,colorchooser
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename ,asksaveasfilename
import os

# Create a new file
def newfile():
    global file
    root.title("Untitled -- Editar")
    file = None
    TextArea.delete(1.0,END)
# Open a new file 
def openfile():
    global file 
    file = askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(file, 'r') as fr:
            TextArea.delete(1.0, END)
            TextArea.insert(1.0, fr.read())
    except FileNotFoundError:
        return 
    except:
        return 
    root.title(os.path.basename(file))
# save a file 
def savefile():
    global file
    if file == None:
        file=asksaveasfilename(initialfile="Nopad.txt",defaultextension=".txt",filetypes=[("All Fles","*.*"),("Text Documents",".txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+" - Editar")
            print("File Saved")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
# Exit app
def Exitfile():
    root.destroy()
    # print(root.destroy())
# copy text 
def Copy():
    TextArea.event_generate(("<Control c>"))
# cut text
def Cut():
    TextArea.event_generate(("<Control x>"))
# past text
def Past():
    TextArea.event_generate(("<Control v>"))
# about our softwear
def about():
    showinfo("Notepad","Editar By Malaviya Krish With Help Herry")
# BackEND For Notpad
currant_font_family="Arial"
currant_font_size=12
# change_font family by order
def change_font(root):
    global currant_font_family
    currant_font_family=font_family.get()
    TextArea.configure(font=(currant_font_family,currant_font_size))
# change_font size by order
def change_size(root):
    global currant_font_size
    currant_font_size=size_font.get()
    TextArea.configure(font=(currant_font_family,currant_font_size))
# change font color
def change_font_color():
    color_var=colorchooser.askcolor()
    TextArea.configure(fg=color_var[1])
# chang font to italic
def font_italic():
    text=font.Font(font=TextArea['font'])
    if text.actual()['slant']=='roman':
        TextArea.configure(font=(currant_font_family,currant_font_size,'italic'))
    else:
        TextArea.configure(font=(currant_font_family,currant_font_size,'normal'))
# chang font to bold
def font_Bold():
    text=font.Font(font=TextArea['font'])
    if text.actual()['weight']=='normal':
        TextArea.configure(font=(currant_font_family,currant_font_size,'bold'))
    if text.actual()['weight']=='bold':
        TextArea.configure(font=(currant_font_family,currant_font_size,'normal'))
# create under line in font 
def font_underline():
    text=font.Font(font=TextArea['font'])
    if text.actual()['underline']==0:
        TextArea.configure(font=(currant_font_family,currant_font_size,1))
    else:
        TextArea.configure(font=(currant_font_family,currant_font_size,'normal'))
# chane text alignment to left 
def align_left():
    text_content = TextArea.get(1.0, 'end')
    TextArea.tag_config('left', justify=LEFT)
    TextArea.delete(1.0, END)
    TextArea.insert(INSERT, text_content, 'left')
# chane text alignment to right
def align_Right():
    text_content = TextArea.get(1.0, 'end')
    TextArea.tag_config('Right', justify=RIGHT)
    TextArea.delete(1.0, END)
    TextArea.insert(INSERT, text_content, 'Right')
# chane text alignment to center
def align_center():
    text_content = TextArea.get(1.0, 'end')
    TextArea.tag_config('center', justify=CENTER)
    TextArea.delete(1.0, END)
    TextArea.insert(INSERT, text_content, 'center')
text_changed = False 
# show CHAR and WORD in dstatuse bar 
def changed(event=None):
    global text_changed
    if TextArea.edit_modified():
        text_changed = True 
        words = len(TextArea.get(1.0, 'end-1c').split())
        characters = len(TextArea.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    TextArea.edit_modified(False)
if __name__ == "__main__":
    root=Tk()
    root.title("Untitled-Editer")
    root.wm_iconbitmap("C:\\Users\\Dell\\Pictures\\python.ico")
    root.geometry("700x500")
    # Text Aria
    file = None

    # Create MEnu Bar 
    MenuBAr=Menu(root)
    FilleMenu= Menu(MenuBAr,tearoff=0)
    EditMenu=Menu(MenuBAr,tearoff=0)
    view=Menu(MenuBAr,tearoff=0)
    helpmenu=Menu(MenuBAr,tearoff=0)
    color_theam=Menu(MenuBAr,tearoff=0)


    # Open New File 
    FilleMenu.add_command(label="New",command=newfile )
    #  opeen writed file 
    FilleMenu.add_command(label="Open",command=openfile)
    #  save the CURRENT file 
    FilleMenu.add_command(label="Save",command=savefile)
    FilleMenu.add_separator()
    FilleMenu.add_command(label="Exit",command=Exitfile)
    # file menu is Finish

    # Edit menu Is start 
    EditMenu.add_command(label="Copy", command=Copy)
    EditMenu.add_command(label="Cut", command=Cut)
    EditMenu.add_command(label="Paste", command=Past)
    # VIEW Menu 
    view.add_checkbutton(label="ToolBar")
    view.add_checkbutton(label="Statuse Bar")

    # color them
    color_dict = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
    }
    theam_choice=StringVar()
    for i in color_dict:
        color_theam.add_radiobutton(label = i, variable=theam_choice, compound=LEFT)


    # Help Menu
    helpmenu.add_command(label="About Notepad",command=about)

    # Pake all Menu 

    MenuBAr.add_cascade(label="File",menu = FilleMenu,)
    MenuBAr.add_cascade(label="Edit",menu=EditMenu)
    MenuBAr.add_cascade(label="View",menu=view)
    MenuBAr.add_cascade(label="Theam",menu=color_theam)
    MenuBAr.add_cascade(label="Help",menu=helpmenu)

    #Create Lable For Tool bar Like a Font Type ANd FOnt SIze And many more
    ToolBar=Label(root)
    ToolBar.pack(side=TOP,fill=X)

    font_tupal=font.families()
    font_family=StringVar()
    font_box=ttk.Combobox(ToolBar,width=30,textvariable=font_family,state="readonly")
    font_box["values"]=font_tupal
    font_box.current(font_tupal.index("Arial"))
    font_box.grid(row=0,column=0,padx=5)

    # FOnt Size
    size_font=IntVar()
    font_size=ttk.Combobox(ToolBar,width=10,textvariable=size_font)
    font_size['values']=tuple(range(2,1000,2))
    font_size.current(12)
    font_size.grid(row=0,column=1,padx=5)

    
    # Bold 
    icon_bold=PhotoImage(file="./img/bold.png")
    bold=ttk.Button(ToolBar,image=icon_bold,command=font_Bold)
    bold.grid(row=0,column=2,padx=3)
    # Italic 
    icon_Italic=PhotoImage(file="./img/italic.png")
    Italic=ttk.Button(ToolBar,image=icon_Italic,command=font_italic)
    Italic.grid(row=0,column=3,padx=3)
    # Underline 
    icon_Underline=PhotoImage(file="./img/underline.png")
    Underline=ttk.Button(ToolBar,image=icon_Underline,command=font_underline)
    Underline.grid(row=0,column=4,padx=3)
    # align_left 
    icon_align_left=PhotoImage(file="./img/align_left.png")
    align_left=ttk.Button(ToolBar,image=icon_align_left,command=align_left)
    align_left.grid(row=0,column=5,padx=3)
    # align_center 
    icon_align_center=PhotoImage(file="./img/align_center.png")
    align_center=ttk.Button(ToolBar,image=icon_align_center,command=align_center)
    align_center.grid(row=0,column=6,padx=3)
    # align_Right
    icon_align_Roghr=PhotoImage(file="./img/align_Roghr.png")
    align_Right=ttk.Button(ToolBar,image=icon_align_Roghr,command=align_Right)
    align_Right.grid(row=0,column=7,padx=3)
    # font_color
    # icon_font_color=PhotoImage(file="./img/font_color.png")
    font_color=ttk.Button(ToolBar,command=change_font_color)
    font_color.grid(row=0,column=8,padx=0)
    
    # _________________Statuse Bar______________________
    status_bar=Label(root)
    status_bar.pack(side=BOTTOM,fill=X)
    
    #text areea
    TextArea= Text(root,font="Arial 12")
    TextArea.config(wrap='word',relief=FLAT)

    # Scorrbar for text area 
    scrool=Scrollbar(root)
    TextArea.focus_set()
    scrool.pack(side=RIGHT,fill =Y)
    TextArea.pack(expand=True,fill=BOTH)
    scrool.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scrool.set)

    font_size.bind("<<ComboboxSelected>>",change_size)
    font_box.bind("<<ComboboxSelected>>",change_font)
    TextArea.bind('<<Modified>>', changed)


    root.config(menu = MenuBAr)
    root.mainloop()