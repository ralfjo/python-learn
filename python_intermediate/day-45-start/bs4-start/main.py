from bs4 import BeautifulSoup
# import lxml
# from charset_normalizer import from_path

# result = from_path("website.html")
# print(result.best().encoding)

with open("website.html", "r", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.a)
# print(soup.p)
all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url)

