"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

Bulls and Cows

author: Václav Hanzl
email: hanzlvaclav00@gmail.com
discord: Wencour#6130 / Vašek H. (Engeto server)
"""

import random

splitter = '-' * 50

print("Hi there!")
print(splitter)

guess_counter = 0

### Get 4 digits unique number

def get_random_number(): 
    
    first_number = random.randint(1, 9)
    last_three_numbers = [random.randint(0, 9) for number in range(3)]
    unique_number = [first_number] + last_three_numbers
    secret_number = "".join(map(str, unique_number))
    print("I've generated a random 4 digit number for you to guess."
        "Let's play Bulls and Cows game!")
    
### Guess the number, conditions of guessing

def guess_the_number():
    
    while True:
        
        user_guess = input("Enter a number: ")
        
        
        if len(user_guess) != 4:
            print("Your number doesn't consist of 4 digits. Try again")
            print(splitter)
            continue
        
        if len(set(user_guess)) != 4:
            print("The number must consist of unique digits.")
            print(splitter)
            continue
            
        if user_guess[0] == 0:
            print("The number must not start with 0")
            print(splitter)
            continue
            
        if not user_guess.isdigit():
            print("The guess must conssit ONLY digits.")
            print(splitter)
            continue


        
            
        
        
        
        
        