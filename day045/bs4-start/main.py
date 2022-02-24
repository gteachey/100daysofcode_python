import requests
from bs4 import BeautifulSoup

#

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

titles = soup.find_all(name="a", class_="titlelink")
article_links = []
article_titles = []

for title in titles:
    text = title.getText()
    article_titles.append(text)
    link = title.get("href")
    article_links.append(link)

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
# print(article_titles)
# print(article_links)
# print(article_upvotes)

scores = [score.split()[0] for score in article_upvotes]
highest_score = scores[0]
index = 0
score_index = 0
for score in scores:
    if int(score) > int(highest_score):
        highest_score = score
        score_index = index
    index += 1

print(f"{highest_score} Index: {score_index}")
print(f"Title: {article_titles[score_index]}\nLink: {article_links[score_index]}")

# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# #print(contents)
# soup = BeautifulSoup(contents, 'html.parser')
# #print(soup.title)
# #print(soup.title.name)
# #print(soup.prettify())
#
# #print(soup.p)
#
# all_anchor_tags = soup.findAll(name="a")
# #print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
#     #print(tag.getText())
#     #print(tag.get("href"))
#
# # heading = soup.find("h1", id="name")
# # print(heading)
# #
#
#
# # class_is_heading = soup.find_all(class_="heading")
# # print(class_is_heading)
# #
# # h3_heading =  soup.find_all("h3", class_="heading")
# # print(h3_heading)
#
# # company_url = soup.select_one(selector="p a")
# # print(company_url)
#
# # company_url = soup.select_one(selector="#name") # Select by ID
# # print(company_url)
#
# heading = soup.select(selector=".heading") # Select by Class
# print(heading)
