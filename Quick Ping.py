from datetime import date
from datetime import datetime
import calendar
import time
from plyer import notification

day_selected=0
hour_selected=0
subject_selected=()
days_of_week=[]
timetable=[[]*7]*24

days, hours = (7, 24)
timetable=[]

for i in range(days):
    
    day = []
    for hour in range(hours):
        day.append(hour)
    
    timetable.append(day)
    
while (day_selected<8):
    print("enter the day for which you want to enter data \n 0 for Monday and 6 for Sunday and 8 to stop entering data")
    day_selected=int(input("enter your day"))   
    if (day_selected<7):
        while(hour_selected<24):
            print("enter the hour of the for which you want to enter data \n 0 for midnight, 1 for 1am etc and 23 for 11pm and 24 to stop entering data")
            hour_selected=int(input("enter your hour"))
            if(hour_selected<24):
                subject_selected=str(input("enter your subject"))
                timetable[day_selected][hour_selected]=subject_selected


print(timetable)
last_subject="Lastone"
while(day_selected==8):
    curr_date = date.today()
    day=calendar.day_name[curr_date.weekday()]
 
    if (day=="Monday"): current_day=0
    if (day=="Tuesday"): current_day=1
    if (day=="Wednesday"): current_day=2
    if (day=="Thurday"): current_day=3
    if (day=="Friday"): current_day=4
    if (day=="Saturday"): current_day=5
    if (day=="Sunday"): current_day=6

    now = datetime.now()
    current_time = int(now.strftime("%H"))
    current_subject=timetable[current_day][current_time]
    if (current_subject!=last_subject):
        last_subject=current_subject
        if __name__ == '__main__':
            while True:
                print("check")
                notification.notify(title = "**Reminder!!",message ="You have a class of " +str(last_subject),timeout= 12)
                #time.sleep(6)
                time.sleep(60*60)
        
                 
