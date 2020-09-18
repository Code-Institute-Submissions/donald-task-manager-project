
i = 1
while i <= 10:
    print(i)
    i += 1


secret_word = "moron"
think = ""
number_count = 0
time_limit = 4
cannot_guess = False


while think != secret_word and not(cannot_guess):
    if number_count < time_limit:
        think = input("Enter the right word: ")
        number_count += 1
    else:
        cannot_guess: True

if time_limit:
    print("you passed")
else:
    print("you are a loser")