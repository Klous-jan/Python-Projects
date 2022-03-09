#tkinter
import tkinter 
from tkinter import *

#webpage generator
import webbrowser
import os


#GUI for py window
class Window(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry("{}x{}".format(460, 95))
        self.master.title("Webpage")
        self.master.config(bg="darkslategray")

        self.varText = StringVar()

        self.lblText = Label(self.master, text="What would you like the page to say? ", bg="darkslategray", fg="darkblue")
        self.lblText.grid(row=1, column=3, padx=(5,5), pady=(5,5))

        self.txtText = Entry(self.master, text=self.varText, bg="darkslategray", fg="darkblue")
        self.txtText.grid(row=2, column=1, rowspan=5, columnspan=8, padx=(5,5), pady=(5,5))

        self.btnSubmit = Button(self.master, text="Enter", width=30, bg="gray", fg="yellow", command=self.input)
        self.btnSubmit.grid(row=8, column=3, padx=(5,5), pady=(5,5))
        
        self.btnSubmit = Button(self.master, text="Exit", width=30, bg="gray", fg="red", command=self.exit)
        self.btnSubmit.grid(row=8, column=5, padx=(5,5), pady=(5,5))

#buttons for py window
#enters text field to gen on web page
    def enter(self):
        self.webbrowser.open_new_tab(filename)

#close application
    def exit(self):
        self.master.destroy()
    def input(self):
        pyinput = self.txtText.get()
        f = open("webpage.html", "w")    

#helps if i just have 2 copies of my code apparently.
        #html input -start-
        html_page = """
        <html>
            <body>
            <head>
                <link rel="stylesheet" href="stylesheet.css">
            </head>
                <h1>"""+pyinput+"""</h1>
            </body>
        </html>
        """
        #html input -end-
        f.write(html_page)

        f.close()
        webbrowser.open_new_tab("webpage.html")

if __name__ == "__main__":
    root = Tk()
    App = Window(root)
    root.mainloop()
