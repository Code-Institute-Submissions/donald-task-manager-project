import random

class Individual:
    def _init_(self, country, capital, dial_code, population, continent, currency):
        self.country = country
        self.capital = capital
        self.dial_code = dial_code
        self.population = population
        self.continent = continent
        self.currency = currency
    def whole_name(self):
        print(f'{self.country} {self.capital}')
    
    def __str__(self):
        return f"{self.country} {self.capital}: {self.dial_code} {self.population} {self.continent} {self.currency}\n"

print("welcome")
print("please enter your information")

country = input("please enter country = ")
capital = input("please enter country's capital = ")
dial_code = input("please enter the country dial code = ")
population = input("please enter the country's population = ")
continent = input("please enter the country's continent = ")
currency = input("please enter the country's currency = ")

print("thank you for providing the country's information")

the_Country = Individual(country, capital, dial_code, population, continent, currency)
print(the_Country)

