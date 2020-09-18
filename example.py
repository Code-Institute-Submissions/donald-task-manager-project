is_male = True
is_fat = False

if is_male and is_fat:
    print("you are a male or fat or both")
elif is_male and not(is_fat):
    print("you are small and fry")
elif not(is_male) and is_fat:
    print("you are not small and fry")
else:
    print("You are not a male or fat or both")

def main_num (fact1, fact2, fact3, fact4):
    if fact1 <= fact2 and fact3 >= fact4:
        return fact1
    elif fact2 != fact1 and fact3 <= fact4:
        return fact3
    else:
        return fact3

print(main_num(12, 10, 22, 40))
