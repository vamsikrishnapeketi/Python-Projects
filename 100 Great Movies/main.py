from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text

soup = BeautifulSoup(data, "lxml")

new_list = []

for movie in soup.find_all(name="h3", class_="title"):
    m = movie.getText()
    new_list.append(m)


l = [i for i in new_list[len(new_list)-1: 0: -1]]

with open("movies.txt",mode="w",encoding="utf-8") as file:
    for item in l:    
        file.write(f"{item}\n")
