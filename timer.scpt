set folderPath to POSIX path of ((path to me as text) & "::")
set constantsScript to folderPath & "constants.py"

set pythonCommand to "python -c 'import sys, os; sys.path.append(os.path.dirname(\"" & constantsScript & "\")); import constants; print(os.path.join(os.path.dirname(\"" & constantsScript & "\"), constants.ICON_FILE)); print(constants.TITLE)'"

set constantInfo to do shell script pythonCommand

set {iconPath, titleText} to paragraphs of constantInfo

set theResponse to display dialog "How long should the timer run?" with title (titleText as text) default answer "" buttons {"Cancel", "Continue"} default button "Continue" with icon file (iconPath as POSIX file)

set timerDuration to missing value

if button returned of theResponse is "Continue" then
    try
        set timerDuration to (text returned of theResponse) as number
        display dialog "Timer will run for " & timerDuration & " minutes." with title (titleText as text) with icon file (iconPath as POSIX file)
    on error errText
        set terminalCommand to "echo " & quoted form of ("An error occurred: " & errText) & " >> /dev/tty"
        do shell script terminalCommand
        display dialog "Invalid input. Please try again." with title (titleText as text) with icon file (iconPath as POSIX file)
        set timerDuration to 0
    end try
end if

return timerDuration
