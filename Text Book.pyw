from tkinter import *
from tkinter import filedialog,simpledialog
from tkinter.scrolledtext import ScrolledText
from tkinter  import messagebox
from tkinter.ttk import *
import re
from tkinter.colorchooser import askcolor
from tkinter.font import Font, families
import time
import sys

root = Tk()
root.title("Text Book")
root.geometry("300x250+300+300")
root.minsize(width=400, height=400)

textPad = ScrolledText(root, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
textPad.pack(fill=Y, expand=1)
textPad.focus_set()

#Defining Functions 
#textpad New_file()
def newFile():
    global filename
    root.title("Text book")
#textpad save_file
def saveFile():
    f = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if f!= None:
        data = textPad.get('1.0',END)
    try:
        f.write(data)
    except:
        messagebox.showerror(title="Oops!!",message="Unable to save file!")
#textpad saveAs_file()
def saveAs():
    f = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    t = textPad.get(0.0,END)
    try:
        f.write(t.rstrip())
    except:
        messagebox.showerror(title="Oops!!",message="Unable to save file!")
#textpad open_file()
def openFile():
    f = filedialog.askopenfile(parent=root,mode='r')
    t = f.read()
    textPad.delete(0.0,END)
    textPad.insert(0.0,t)
#textpad about_command()   
def about_command():
    label = messagebox.showinfo("About","Created By Syeda Ayesha Khateeb \n You can contact Us through\nEMAIL : s.aye.khateeb@gmail.com")
#textpad find_pattern()
def find_pattern():
    textPad.tag_remove("Found",'1.0',END)
    find = simpledialog.askstring("Find....","Enter text:")
    if find:
        idx = '1.0'
    while 1:
        idx = textPad.search(find,idx,nocase=1,stopindex=END)
        if not idx:
            break
        lastidx = '%s+%dc' %(idx,len(find))
        textPad.tag_add('Found',idx,lastidx)
        idx = lastidx
    textPad.tag_config('Found',foreground='white',background='black')

'''
    t = textPad.get('1.0',END)
    occurance = t.upper().count(find.upper())
        
    if occurance > 0:
        label = messagebox.showinfo("Find",find+" has multiple occurances "+str(occurance))
    else:
        label = messagebox.showinfo("Find","No results")
    '''
#textpad exit_command()
def exit_command():
    if messagebox.askyesno("Exit","Are you sure you want to exit?"):
        root.destroy()
#textpad. edit_copy()
def copy(): # works only if text is selected
    try:
        textPad.clipboard_clear()
        text = textPad.get("sel.first", "sel.last")
        textPad.clipboard_append(text)
    except:
        pass
    # textPad.edit_copy()
    
# textPad.edit_paste()
def paste():# works only if text is copied or cut 
    try:
        text = textPad.selection_get(selection='CLIPBOARD')
        textPad.insert('insert', text)
    except:
        pass
   
# textPad.edit_cut()
def cut():# works only if text is selected
    try:
        copy()
        textPad.delete("sel.first", "sel.last")
    except:
        pass
    
# textPad.edit_undo()
def undo():  
    textPad.edit_undo()

# textPad.edit_redo()
def redo():     
    textPad.edit_redo()
    
# textPad.edit_clear_All()    
def clear_All():
    textPad.delete( 1.0, END)
    
#Function for background change
def changeBg():
    (triple, hexstr)= askcolor()
    if hexstr:
        textPad.config(bg=hexstr)

#Function for text color change
def changeFg():
    (triple, hexstr) = askcolor()
    if hexstr:
        textPad.config(fg=hexstr)

#Function For BOLD
def bold(*args):  # Works only if text is selected
    try:
        current_tags = textPad.tag_names("sel.first")
        if "bold" in current_tags:
            textPad.tag_remove("bold", "sel.first", "sel.last")
        else:
            textPad.tag_add("bold", "sel.first", "sel.last")
            bold_font = Font(textPad, textPad.cget("font"))
            bold_font.configure(weight="bold")
            textPad.tag_configure("bold", font=bold_font)
    except:
        pass

#Function For Italic
def italic( *args):  # Works only if text is selected
    try:
        current_tags = textPad.tag_names("sel.first")
        if "italic" in current_tags:
            textPad.tag_remove("italic", "sel.first", "sel.last")
        else:
            textPad.tag_add("italic", "sel.first", "sel.last")
            italic_font = Font(textPad, textPad.cget("font"))
            italic_font.configure(slant="italic")
            textPad.tag_configure("italic", font=italic_font)
    except:
        pass

#function for underline
def underline( *args):  # Works only if text is selected
    try:
        current_tags = textPad.tag_names("sel.first")
        if "underline" in current_tags:
            textPad.tag_remove("underline", "sel.first", "sel.last")
        else:
            textPad.tag_add("underline", "sel.first", "sel.last")
            underline_font = Font(textPad, textPad.cget("font"))
            underline_font.configure(underline=1)
            textPad.tag_configure("underline", font=underline_font)
    except:
        pass

#function for Overstrike
def overstrike( *args):  # Works only if text is selected
    try:
        current_tags = textPad.tag_names("sel.first")
        if "overstrike" in current_tags:
            textPad.tag_remove("overstrike", "sel.first", "sel.last")
        else:
            textPad.tag_add("overstrike", "sel.first", "sel.last")
            overstrike_font = Font(textPad, textPad.cget("font"))
            overstrike_font.configure(overstrike=1)
            textPad.tag_configure("overstrike", font=overstrike_font)
    except:
        pass

#function for adding date 
def addDate():
    full_date = time.localtime()
    day = str(full_date.tm_mday)
    month = str(full_date.tm_mon)
    year = str(full_date.tm_year)
    date = day + '/' + month + '/' + year
    textPad.insert(INSERT, date, "a")



#creating Main menu

menuM = Menu(root, )
root.configure(menu=menuM)

#adding file menu and its commands in Main
fileM = Menu(menuM, tearoff=False)
menuM.add_cascade(label='File',menu=fileM)
fileM.add_command(label='New',command=newFile)
fileM.add_command(label='Open',command=openFile)
fileM.add_command(label='Save',command=saveFile)
fileM.add_command(label='Save As...',command=saveAs)
fileM.add_separator()
fileM.add_command(label='Exit',command=exit_command)

#adding edit menu and its options in Main
editM = Menu(menuM, tearoff=False)
menuM.add_cascade(label='Edit',menu=editM)
editM.add_command(label='Undo',command=undo, accelerator="Ctrl+Z")
editM.add_command(label='Redo',command=redo, accelerator="Ctrl+Y")
editM.add_command(label='Cut',command=cut, accelerator="Ctrl+X")
editM.add_command(label='Copy',command=copy, accelerator="Ctrl+C")
editM.add_command(label='Paste',command=paste, accelerator="Ctrl+V")
editM.add_separator()
editM.add_command(label='Clear All',command=clear_All, )

#Declaring font family and size
fontoptions = families(root)
font = Font(family="Arial", size=10)
textPad.configure(font=font)

#Adding format menu and its options in Main
formatMenu = Menu(menuM, tearoff=False)

#creating two sub menus for changes Font style and size 
fsubmenu = Menu(formatMenu, tearoff=0)
ssubmenu = Menu(formatMenu, tearoff=0)

#creating command for change font style 
for option in fontoptions:
    fsubmenu.add_command(label=option, command=lambda option=option: font.configure(family=option))

#creating command for change font size    
for value in range(1, 31):
    ssubmenu.add_command(label=str(value), command=lambda value=value: font.configure(size=value))

#adding format menu and its options in Main
menuM.add_cascade(label="Format", menu=formatMenu)
formatMenu.add_command(label="Change Background", command=changeBg)
formatMenu.add_command(label="Change Font Color", command=changeFg)
formatMenu.add_cascade(label="Font", underline=0, menu=fsubmenu)
formatMenu.add_cascade(label="Size", underline=0, menu=ssubmenu)
formatMenu.add_command(label="Bold", command=bold, accelerator="Ctrl+B")
formatMenu.add_command(label="Italic", command=italic, accelerator="Ctrl+I")
formatMenu.add_command(label="Underline", command=underline, accelerator="Ctrl+U")
formatMenu.add_command(label="Overstrike", command=overstrike, accelerator="Ctrl+T")
formatMenu.add_separator()
formatMenu.add_command(label="Add Date", command=addDate)

root.bind_all("<Control-b>", bold)
root.bind_all("<Control-i>", italic)
root.bind_all("<Control-u>", underline)
root.bind_all("<Control-T>", overstrike)

#adding find menu in Main
findM = Menu(menuM, tearoff=False)
menuM.add_cascade(label='Find',menu=findM)
findM.add_command(label='Find',command = find_pattern)

#adding about menu in Main
aboutM = Menu(menuM, tearoff=False)
menuM.add_cascade(label='About',menu=aboutM)
aboutM.add_command(label='About',command = about_command)


textPad.pack()

root.mainloop()



