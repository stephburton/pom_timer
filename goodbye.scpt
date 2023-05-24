set folderPath to POSIX path of ((path to me as text) & "::")
set constantsScript to folderPath & "constants.py"

set pythonCommand to "python -c 'import sys, os; sys.path.append(os.path.dirname(\"" & constantsScript & "\")); import constants; print(os.path.join(os.path.dirname(\"" & constantsScript & "\"), constants.ICON_FILE)); print(constants.TITLE)'"

set constantInfo to do shell script pythonCommand

set {iconPath, titleText} to paragraphs of constantInfo

set theResponse to display dialog "Goodbye" with title (titleText as text) buttons {"OK"} default button "OK" with icon file (iconPath as POSIX file)
