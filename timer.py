#!/usr/bin/env python

import time
import subprocess

def system_dialog(script):
    """
    Kicks off the timer.scpt script
    Collects the user's input and converts it to an integer, which is multiplied by 60 to give the number of minutes
    Prints the number of minutes to the terminal (which is not necessary but feedback is good)
    Passes the interval variable's value to the pom_timer function
    """
    try:
        output = subprocess.check_output(['osascript', script]).decode('utf-8').strip()
        print("The timer will run for " + output + " minutes.")
        interval = int(output[0]) * 60
        pom_timer(interval)
    except subprocess.CalledProcessError as e:
        print("An error occurred while executing timer.scpt.")
        print("Error message:", str(e))
    except Exception as e:
        print("An unexpected error occurred:", str(e))

def pom_timer(interval):
    """
    Uses the Python time module to make the process "sleep" for the number of minutes (interval)
    Emits a noise when the sleep period ends
    Runs the timer_end.scpt script
    Passes information about what button the user has clicked to the new_timer function
    """
    try:
        time.sleep(interval)
        subprocess.run(["afplay", "/System/Library/Sounds/Hero.aiff"])
        output = subprocess.check_output(['osascript', 'timer_end.scpt']).decode('utf-8').strip()
        new_timer(output)
    except subprocess.CalledProcessError as e:
        print("An error has occurred while running the timer.")
        print("Error message:", str(e))
    except Exception as e:
        print("An unexpected error occurred:", str(e))

def new_timer(output):
    """
    Checks the user's response (button clicked) and performs actions based on the response
    If "Yes" the system_dialog function will run again
    If "No" the goodbye.scpt script is run
    If some other option were to be triggered, a message is printed to the terminal
    """
    if "Yes" in output:
        print("User wants to start a new timer.")
        system_dialog(script)
    elif "No" in output:
        print("User does not want to start a new timer.")
        subprocess.run(['osascript', 'goodbye.scpt'])
    else:
        print("Unknown button response")

script = 'timer.scpt'

def main():
    """
    Prints the name of the script to the terminal
    Kicks off the system_dialog function
    """
    print("Pomodoro Timer")
    system_dialog(script)

if __name__ == "__main__":
    main()
