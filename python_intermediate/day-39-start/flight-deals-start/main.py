#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from flight_search import FlightSearch

# Sheety API URL
SHEETY_API_URL = ""  # 여기에 Sheety API URL을 입력하세요.


def fetch_google_sheet_data():
    try:
        # API 호출
        response = requests.get(SHEETY_API_URL)
        response.raise_for_status()  # 에러가 있으면 예외 발생

        # 데이터 출력
        data = response.json()
        # pprint(data)
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"API 호출 중 오류 발생: {e}")
        return None

# 함수 실행
if __name__ == "__main__":
    gsheet_data = fetch_google_sheet_data()
    
    sheet_data = gsheet_data["prices"]
    # pprint(sheet_data)
    
    for data in sheet_data:
        print(data["city"])

