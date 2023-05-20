#!/bin/python

import time
import subprocess

print("Pomodoro Timer")
work_time = int(input("How long (minutes) should the work timer run? ")) * 60

def pom_timer(seconds):
    print("Running timer for " + str(seconds // 60) + " minutes.")
    time.sleep(seconds)
    print("Time's up!")
    subprocess.run(["afplay", "/System/Library/Sounds/Funk.aiff"])

pom_timer(work_time)

rest_option = input("Would you like to start a rest timer? y/n ")

if rest_option == "y":
    rest_time = int(input("How long (minutes) should the rest timer run? ")) * 60
    pom_timer(rest_time)
else:
    print("Ok. Goodbye.")