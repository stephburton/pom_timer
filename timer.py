#!/usr/bin/env python

import time
import subprocess

def pom_timer(seconds):
    """
    Run the timer for a specified number of seconds.
    After the timer is complete, it prints "Time's up!".
    """
    print("Running timer for " + str(seconds // 60) + " minutes.")
    time.sleep(seconds)
    print("Time's up!")

def work_interval():
    """
    Ask the user for the length of time the work interval should run.
    Multiply by 60 to get the number of seconds.
    Run the pom_timer function.
    Alert with a sound specific to the work_interval.
    Run the rest_interval function.
    """
    try:
        interval = int(input("How long (minutes) should the work timer run? ")) * 60
        pom_timer(interval)
        subprocess.run(["afplay", "/System/Library/Sounds/Funk.aiff"])
        rest_interval()
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        work_interval()
    except KeyboardInterrupt:
        print("\nTimer interrupted. Cancelling the timer...")
    except EOFError:
        print("End of input reached. Exiting timer...")

def rest_interval():
    """
    Ask the user if they want to start a rest interval.
    If yes...
    Ask the user for the length of time the work interval should run.
    Multiply by 60 to get the number of seconds.
    Run the pom_timer function.
    Alert with a sound specific to the rest_interval.
    If no...
    Print "Ok. Goodbye."
    If the user answers with something other than "y" or "n"...
    Print "Invalid input. Please answer y or n."
    Run the rest_interval function.
    """
    rest_option = ""

    while rest_option not in ["y", "n"]:
       rest_option = input("Would you like to start a rest timer? (y/n) ")

       if rest_option == "y":
          try:
            interval = int(input("How long (minutes) should the rest timer run? ")) * 60
            pom_timer(interval)
            subprocess.run(["afplay", "/System/Library/Sounds/Blow.aiff"])
          except ValueError:
              print("Invalid input. Please enter a valid integer.")
              rest_interval()
          except KeyboardInterrupt:
              print("\nTimer interrupted. Cancelling the timer...")
          except EOFError:
              print("End of input reached. Exiting timer...")
       elif rest_option == "n":
          print("Ok. Goodbye.")
       else:
          print("Invalid input. Please answer y or n.")

def main():
    print("Pomodoro Timer")
    work_interval()

if __name__ == "__main__":
    main()