#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

try:
	import Tkinter
except ImportError:
	raise ImportError,"The Tkinter module is required to run this program"

try:
	from PIL import ImageTk, Image
except ImportError:
	raise ImportError,"The ImageTk module is required to run this program"

try:
	import MySQLdb
except ImportError:
	raise ImportError,"The MySQLdb module is required to run this program"
	
db = MySQLdb.connect(host="localhost",user="fadhilsuhendi",passwd="fadil278823",db="hotel")
cursor = db.cursor()
	
class hotelApp(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        img = self.img = ImageTk.PhotoImage(Image.open('hotel_picture.jpg'))
        panel = Tkinter.Label(self,image=img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        panel.grid(column=0,row=0)

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable, width = 50)
        self.entry.grid(column=0,row=1,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter the query:")

        button = Tkinter.Button(self,text=u"Find",
                                command=self.OnButtonClick)
        button.grid(column=1,row=1)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,height=20, justify="left",textvariable=self.labelVariable,
                              anchor="w",fg="yellow",bg="blue")
        label.grid(column=0,row=2,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Hello!")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())       
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
		cursor.execute(self.entryVariable.get())
		db.commit()
		string =""
		result = cursor.fetchall()
		for row in result:
			for i in row:
				string = string + " | "+ str(i)
			string = string + "\n"
		self.labelVariable.set(string)
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self,event):
		cursor.execute(self.entryVariable.get())
		db.commit()
		string =""
		result = cursor.fetchall()
		for row in result:
			for i in row:
				string = string + " | "+ str(i)
			string = string + "\n"
		self.labelVariable.set(string)
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)

if __name__ == "__main__":
    app = hotelApp(None)
    app.title('Welcome to hotel database')
    app.mainloop()
