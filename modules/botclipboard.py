import win32clipboard as clp, win32api

class BotClipboard():
	"""Class for the Windows Clipboard. Initializes with the Windows Clipboard Format parameters."""
	def __init__(self):
		self.text = 13 #it is a numeric representation of format for UTF-8 
		self.filepath = 49158 #representation for filepath when you copy files into clipboard
		self.format_numbers=[None]
		self.format_names=[]

	def get_text(self): #We are only working in "UTF-8" mode to avoid any errors when copying utf-8 specific characters.
		clp.OpenClipboard(None)
		rc= clp.EnumClipboardFormats(0) #According to MSDN we start iterating from zero and each time supplying the previous number in iteration. When it reaches the end of the list it sends false(I guess).
		while rc:
			try: theformat= clp.GetClipboardFormatName(rc) #THESE THREE LINES ARE THERE TO SEE THE NAMES OF THE FORMATS
			except win32api.error: theformat= "?"
			#print ("format", rc, theformat) Uncomment this line to see all avalable formats.
			self.format_names.append(theformat)
			self.format_numbers.append(rc)
			rc= clp.EnumClipboardFormats(rc)
		if (self.text in self.format_numbers):
			text = clp.GetClipboardData(self.text)
		else:
			text = ''
		return text
#		return self.format_numbers
		clp.CloseClipboard()

	def put_text(self, text):
		clp.OpenClipboard(None)
		clp.SetClipboardText(text, self.text)
		clp.CloseClipboard()