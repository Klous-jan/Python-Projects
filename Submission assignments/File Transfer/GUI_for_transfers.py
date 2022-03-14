# [x] Allow the user to browse and choose a specific folder that will contain the files to be checked daily.   |
# [x] Allow the user to browse and choose a specific folder that will receive the copied files.                |
# [x] Allow the user to manually initiate the 'file check' process that is performed by the script.            |
# [x] Add comments throughout your Python explaining your code.                                                |
#______________________________________________________________________________________________________________|

import tkinter
from tkinter import *
import os
import shutil
from datetime import datetime, timedelta
import tkinter.filedialog

class uiWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)

        # Building the window
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry("{}x{}".format(405,140))
        self.master.title("File Transfer")
        self.master.config(bg="darkslategray")

        #Start button
        self.btnTransfer = Button(self.master, text="Start", bg="gray", fg="yellow", width=42, command=GetList)
        self.btnTransfer.grid(row=5, column=4, padx=(5,5))

        #File Transfer title
        self.lblHL = Label(self.master, text="File Transfer", bg="darkslategray", fg="green")
        self.lblHL.grid(row=0, column=4, padx=(5,5), pady=(5,5))

        #From button text
        self.btnBrowse = Button(self.master, text="From:", bg="gray", fg="yellow", width=10, command=chooseFileStart)
        self.btnBrowse.grid(row=1, column=1, padx=(5,5), pady=(5,5))

        #From button field
        self.folderA = Entry(self.master, text=folderStart, width=50, bg="gray", fg="yellow")
        self.folderA.grid(row=1, column=2, columnspan=5, padx=(5,5), pady=(5,5))

        #To button text
        self.btn1Browse = Button(self.master, text="To:", bg="gray", fg="yellow", width=10, command=chooseFileEnd)
        self.btn1Browse.grid(row=3, column=1, padx=(5,5), pady=(5,5))

        #To button field
        self.folderB = Entry(self.master, text=folderEnd, width=50, bg="gray", fg="yellow")
        self.folderB.grid(row=3, column=2, columnspan=5, padx=(5,5), pady=(5,5))
         
def chooseFileStart():

    name = tkinter.filedialog.askdirectory()
    folderStart.set(name)

def chooseFileEnd():
    name = tkinter.filedialog.askdirectory()
    folderEnd.set(name)

def GetList():
    
    #Start FOlder
    startTransfer = folderStart.get()

    #End Folder
    finishTransfer = folderEnd.get()

    #File type looking for during transfer
    fileType = '.txt'

    cur_time = datetime.now()
    files = os.listdir(startTransfer)


    for i in files:
        #getting the dates of the files and modding time to the last 24 hours and converting seconds to days
        file_path = os.path.join(startTransfer, i)
        past_24hr = cur_time - timedelta(hours=24)
        mod_time = os.path.getmtime(file_path)
        recentlyUpdated = datetime.fromtimestamp(mod_time)
        if past_24hr < recentlyUpdated:
            shutil.move(startTransfer + '/' + i, finishTransfer)
            print(i + ' success!')
            #success.set(' success!')
        else:
            print('Not transfered')
           
    
if __name__ == "__main__":
    root = Tk()
    folderStart = StringVar()
    folderEnd = StringVar()
    App = uiWindow(root)
    root.mainloop()
