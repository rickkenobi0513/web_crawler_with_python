from csv import DictWriter
import csv
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

orin_url = "http://quotes.toscrape.com"



def scrape_quote():
    allquote = []
    url = "/page/1"
    while url:
        request = requests.get(f"{orin_url}{url}")
        soup = BeautifulSoup(request.text, "html.parser")
        quote = soup.select(".quote")
        
        for q in quote:
            allquote.append({
                "text" : q.find(class_="text").get_text(),
                "author" : q.find(class_="author").get_text(),
                "link" : q.find("a")["href"]
            })
        next = soup.find(class_="next")
        url = next.find("a")["href"] if next else None
        sleep(1)
    return allquote

def write_quote(quotes):
    with open("quote.csv", "w") as file:
        headers = ["text","author","link"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for q in quotes:
            csv_writer.writerow(q)
quotes = scrape_quote()
write_quote(quotes)
