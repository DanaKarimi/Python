import requests
from bs4 import BeautifulSoup

r = requests.get("https://tv.filmnet.ir/")

soup = BeautifulSoup(r.text, "html.parser")
s = soup.find_all("h4")


for i in s:
    a = i.text
    print(a)