import time
import os
import sys
sys.path.insert(0, os.getcwd() + '\modules')

import pprint
import botclipboard
from tkinter import *
import sys


root = Tk()
root.title('Alesha')
root.iconbitmap(default='transparent.ico')

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (ws-20, 28, 0, hs-110))
root.wm_attributes("-topmost", 1) #keep the window above all windows
root.overrideredirect(True)

b1 = Button(root,text="One")
b2 = Button(root,text="Two")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b1.configure(bg = "#2DA507")
root.mainloop()




clipobj = botclipboard.BotClipboard()
mytxt = clipobj.get_text()
mytxt = mytxt.replace('g', '12345')
print(mytxt)
clipobj.put_text(mytxt)
