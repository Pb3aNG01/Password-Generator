import string
import secrets
import tkinter
from tkinter import messagebox

def checkPassWord(str) -> bool:
    if len(set(str)) == len(str):
        flagl, flagu, flagn, flags = False, False, False, False
        for s in str:
            if s in string.ascii_lowercase:
                flagl = True
            if s in string.ascii_uppercase:
                flagu = True
            if s in string.digits:
                flagn = True
            if s in string.punctuation:
                flags = True
        return flagl and flagu and flagn and flags
    return False

def genPassWord(length):
    passcharacters = string.ascii_letters + string.digits + string.punctuation
    
    while True:
        passgen = ''.join(secrets.choice(passcharacters) for i in range(length))
        if checkPassWord(passgen):
            return passgen
        else:
            passgen = ''.join(secrets.choice(passcharacters) for i in range(length))
            continue

def guiWin():
    main_window = tkinter.Tk()
    main_window.geometry("400x200")
    top_frame = tkinter.Frame()
    mid_frame = tkinter.Frame()
    bot_frame = tkinter.Frame()
    
    l = tkinter.IntVar()

    def showpass():
        test = genPassWord(l.get())
        genpass.config(text=test)
        return test
    
    def copypass():
        main_window.clipboard_clear()
        main_window.clipboard_append(showpass())
        messagebox.showinfo("Password Copied", "Password copied to clipboard")
        main_window.update()

    prompt_label = tkinter.Label(top_frame, text = 'Please enter the length you want the password:')
    length_scale = tkinter.Scale(top_frame, variable=l, from_=8, to=32, orient="horizontal")
    prompt_label.pack(side="left")
    length_scale.pack(side="left")
    top_frame.pack()
    
    yourpass_label = tkinter.Label(mid_frame, text = 'Your password is:')
    genpass = tkinter.Label(mid_frame, text = '')
    yourpass_label.pack(side="left")
    genpass.pack(side="left")
    mid_frame.pack()
    
    displaypass_button = tkinter.Button(bot_frame,text="Display Password", command = showpass)
    getpass_button = tkinter.Button(bot_frame, text="Get Password", command = copypass)
    quit_button = tkinter.Button(bot_frame, text = 'Quit', command=main_window.destroy)
    displaypass_button.pack(side="left")
    getpass_button.pack(side="left")
    quit_button.pack(side="left")
    bot_frame.pack()
    
    tkinter.mainloop()
    
guiWin()