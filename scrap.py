import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_date.csv", "w") as csv_file:
    csvwriter = writer(csv_file)
    csvwriter.writerow(["title", "link", "date"])
    for a in articles:
        f_tag = a.find("a")
        title = f_tag.get_text()
        href = f_tag["href"]
        date = a.find("time")["datetime"]
        csvwriter.writerow([title, href, date])

    




