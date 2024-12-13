from bs4 import BeautifulSoup
import requests
# import lxml
# from charset_normalizer import from_path

# result = from_path("website.html")
# print(result.best().encoding)

# with open("website.html", "r", encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)

# # print(soup.prettify())

# # print(soup.a)
# # print(soup.p)
# all_anchor_tags = soup.find_all(name="a")

# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)
# print(section_heading.get("class"))

# company_url = soup.select_one(selector="p a")
# print(company_url)


# https://news.ycombinator.com/news
# https://appbrewery.github.io/news.ycombinator.com/
# https://gist.github.com/TheMuellenator/941a8d6bfc555dbc7c939d2c3720a87d
# https://gist.github.com/TheMuellenator/181821980a1788aec82c254f39da63ac

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# article_tag = soup.find(name="span", class_="titleline")
# article_tag = soup.select_one(".titleline a")
# # article_tag = span_tag.find(name="a")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()

# print(article_tag)
# print(article_text)
# print(article_link)
# print(article_upvote)


articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []
for span_tag in articles:
    article_tag = span_tag.find(name="a")
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

# print(article_texts)
# print(article_links)
# print(article_upvotes)
# print(int(article_upvotes[0].split()[0]))