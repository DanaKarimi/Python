import requests
from bs4 import BeautifulSoup

r = requests.get("https://karnameh.com/car-price")
soup = BeautifulSoup(r.text,"html.parser")
carsName_s = soup.find_all(class_="MuiTypography-root MuiTypography-body1 muirtl-iy5bpq")
price_s = soup.find_all(class_="MuiTypography-root MuiTypography-body1 muirtl-22intj")

carsName = []
price = []
for i in carsName_s:
    carsName.append(i.text)

for i in price_s:
    price.append(i.text)
i = 0
while i < len(carsName):
    print(carsName[i], ":", price[i])
    i = 1 + i