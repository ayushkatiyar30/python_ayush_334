#python 
#if(): elif(): else:
import time
timestamp= time.strftime("%H:%M:%S")
print(timestamp)
hour= int(time.strftime('%H'))
# print(hour)
min= int(time.strftime("%M"))
# print(min)
sec= int(time.strftime("%S"))
# print(sec)
print(f"current time: {hour:02d}:{min:02d}:{sec:02d}")
if( 0 <= hour < 12):
    # if(min > 0):
    print("Good morning")
elif(hour == 12 and min==0):
        print("Good noon")
elif(hour >= 12 and hour < 17):
    print("Good Afternoon")
elif(hour >= 17 and hour <21):
    print("Good Evening")
else:
     print("Good Night")