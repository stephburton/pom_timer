#!/bin/python

import time
import subprocess

print("Pomodoro Timer")

def pom_timer(seconds):
  print("Running timer for " + str(seconds // 60) + " minutes.")
  time.sleep(seconds)
  print("Time's up!")

def work_interval():
  work_time = int(input("How long (minutes) should the work timer run? ")) * 60
  pom_timer(work_time)
  subprocess.run(["afplay", "/System/Library/Sounds/Funk.aiff"])
  rest_interval()

def rest_interval():
  rest_option = input("Would you like to start a rest timer? y/n ")

  if rest_option == "y":
    rest_time = int(input("How long (minutes) should the rest timer run? ")) * 60
    pom_timer(rest_time)
    subprocess.run(["afplay", "/System/Library/Sounds/Blow.aiff"])
  elif rest_option == "n":
    print("Ok. Goodbye.")
  else:
    print("Invalid input. Please answer y or n.")
    rest_interval()

work_interval()