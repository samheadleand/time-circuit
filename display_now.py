import RPi.GPIO as GPIO
import time
import get_time
from datetime import datetime
import keypad

GPIO.setmode(GPIO.BCM)

pad = keypad.Keypad()

times = [3,2]

for slot in times:
    GPIO.setup(slot, GPIO.OUT)
    GPIO.output(slot, 0)

segments = [11,10,27,4,22,9,17]

#top 27
#top right 4
#bottom right 22
#bottom 9
#bottom left 11
#top left 10
#middle 17

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

digits = [14,15,18,23,24,25,8,1,7,12,16,20]

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)


num = {' ': [1,1,1,1,1,1,1],
       '0': [0,0,0,0,0,0,1],
       '1': [1,1,1,0,0,1,1],
       '2': [0,1,0,0,1,0,0],
       '3': [1,1,0,0,0,0,0],
       '4': [1,0,1,0,0,1,0],
       '5': [1,0,0,1,0,0,0],
       '6': [0,0,1,1,0,0,0],
       '7': [1,1,0,0,0,1,1],
       '8': [0,0,0,0,0,0,0],
       '9': [1,0,0,0,0,1,0],}

def time_to_display(time):
    if ' ' in time:
        return '            ', 'am'
    day, month, year, hour, minute = time[:2], time[2:4], time[4:8], time[8:10], time[10:]
    if int(day) > 31:
        return '            ', 'am'
    if int(month) > 12:
        return '            ', 'am'
    if int(hour) > 23:
        return '            ', 'am'
    elif int(hour) > 11:
        return (time, day + month + year + get_time.add_zero_to_datetimes(str(int(hour) - 12)) + minute, 'pm')
    else:
        return (time, time, 'am')



while True:
    now = datetime.now()
    # If nows time use this
    if get_time.find_time(now)[0] == 'am':
        GPIO.output(times[0], 1)
        GPIO.output(times[1], 0)
    else:
        GPIO.output(times[0], 0)
        GPIO.output(times[1], 1) 
    numbers = get_time.find_month_date(now) +  get_time.find_year(now) + get_time.find_time(now)[1]
    
    for counter,digit in enumerate(digits):
        for segment in range(7):
            GPIO.output(segments[segment], num[numbers[counter]][segment])
        GPIO.output(digit, 1)
        time.sleep(0.001)
        GPIO.output(digit, 0)
        

