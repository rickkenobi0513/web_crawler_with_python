from csv import DictReader
import csv
import requests
from bs4 import BeautifulSoup
from random import choice

def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def start_game(q):
    quotes = choice(q)
    remain = 4
    print("Here's a quote:")
    print(quotes["text"])
    guess = ''
    your_name = input(f"What's your name?: ")
    while guess.lower() != quotes["author"].lower() and remain > 0:
        guess = input(f"Remain chances :{remain}  Who said this quote?: \n")
        if guess.lower() == quotes["author"].lower():
            print(f"That's right,{your_name}.")
            break
        remain -= 1
        if remain == 3:
            res = requests.get(f"{orin_url}{quotes['link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth = soup.find(class_="author-born-date").get_text()
            place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint:Author is born on {birth} {place}")
        elif remain == 2:
            first = quotes["author"][0]
            print(f"Here's another hint:Author's first name starts with {first}")
        elif remain == 1:
            last = quotes["author"].split(" ")[1][0]
            print(f"Last chance~~~Author's last name starts with {last} ") 
        else:
            print("You're out of chances,Sucker!!!")
            print(f"The answer was :{quotes['author']}")
            print(f"Nice try,{your_name}")   
    again = ''
    while again.lower() not in ('y','yes','no','n'):
        again = input("Would you like to go again? y/n: \n")
    if again.lower() in ('y','yes'):
        print("OK")
        return start_game(q)
    else:
        print("bye")
q = read_quotes("quote.csv") 
start_game(q)