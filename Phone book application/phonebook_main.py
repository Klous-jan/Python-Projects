# Python ver:   3.9.7
#
# Author:       Nickolaus Janak
#
# Purpose:      Phonebook demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and child relationships.
#
# Tested OS:    This code was written and tested to work with Windows 10.

import tkinter
from tkinter import *
import tkinter as tk

import phonebook_gui
import phonebook_func

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.geometry('{}x{}+{}+{}'.format(500, 300, -2660, 350))
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        # Below - the CenterWindow method will center the app
        # on the user's screen
        ##phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        # Below - This protocol method is a tkinter built-in method to
        # catch if the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module,
        # keeping your code compartmentalized and cluster free
        phonebook_gui.load_gui(self)



if __name__ == "__main__":
    # Below - syntax to create a window from the Tkinter
    root = tk.Tk()
    # Below - calling our class the "app" and attached "root" the Tkinter window
    App = ParentWindow(root)
    # Below - without "root.mainloop()" the window would instantly close
    # it will fire constantly to keep the window open
    root.mainloop()
    # Summary of above - take the first Tkinter object window "tk.Tk()" we named
    # it root we attached that root to the class "ParentWindow", then
    # root.mainloop() is saying take the "root" from "root = tk.Tk()"
    # and make it a main loop to keep the window open
















   
