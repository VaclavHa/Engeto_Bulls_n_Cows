"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

Bulls and Cows

author: Václav Hanzl
email: hanzlvaclav00@gmail.com
discord: Wencour#6130 / Vašek H. (Engeto server)
"""

import random
from datetime import datetime

splitter = ('-' * 50)
double_splitter = ("=" * 50)

print("Hi there!")
print(splitter)


#############  Get 4 digits unique number  #############

def get_random_number(): 

    digits = random.sample(range(1, 10), 1) + random.sample(range(0, 10), 3)
    while len(set(digits)) != 4:
        continue
    else:
        secret_number = "".join(map(str, digits))
        print("I've generated a random 4 digit number for you to guess."
            "Let's play Bulls and Cows game!")
        print(splitter)
    return secret_number

#############  Compare values, get bulls or cows  #############

def compare_values(secret, guess):

    bulls = 0
    cows = 0
    
    for s_char, g_char in zip(secret, guess):
        if s_char == g_char:
            bulls += 1
            
    for s_char in secret:
        if s_char in guess:
            cows += 1
        
    cows -= bulls
            
    return bulls, cows
            

#############  Guess the number, conditions of guessing  #############

def guess_number():
    
    guessed_number = get_random_number()
    guess_counter = 0
    
    start_time = None
    
    while True:
        
        
        user_guess = input("Enter a number: ")
        
        if not start_time:
            start_time = datetime.now()
        
        guess_counter += 1
        
        if len(user_guess) != 4:
            print("Your number doesn't consist of 4 digits. Try again")
            print(splitter)
            continue
        
        if len(set(user_guess)) != 4:
            print("The number must consist of UNIQUE digits. Try again")
            print(splitter)
            continue
            
        if user_guess[0] == "0":
            print("The number MUST NOT start with 0. Try again")
            print(splitter)
            continue
            
        if not user_guess.isdigit():
            print("The guess must conssit ONLY digits. Try again")
            print(splitter)
            continue
        
        bulls, cows = compare_values(guessed_number, user_guess)
        
 #############  Result check  #############
    
        if bulls == 4:
            print(double_splitter, "\n")
            end_time = datetime.now()
            elapsed_time = (end_time - start_time)
            print(f"Correct, you've guessed the right number {user_guess}!\n")
            print(f"It took you {guess_counter} guesses!\n")
            print(f"Also it took you {elapsed_time}\n")
            print(double_splitter)        
            break
        
        else:
            
            if bulls == 1:
                bull_note = "bull"
            else:
                bull_note = "bulls"
                
            if cows == 1:
                cow_note = "cow"
            else:
                cow_note = "cows"
                
            print(f"You got {bulls} {bull_note} and {cows} {cow_note}")
            print(splitter)
            
if __name__ == "__main__":
    guess_number()