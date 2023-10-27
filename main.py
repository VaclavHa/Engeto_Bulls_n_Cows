import random
import string

"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

Bulls and Cows

author: Václav Hanzl
email: hanzlvaclav00@gmail.com
discord: Wencour#6130 / Vašek H. (Engeto server)
"""



splitter = '-' * 50

print("Hi there!")
print(splitter)


def get_random_number(): ### Get 4 digits unique number
    
    first_number = random.randint(1, 9)
    last_three_numbers = [random.randint(0, 9) for number in range(3)]
    unique_number = [first_number] + last_three_numbers
    random_number_str = "".join(map(str, unique_number))
    
    