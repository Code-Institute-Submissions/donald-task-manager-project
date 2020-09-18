import time

country_data = open("country_data.storage", "+r")
country_change = open("country_data.storage", "+a")

addcountry_response = ["add a new country", "add country", "country add", "new country", "add new country", "add a new country.", "add country.", "country add.", "new country.", "add new country."]
readcountry_response = ["read countries", "read country", "view countries", "view country", "see countries", "see country.", "view countries"]
leavemode_response = ["exit mode", "exit", "leave mode", "leave", "finish mode", "finish"]


def nationscore_better():
    for i in range(1, 2):
        print("#")


def lead():
    nationscore_better()
    state = input("Do you have the option to see the country? If you want to leave then use 'exit'")
    state = str(state)

    if state in addcountry_response:
        nationscore_better()
        print("Please enter the country details")

        country = input("Country: ")
        country = str(country)
        dial_code = input("Dial code: ")
        dial_code = str(dial_code)
        population = input("Population: ")
        population = str(population)
        continent = input("Continent: ")
        continent = str(continent)
        square_area = input("Square area: ")
        square_area = str(square_area)

        entry = (country + " - " + dial_code + " - " + population + " - " + continent + " - " + square_area)
        entry = str(entry)

        country_change.write(entry)
        country_change.write("\n")
        print("Country added>>>>" + entry)

    elif state in readcountry_response:
        country_data = open("country_data.storage", "+r")

        nationscore_better()

        countries = country_data.read()
        countries = str(countries)

        print(countries)

    elif state in leavemode_response:
        exit()

    else:
        print("This country is not known.")

continuation = True
while continuation:
    time.sleep(1)
    nationscore_better()
    lead()

