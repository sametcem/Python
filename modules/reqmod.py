import requests
from bs4 import BeautifulSoup

url = "http://alttab.site/"
response = requests.get(url)

print(response)

html_content = response.content

soup = BeautifulSoup(html_content,"html.parser")
#print(soup.prettify())

for i in soup.find_all("a"):
    print(i)
    print("*********************")
    print(i.get("href"))
    print(i.text)

# print(soup.find_all("div",{"class":"yp-poi-box-2"}))



