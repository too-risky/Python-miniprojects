#Countdown programme 2

import time

end1= int(input("Enter designated amount of time : "))

def count(start, end) :
    for x in range(start, end+1) :
        print(x)
        time.sleep(1)
    print("~~DONE!!~~")

count(0, end1)