from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url =f"https://www.billboard.com/charts/hot-100/{date}/"

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0', ## the website need to check the user agent to make sure its not a bot
    'Referer': 'https://www.billboard.com/' ## also it needs a referer to the base site
}
response = session.get(url=url, headers=headers)
response.raise_for_status() ## we use this to stop the code if the respons code is not 200

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)