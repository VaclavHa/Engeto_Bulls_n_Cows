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


def get_random_number():
    
    random_number = random.randint(1, 9)
    digits = [1,2,3,4,5,6,7,8,9]
    digits[random_number - 1] = 0
    for i in random.sample(digits, 3):
        random_number = random_number*10 + i
    print(random_number)

get_random_number()
