from datetime import datetime
from time import sleep
import random

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

# odd2 using loops
for i in range(4):  
    right_this_minute = datetime.today().minute
    if right_this_minute in odds: #This : introduces the suite of code.
        print("This minute is odd")
        print("current time is:", datetime.today())
    else:
        print("Not an odd minute")
        print("current time is:", datetime.today())
    sleep(random.randint(1,59))


    

