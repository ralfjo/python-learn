import requests

MY_LAT = 37.532600
MY_LONG = 127.024612

# https://www.webfx.com/web-development/glossary/http-status-codes/
# 1xx: Hold on
# 2xx here you go
# 3xx Go Away
# 4xx You screwed up
# 5xx I screwed up
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response = requests.get(url="https://api.kanye.rest")
# response.raise_for_status()

# data = response.json()["quote"]

# print(data)

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)

# print(iss_position)



parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}

response = requests.get("https://api.sunrise-sunset.org/json", verify=False, params=parameters)
response.raise_for_status()
data = response.json()
print(data)

