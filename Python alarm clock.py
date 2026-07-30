#Python alarm clock

import time
import datetime

def set_alarm(alarm_time) :
    print(f"Alarm set for {alarm_time}")
    running = True

    while running :
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time :
            print("WAKE UP")
            running = False

        time.sleep(1)


if __name__ == "__main__" :
    alarm_time = input("Enter the Alarm time (HH:MM:SS) : ")
    set_alarm(alarm_time)
    
