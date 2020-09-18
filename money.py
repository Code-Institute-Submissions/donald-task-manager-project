def turn(phrase):
    phrasing = ""
    for letter in phrase:
        if letter in "aeiou":
            phrasing = phrasing + "ratting"
        else:
            phrasing = phrasing + letter
    return phrasing

print(turn(input("put your words: ")))