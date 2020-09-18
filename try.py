import random
import tkinter


guesser = True
while guesser:
    number = input("put the right number: ")

    if number.isdigit():
        print("Ok! Let's go")
        number = int(number)
        guesser = False
    else:
        print("this is wrong. Put the right number")

rand_number = random.randint(1,number)

