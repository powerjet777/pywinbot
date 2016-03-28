import time
import os
import sys
sys.path.insert(0, os.getcwd() + '\modules')

import pprint
import botclipboard
from tkinter import *


"""

root = Tk()
root.title('Alesha')
root.iconbitmap(default='transparent.ico')
root.wm_attributes("-toolwindow", 1) #keep the window above all windows
b1 = Button(root,text="One")
b2 = Button(root,text="Two")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (ws, 150, 0, hs-250))
root.mainloop()

"""




clipobj = botclipboard.BotClipboard()
mytxt = clipobj.get_text()
#mytxt = mytxt.encode(encoding="utf-8")
mytxt = mytxt.replace(' ', 'gogogo')
print(mytxt)
clipobj.put_text(mytxt)
