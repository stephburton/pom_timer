set folderPath to POSIX path of ((path to me as text) & "::")
set constantsScript to folderPath & "constants.py"

set pythonCommand to "python -c 'import sys, os; sys.path.append(os.path.dirname(\"" & constantsScript & "\")); import constants; print(os.path.join(os.path.dirname(\"" & constantsScript & "\"), constants.ICON_FILE)); print(constants.TITLE)'"

set constantInfo to do shell script pythonCommand

set {iconPath, titleText} to paragraphs of constantInfo

set theResponse to display dialog "Time's up! Would you like to start a new timer?" with title (titleText as text) buttons {"Yes", "No"} default button "No" with icon file (iconPath as POSIX file)

set newTimer to missing value

if button returned of theResponse is "Yes" then
    set newTimer to "Yes"
else if button returned of theResponse is "No" then
    set newTimer to "No"
end if

return newTimer