# Python Pomodoro Timer - Project Notes

## Why am I building this thing...

I'm building this very small app to learn how to write Python code. Why a pomodoro timer? Because I'm trying to learn a lot of things right now and I have ADHD. I've found the pomodoro method to be very helpful when I'm trying to learn a lot of dense stuff. Especially if I want to learn quickly.

## What have I done so far...

### May 20, 2023

- Created the bare-bones timer
- Created this repo
- [Condensed the timer functions into one single function](https://github.com/stephburton/pom_timer/pull/1)
- [Separated the work and rest intervals into their own functions, so I can add different alert sounds](https://github.com/stephburton/pom_timer/pull/2)
- [Made a number of improvements in this PR](https://github.com/stephburton/pom_timer/pull/3)
  - Learned about and added a main guard
  - Learned about docstrings and added some of those (why are they so ugly?)
  - Switched out the conditional in the rest_interval function for a while loop
  - Learned about try-except blocks and added some error handling (ValueError, KeyboardInterrupt, EOFError)
