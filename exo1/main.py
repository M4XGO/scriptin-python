import os
import time
import datetime


repertory = './tmp'

def main():
    files = os.listdir(repertory)
    now = datetime.datetime.now()
    ten_days_ago = now + datetime.timedelta(days = -10)
    for file in files :
        modification_time = os.path.getmtime(repertory+"/"+file)
        modification_datetime = datetime.datetime.fromtimestamp(modification_time)
        local_time = time.ctime(modification_time)
        if modification_datetime < ten_days_ago:
            print(file, 'will be erease --> ', str(local_time))
        else: 
            print(file, 'other files    --> ', str(local_time))


main()
