set theResponse to display dialog "How long should the timer run?" default answer "" buttons {"Cancel", "Continue"} default button "Continue" with icon POSIX file "/Users/steph/learn-python/pom_timer/pomodoro.png"

set timerDuration to missing value

if button returned of theResponse is "Continue" then
    try
        set timerDuration to (text returned of theResponse) as number
        display dialog "Timer will run for " & timerDuration & " minutes." with title "Pomodoro Timer"
    on error errText
        set terminalCommand to "echo " & quoted form of ("An error occurred: " & errText) & " >> /dev/tty"
        do shell script terminalCommand
        display dialog "Invalid input. Please try again." with title "Pomodoro Timer"
        set timerDuration to 0
    end try
else if button returned of theResponse is "Cancel" then
    display dialog "Timer canceled." with title "Pomodoro Timer"
end if

return timerDuration
