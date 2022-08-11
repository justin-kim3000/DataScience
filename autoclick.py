from math import radians
import pyautogui
import time
import random


i=0
chack_minutue_time = 50
for i in range(0,chack_minutue_time):
    random_x = random.randint(1,2000)
    random_y = random.randint(1,2000)

    # pyautogui.click(100, 109, button='left', clicks=1, interval=1)
    # time.sleep(1)
    # pyautogui.click(1000, 1009, button='left', clicks=1, interval=1)
    pyautogui.click(random_x,random_y)
    time.sleep(1)
    


print('작업을 완료하였습니다.')