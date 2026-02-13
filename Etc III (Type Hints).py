'''
Einstein Mwase
Harvard edX, CS50P Python
https://cs50.edx.org/python
https://home.edx.org/

CS50P Lecture 8 - Etcetera III (Type Hints)
CONTINENT QUIZ
Thursday, 12th February, 2026
'''

#Going to use python, git, and gitHub to create a py file that quizes you about the location of a country
#It should ask the user "Which continent is [Random Country] in?" and then check if the answer is correct,
#given that the user responds by typing out the continent. 
#This code should ignore capitalizations and spaces, 
#So "North America" or "north america" or "Northamerica" or "northamerica", are all be correct for the country "United States of America"
#As an execution of "type hints" from John Mallan

America = ["USA", "Canada", "Mexico", "Brazil", "Argentina"]
Africa = ["Nigeria", "Egypt", "South Africa", "Kenya", "Ethiopia"]
Asia = ["China", "India", "Japan", "South Korea", "Indonesia"]  
Europe = ["United Kingdom", "Germany", "France", "Italy", "Spain"]
Australia = ["Australia", "New Zealand", "Fiji", "Papua New Guinea"]

import random

def continentCheck(country: str):
    country = country.strip().title()  # Remove leading/trailing spaces and capitalize each word
    
    America = ["USA", "Canada", "Mexico", "Brazil", "Argentina"]
    Africa = ["Nigeria", "Egypt", "South Africa", "Kenya", "Ethiopia"]
    Asia = ["China", "India", "Japan", "South Korea", "Indonesia"]  
    Europe = ["United Kingdom", "Germany", "France", "Italy", "Spain"]
    Australia = ["Australia", "New Zealand", "Fiji", "Papua New Guinea"]

    if country in America:
        print( country, "is in America")
    elif country in Africa:
        print( country, "is in Africa") 
    elif country in Asia:
        print( country, "is in Asia")
    elif country in Europe:
        print( country, "is in Europe")
    elif country in Australia:
        print( country, "is in Australia")
    else:
        print("Sorry, ", country, "does not seem to exist in any continent known to me.") 

world = America + Africa + Asia + Europe + Australia
randomCountry = random.choice(world)

continent = input("Which continent is " + randomCountry + " in? ")
continentCheck(randomCountry)

#This code is well and goot but it does not yet:
#1. Check if the user's answer is correct or not, it just tells them which continent the country is in
#2. It does not ignore capitalizations and spaces in the user's answer

#But it does use "type hints", I just need to make that more explicit
