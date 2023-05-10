'''
countdown Timer
'''
import time
from playsound import playsound
#pip3 install playsound


def countdown(user_time):
    while user_time >= 0:
        minutes, seconds = divmod(user_time, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer)
        time.sleep(1)
        user_time -= 1
    print('End !!')
    playsound(r'c:\Users\UZ1\Desktop\daily-coding\daily-coding\Day 4\alarm.mp3')

if __name__ == '__main__':
    user_time = int(input('Enter time in seconds: '))
    countdown(user_time)