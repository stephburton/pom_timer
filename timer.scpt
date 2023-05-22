set theResponse to display dialog "How long should the timer run?" default answer "" buttons {"Cancel", "Continue"} default button "Continue" with icon POSIX file "/Users/steph/learn-python/pom_timer/pomodoro.png"

set timerDuration to missing value

-- Check the button clicked by the user
if button returned of theResponse is "Continue" then
    set timerDuration to (text returned of theResponse) as number
    -- Perform the default action for "Continue" button
    -- display dialog "Timer will run for " & timerDuration & " minutes."
    display dialog "Timer will run for " & timerDuration & " seconds."
else if button returned of theResponse is "Cancel" then
    -- Perform the action for "Cancel" button
    display dialog "Timer canceled."
end if

return timerDuration
