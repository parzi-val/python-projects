from tkinter import *  # pylint: disable=unused-wildcard-import
from gtts import gTTS
from playsound import playsound
import os

def Text_to_speech():
    Message = entryfield.get()
    speech = gTTS(text = Message)
    speech.save('someshit.mp3')
    playsound('someshit.mp3')

def exit():
    root.destroy()

def reset():
    Msg.set("")
    os.remove(r"C:\Users\KR Bala\Desktop\python\python code school\someshit.mp3")

root = Tk() #Initisalising tkinter for GUI
root.geometry('600x100') #Sets size
root.configure(bg='gray14',) #Sets bg
root.title("Text2Speech") #Sets Title name
Label(root, text = "Text to Speech",bg = 'gray14', font = 'ariel 15',fg = 'white').pack()
Label(root, text = "Enter Text Here :", font = "ariel 12", fg = 'white',bg = 'gray14').place(x  = '0', y = '30')
Msg = StringVar()
entryfield = Entry(root, text = "Enter Text",font = "ariel 12 ",bg = 'white smoke' ,width = 50, textvariable = Msg)
entryfield.place(x = 125 , y = 30)

Button(root, text = "Play",width = 10,command = Text_to_speech,).place(x = '125', y = '55')
Button(root, text = "Reset",width = 10,command = reset).place(x = '300', y = '55')
Button(root, text = "Exit",width = 10,command = exit).place(x = '500', y = '55')
mainloop()