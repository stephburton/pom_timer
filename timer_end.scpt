set theResponse to display dialog "Time's up! Would you like to start a new timer?" buttons {"Yes", "No"} default button "No" with icon POSIX file "/Users/steph/learn-python/pom_timer/pomodoro.png"

set newTimer to missing value

if button returned of theResponse is "Yes" then
    set newTimer to "Yes"
else if button returned of theResponse is "No" then
    set newTimer to "No"
end if

return newTimer