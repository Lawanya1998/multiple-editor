from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import Tk,Canvas,Menu,Text,NONE
import subprocess
import pyttsx3 #package to convert text to speech
engine = pyttsx3.init() #one time initialization
engine.setProperty('rate',150)# Speed percent (can go over 100)
engine.setProperty('volume',0.9)# Volume 0-1
engine.say("Multiple Language Editor Using Python")
engine.say("One stop for all your need")
engine.say("Here We go")
engine.runAndWait()
engine.stop()
def showContact():
    window = Tk()
    window.geometry("600x600".format((sw - 600) // 2, (sh - 600) // 2))
    window.attributes("-topmost", True, "-toolwindow", True)
    window.resizable(0, 0)
    
class Fileinfo:
    fname=""
#different functions
def newprg():
    tf.delete(1.0,END)
    Fileinfo.fname=""
    window.title("Multiple Language Editor (WOW!)")
def saveAsprg():
    try:
        fn=filedialog.asksaveasfilename(initialdir = "C:\jp",
                                        filetype = (("All Files","*.*"),
                                                    ("Java Files","*.java"),
                                                    ("C Files","*.c"),
                                                    ("CPP Files","*.cpp"),
                                                    ("Python Files","*.py"),
                                                    ("C/CPP Header Files","*.h"))
                                        )
        if fn!=None and str(fn).strip()!="":
            file = open(fn,"w")
            file.write(tf.get(1.0,END))
            file.close()
            Fileinfo.fname = fn
            window.title("Multiple Language Editor (WOW!) ("+ fn +")")
    except Exception as ex:
        messagebox.showerror(title="Error",message=ex)
def saveprg():
    try:
        file = open(Fileinfo.fname,"w")
        file.write(tf.get(1.0,END))
        file.close()
    except Exception as ex:
        messagebox.showerror(title="Error",message=ex)
def openprg():
    try:
        fn = filedialog.askopenfilename(initialdir="C:\jp",
                                                  filetype=(("All Files", "*.*"),
                                                            ("Java Files", "*.java"),
                                                            ("C Files", "*.c"),
                                                            ("CPP Files", "*.cpp"),
                                                            ("Python Files", "*.py"),
                                                            ("C/CPP Header Files", "*.h"))
                                                  )
        if fn != None and str(fn).strip() != "":
            file = open(fn, "r")
            tf.delete(1.0, END)
            tf.insert(1.0,file.read())
            file.close()
            Fileinfo.fname = fn
            window.title("Multiple Language Editor (WOW!) (" + fn + ")")
    except Exception as ex:
            messagebox.showerror(title="Error", message=ex)
def newOperation ():
    if str(tf.get(1.0,END)).strip()!="":
        res= messagebox.askyesno(title="Confirm",message = "Do you want to save")
        if res:
            if Fileinfo.fname == None or Fileinfo.fname.strip() == "":
                saveAsprg()
            else:
                saveprg()
    elif Fileinfo.fname!=None and Fileinfo.fname.strip()!="":
        res=messagebox.askyesno(title="Confirm",message="Do you want to save")
        if res:
            saveprg()
    newprg()
def saveOperation():
    if Fileinfo.fname == None or Fileinfo.fname.strip() == "":
        saveAsprg()
    else:
        saveprg()
def saveAsOperation():
        saveAsprg()
def openOperation():
    if str(tf.get(1.0,END)).strip()!="":
        res= messagebox.askyesno(title="Confirm",Message = "Do You Want To Save")
        if res:
            if Fileinfo.fname == None or Fileinfo.fname.strip() == "":
                saveAsprg()
            else:
                saveprg()
    elif Fileinfo.fname!=None and Fileinfo.fname.strip()!="":
        res=messagebox.askyesno(title="Confirm",message="Do you want to save")
        if res:
            saveprg()
    openprg()
def exitprogram():
    res = messagebox.askyesno(title="confirmation",message="Do You Really want To Exit")
    if res:
          window.quit()
def changeFG():
    col = colorchooser.askcolor()
    if col[1]!=None:
        tf.configure(fg=col[1])
def changeBG():
    col = colorchooser.askcolor()
    if col[1]!=None:
        tf.configure(bg=col[1])
def cutOperator():
    tf.clipboard_clear()
    tf.clipboard_append(tf.selection_get())
    tf.delete(SEL_FIRST,SEL_LAST)
def copyOperator():
    tf.clipboard_clear()
    tf.clipboard_append(tf.selection_get())
def pasteOperator():
    tf.insert(INSERT,tf.clipboard_get())
def selectAllOpertaion():
    tf.tag_add(SEL,1.0,END)
def aboutusOperation():
   # win = Tk()
    #win.title("About Us")
    #win.geometry("400x400")
    #win.attributes("-topmost",True,"-toolwindow",True)
    #win.resizable(False,False)
    #win.mainloop()
    messagebox.showinfo(title="About Us",message="Multiple Language Editor (WOW!)\nVersion 2.O\nFounder Ipsit Bhatt\nMultiple Editor 2.0")
def contactOperation():
   # win = Tk()
    #win.title("About Us")
    #win.geometry("400x400")
    #win.attributes("-topmost",True,"-toolwindow",True)
    #win.resizable(False,False)
    #win.mainloop()
    messagebox.showinfo(title="Contact",
                        message="THE TECHNICAL SOLUTION\n"
                                "Version 2.O\n"
                                "Founder Ipsit bhatt\n"
                                "Contact.No = 8979178483")
def companyOperation():
     #win = Tk()
     #win.title("About Us")
     #win.geometry("400x400")
     #win.attributes("-topmost",True,"-toolwindow",True)
     #win.resizable(False,False)
     #win.mainloop()
     messagebox.showinfo(title="Contact details", message="\nEmail: ipsitbhatt@outlook.com\nphone no: 8979178483\nMultiple Editor 2.0")
     #win.mainloop()
def compileOperation():
    try:#to avoid any mistakes

        fout = open("out.txt","w+")
        ferr = open("err.txt", "w+")
        subprocess.call(["javac",Fileinfo.fname],shell=True,stdout=fout,stderr=ferr)
        fout.seek(0)#to begining of file through seek
        if len(fout.read())==0:
            print("Sucessfully Compiled")
        ferr.seek(0)
        print(ferr.read())
    except Exception as ex:
        print(ex)



def runOperation():
    try:
        if Fileinfo.fname == None and Fileinfo.fname == "":
           print("No file Selected")
           return
        completepath = Fileinfo.fname.rpartition(".")[0]
        path = completepath.rpartition("/")[0]
        fn = completepath.rpartition("/")[2]
       # print(path,"-------",fn)
        if len(path) == 2:
            path = path + "/"
        #print(path, " --- ", fn)
        subprocess.call(["java","-cp",path,fn],shell=True)
    except Exception as ex:
        print(ex)


#main functions starts
window = Tk()
window.title("EDITOR FOR MULTIPLE LANGUAGE (WOW!)")
window.geometry("800x400")
mb = Menu(window)
window.configure(bg="blue",menu=mb)
mFile = Menu()
mEdit = Menu()
mFormat = Menu()
mExecute = Menu()
mHelp = Menu()
mprint = Menu()


mFile.add_command(label="New",command = newOperation)
mFile.add_command(label="Open",command = openOperation)
mFile.add_command(label="Save",command = saveOperation)
mFile.add_command(label="SaveAs",command =saveAsOperation)
mFile.add_separator()
mFile.add_cascade(label="print",menu=mprint)
mFile.add_separator()
mFile.add_command(label="Exit",command=exitprogram)

mprint.add_command(label="Print Preview")
mprint.add_command(label="Page Setup")
mprint.add_command(label="Print Document")

mEdit.add_command(label="Cut",command = cutOperator)
mEdit.add_command(label="Copy",command = copyOperator)
mEdit.add_command(label="Paste",command = pasteOperator)
mEdit.add_command(label="Select All",command = selectAllOpertaion)
mEdit.add_command(label="Find")
mEdit.add_command(label="Replace")

mFormat.add_command(label="Foreground",command = changeFG)
mFormat.add_command(label="Background",command = changeBG)
mFormat.add_command(label="Font")

mExecute.add_command(label="Compile",command = compileOperation)
mExecute.add_command(label="Run",command= runOperation)
mExecute.add_command(label="Option")

mHelp.add_command(label="About Us",command = aboutusOperation )
mHelp.add_command(label="Content",command = contactOperation)
mHelp.add_command(label="Technical Solution (REG)",command = companyOperation)

mb.add_cascade(label="File",menu=mFile)
mb.add_cascade(label="Edit",menu=mEdit)
mb.add_cascade(label="Format",menu=mFormat)
mb.add_cascade(label="Execute",menu=mExecute)
mb.add_cascade(label="Help",menu=mHelp)


sc1=Scrollbar(window)
sc2=Scrollbar(window,orient=HORIZONTAL)
sc1.pack(side="right",fill="y")
sc2.pack(side="bottom",fill="x")
tf = Text(window,wrap=NONE,yscrollcommand=sc1.set,xscrollcommand=sc2.set)
sc1.configure(command=tf.yview)
sc2.configure(command=tf.xview)
tf.pack(side="left",fill="both",expand=1)
window.protocol("WM_DELETE_window",exitprogram)
window.mainloop()