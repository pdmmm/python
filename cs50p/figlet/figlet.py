import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    randomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--f"):
    randomFont = False
else:
    sys.exit("Invalid usage")

figlet.getFonts()

if randomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        sys.exit("Invalid usage")
else:
    font = random.choice(figlet.getFonts())

message = input("Input: ")

print("Output:")
print(figlet.renderText(message))
