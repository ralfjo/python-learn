from pykrx import stock
import pandas as pd
from datetime import datetime

# 데이터를 저장할 데이터프레임 생성
all_data = pd.DataFrame()

# 사용자로부터 날짜 범위 입력 받기
start_date = input("시작일을 입력하세요 (YYYY-MM-DD): ")
end_date = input("종료일을 입력하세요 (YYYY-MM-DD): ")

# 날짜 범위 생성
date_range = pd.date_range(start=start_date, end=end_date)

# 각 날짜에 대해 데이터 가져오기
for date in date_range:
    date_str = date.strftime("%Y-%m-%d")
    try:
        df = stock.get_market_cap_by_ticker(date_str)
        
        # 데이터가 비어있거나 모든 값이 0인 경우 건너뛰기
        if df.empty or (df == 0).all().all():
            print(f"No data or all zeros on {date_str}. Skipping...")
            continue
        
        # 티커 코드를 종목명으로 변환하여 추가
        df['종목명'] = df.index.map(lambda x: stock.get_market_ticker_name(x))
        df['날짜'] = date_str  # 날짜 정보 추가
        all_data = pd.concat([all_data, df])
    except Exception as e:
        print(f"Error on {date_str}: {e}")

# 데이터 확인
print(all_data)

# 파일로 저장
file_name = f"krx_data_{start_date}_to_{end_date}.xlsx"
all_data.to_excel(file_name, index=True)  # 티커 코드를 인덱스로 저장
print(f"KOSPI & KOSDAQ Market Cap Data from {start_date} to {end_date} saved to {file_name}")