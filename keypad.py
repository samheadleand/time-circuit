import time, random, RPi.GPIO as GPIO
from datetime import datetime

# 0 5 6 13 19 26 21

ROW = [5,21,26,13] # Inputs as below

COLUMN = [6,0,19] # Outputs - set to zero

MAPPING = {(0, 0): '1', (0, 1): '2', (0, 2): '3',
           (1, 0): '4', (1, 1): '5', (1, 2): '6',
           (2, 0): '7', (2, 1): '8', (2, 2): '9',
           (3, 0): 'clear', (3, 1): '0', (3, 2): '.',
           }

    

class Keypad:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        for c in COLUMN:
            GPIO.setup(c, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        for r in ROW:
            GPIO.setup(r, GPIO.OUT)
            GPIO.output(r, 1)
        self.last_time_called = datetime.now()

    def all_rows_on(self):
        for r in ROW:
            GPIO.output(r, 1)

    def scan(self, now):
        if (now - self.last_time_called).total_seconds() < 1:
            return False
        #which key has been pressed
        #run loop over each column, set the one I'm on to zero and the other two to 1
        #check to see if row input is zero or one
        for r in ROW:
            self.all_rows_on()
            GPIO.output(r, 0)
            time.sleep(0.0001)
            for c in COLUMN:
                if not GPIO.input(c):
                    self.last_time_called = now
                    return MAPPING[(ROW.index(r), COLUMN.index(c))]
        return False
