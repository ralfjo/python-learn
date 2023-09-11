# API
# Example
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

if response.status_code != 200:
    raise Exception("Error from server")

response.raise_for_status()

payload = response.json()

print(payload)

# what is response status code?
# 1XX : Informational responses
# 2XX : Successful responses
# 3XX : Redirection responses
# 4XX : Client error responses
# 5XX : Server error responses

# 200 OK
# 403 Forbidden - not have access right
# 404 Not Found
# 503 Service unavailable
# 504 Gateway Timeout
