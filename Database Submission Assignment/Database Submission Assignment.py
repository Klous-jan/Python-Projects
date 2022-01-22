# Step 1
import sqlite3

# Connecting to the DB
conn = sqlite3.connect('DB_sub.db')

# Step 2
# creating a table in for the DB
with conn:
    cur = conn.cursor()
    # Step 2.1 - an auto-increment primary integer field
    # Step 2.2 - a data type 'string' field
    cur.execute("CREATE TABLE IF NOT EXISTS txt_files(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_extension TEXT)")
    conn.commit()

# Step 3.1 - the supplied list of file names
fileList = ('information.docx', 'Hello.txt', 'myImage.png',\
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# loop through each object in the tuple to find the files that end in .txt
for x in fileList:
    # Step 3.2 - determining which files from the list end with a “.txt” file extension
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        # The value for each row will be one file out or the tuple therefore (x,)
        # will denote a one element tuple for each file ending with .txt
            # tep 4 - add the file names from the list ending with “.txt” file extension within the database.
            cur.execute("INSERT INTO txt_files (file_extension) VALUES (?)", (x,))
            # Step 5
            print(x)
conn.close()

#Step 6 - code is commented
