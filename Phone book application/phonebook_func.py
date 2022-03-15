import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3

import phonebook_main
import phonebook_gui


def center_window(self, w, h):
    # Below - gets the user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    # Below - calculate x and y coordinates to pair the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # Below - closes the app
        self.master.destroy()
        os._exit(0)

#-------------------------------------------------------------------------------
def create_db(self):
    # Below - creating class object called "conn"
    conn = sqlite3.connect('phonebook.db')
    with conn:
        # Below - "conn.cursor()" using the "cursor" of the class object "conn"
        # Below - cursor is required to do our syntax like SQL quarys
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_phonebook( \
            ID INTERGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            );")
        # Below - if you dont commit, you dont actually make the database.
        conn.commit()
    # Below - closing the connection    
    conn.close()
    # Below - calls another function "first_run()"
    first_run(self)


def first_run(self):
    # Below - ('John','Doe','John Doe','123-456-7890','jdoe@email.com') is a tuple
    data = ('John','Doe','John Doe','123-456-7890','jdoe@email.com')
    conn = sqlite3.connect('phonebook.db')
    with conn:
        # Below - calling "conn.cursor()" and making it the variable "cur"
        cur = conn.cursor()
        # Below - count_records(cur) calls a function (see def count_records(cur) below)
        # and we pass in permission from cur "conn.cursor()" which will (see def count_records(cur)
        # execute, access the database, and return that all back and we will have the
        # "count" from the database due to "return cur,count"
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""", ('John','Doe','John Doe','111-111-1111','jdoe@email.com'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    # Below - ("""SELECT COUNT(*) FROM tbl_phonebook""")
    # this is counting all the rows, from the tbl_phonebook and returning it back
    # to the function "first_run(self)" where "cur,count = count_records(cur)" called it.
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    # Below -  the "cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")" above, counts from the tbl_phonebook.
    # the data will be returned back as a tuple, and the "cur.fetchone()[0]" below extracts that data and the "[0]
    # calls the first index in the tuple and passes that into "count" as a variable.
    count = cur.fetchone()[0]
    # Below -  this returns the data (described above) to the "first_run(self)" function 
    return cur,count

# Below - selects an item in ListBox
def onSelect(self,event):
    # Below - "event.widget" whatever is triggering the event.
    varList = event.widget
    # Below - "varList.curselection()[0]" its selection from the tuple [0] pulls from the first index. however it doesnt pull the text.. see below
    select = varList.curselection()[0]
    # Below - to get the text, pass the index "select" from above into varList.get(select)
    value = varList.get(select)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        # Below - col_fullname = [value], value = varList.get(select)
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        # This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            # Below - is accessint specific parts of the tuple and pulling those specific indexs
            # Below - deleting the text box first, then inserting the new extracted data
            self.txt_fname.delete(0,END)
            # Below - first part of the tuple
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            # Below - second part of the tuple
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            # Below - third part of the tuple
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            # Below - forth part of the tuple
            self.txt_email.insert(0,data[3])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # normalize the data to keep it consistent in the database, capitalizing first names ect
    var_fname = var_fname.strip() # This will remove any blank spaces before and after the user's entry
    var_lname = var_lname.strip() # This will ensure that the first character in each word is capitalized
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname)) # combine our normailzed names into a fullname
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email:
        print("Incorrect email format!!!")
        # Below - len = length, so, (len(var_fname) > 0) mean if the length of the first name is greater
        # than 0, same with last name and phone number, if they are greater then zero then to the following.
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and(len(var_email) > 0): # enforce the user to provide both names
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cursor = conn.cursor()
            # Check the database for existance of the fullname, if so we will alert user and disregard request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))#,(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: # if this is 0 then there is no existance of the fullname and we can add new data
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email))
                self.lstList1.insert(END, var_fullname) # update listbox with the new fullname
                onClear(self) # call the function to clear all of the textboxes
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                onClear(self) # call the function to clear all of the textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")


















