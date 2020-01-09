import requests

from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"
response = requests.get(url)
#print(response)

html_content = response.content
soup = BeautifulSoup(html_content,"html.parser")

raterank = float(input("Please input Rating"))


titleList = soup.find_all("td",{"class":"titleColumn"})
ratingList = soup.find_all("td",{"class":"ratingColumn imdbRating"})

#print(len(titleList),len(ratings))

for title,rating in zip(titleList,ratingList):
    title = title.text
    rating = rating.text

    title = title.strip()
    title = title.replace("\n","")
    rating = rating.strip()
    rating = rating.replace("\n","")

    if(float(rating) >= raterank):
        print("Film name: {} Film Rating: {}".format(title,rating))
        