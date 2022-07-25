#Python practice
#Emoji converter with functions
from colorama import Fore
import sys

class main_prog:
    def prog_excec(user_message):
        user_words = user_message.split(" ")
        emoji = {
            ":)": "😊",
            ":(": "😥"
            }
        result = ""
        for x in user_words:
            result += emoji.get(x, x) + " "
        return result
    begg = input(Fore.LIGHTBLUE_EX + "What's your name: ")
    res = input("Hello " + begg + " " + "Do you wanna try our emoji converter? (y)es or (n)o: ")
    if res == 'n':
        print("Thank you bye!")
        sys.exit()
    else:
        prog_excec
    user_message = input(Fore.LIGHTBLUE_EX + """┌──(python3㉿emojiconverter)-[~]
└─# """)

    print(prog_excec(user_message))

    


            

       