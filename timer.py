#!/usr/bin/env python

import time
import subprocess

def system_dialog(script):
    output = subprocess.check_output(['osascript', script]).decode('utf-8').strip()
    # print("The timer will run for " + output + " minutes.")
    # interval = int(output[0]) * 60
    print("The timer will run for " + output + " seconds.")
    interval = int(output[0])
    pom_timer(interval)

def pom_timer(interval):
    time.sleep(interval)
    subprocess.run(["afplay", "/System/Library/Sounds/Hero.aiff"])
    output = subprocess.check_output(['osascript', 'timer_end.scpt']).decode('utf-8').strip()
    new_timer(output)

def new_timer(output):
    if "Yes" in output:
        print("Yes button clicked")
        system_dialog(script)
    elif "No" in output:
        print("No button clicked")
        subprocess.run(['osascript', 'goodbye.scpt'])
    else:
        print("Unknown button response")

script = 'timer.scpt'

def main():
    print("Pomodoro Timer")
    system_dialog(script)

if __name__ == "__main__":
    main()
