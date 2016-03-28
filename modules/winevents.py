"""https://social.msdn.microsoft.com/Forums/windows/en-US/1dc356e6-9441-44de-9eda-247003fa6ef5/copy-selected-text-from-any-window?forum=winformsapplications"""
import time 
import pprint
import pyautogui
import pythoncom, pyHook
import win32api, win32gui, win32process, win32ui



hwnd = win32gui.GetForegroundWindow()
proc = win32process.GetWindowThreadProcessId(hwnd)
print(proc)
print(win32gui.GetWindowText(hwnd))
time.sleep(3)


"""
class Winevents():
	def __init__(self):
		self.selection = '';

	def highlighted:
		if """
