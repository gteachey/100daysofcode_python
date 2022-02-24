import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

movies = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movies.reverse()
with open("movies.txt", "w") as file:
    [file.write(f"{title}\n") for title in movies]
