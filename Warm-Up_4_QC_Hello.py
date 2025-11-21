"""
Filename: Warm-Up_4_QC_Hello.py
Author: <Lastname, Firstname>
Created: <MM/DD/YYYY>
Instructor: Holtslander
"""

import time

def hello():
    """
    Asks the user to input their name. Stores their name in a variable and prints the message:
    "Hello, <name>"
    :return: None
    """
    ### YOUR CODE GOES HERE ###

    while True:
        name = input("What is your name?\n")
        time.sleep(1)
        
        if name == "" or name == " "*len(name):
            print("Please input at least one character!")
            time.sleep(3)
        else:
            print(f"Hello, {name}")
            break

### YOU SHOULD NOT NEED TO CHANGE ANYTHING HERE ###
if __name__ == '__main__':

    #  hello bro 👀
    hello()
