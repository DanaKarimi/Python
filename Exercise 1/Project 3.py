import requests
from bs4 import BeautifulSoup

r = requests.get("https://takhfifan.com/tehran/restaurants-cafes")
soup = BeautifulSoup(r.text,"html.parser")

cafeName_s = soup.find_all(class_="vendor-card-box__title-text")
rate_s = soup.find_all(class_="rate-badge__rate-value")

cafename = []
rate = []

for i in cafeName_s:
    cafename.append(i.text)
for i in rate_s:
    rate.append(i.text)

i = 0
cafeName_rate = {}
while i < len(rate):
    cafeName_rate.update({cafename[i]:rate[i]})
    i = 1 + i

cafeName_rate_sorted = dict(sorted(cafeName_rate.items(), key=lambda item: item[1], reverse=True))

cafename2 =[]
rate2 = []
for i in cafeName_rate_sorted.values():
    cafename2.append(i)
for i in cafeName_rate_sorted.keys():
    rate2.append(i)

i = 0
while i < len(cafename2):
    print(cafename2[i], ":", rate2[i])
    i = 1 + i
