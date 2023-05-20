#!/bin/python

import time
import subprocess

print("Pomodoro Timer")
work_time = int(input("How long (minutes) should the work timer run?")) * 60

def work_timer(seconds):
    print("Running work time for " + str(seconds // 60) + " minutes.")
    time.sleep(seconds)
    print("Time's up!")
    subprocess.run(["afplay", "/System/Library/Sounds/Funk.aiff"])

work_timer(work_time)

rest_option = input("Would you like to start a rest timer? y/n")

def rest_timer(seconds):
    print("Running rest timer for " + str(seconds // 60) + " minutes.")
    time.sleep(seconds)
    print("Time's up!")
    subprocess.run(["afplay", "/System/Library/Sounds/Blow.aiff"])

if rest_option == "y":
    rest_time = int(input("How long (minutes) should the rest timer run?")) * 60
    rest_timer(rest_time)
else:
    print("Ok. Goodbye.")