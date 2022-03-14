import shutil
from datetime import datetime, timedelta
import os


def GetList():
    
    #Start FOlder
    startTransfer = '/Users/Owner/Desktop/One Page Site/New/fullDay'

    #End Folder
    finishTransfer = '/Users/Owner/Desktop/One Page Site/New/homeOffice'

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
            print('No files were transfered')

# Execute function
GetList()
