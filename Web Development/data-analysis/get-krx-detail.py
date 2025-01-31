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
        # 1. 시가총액 및 가격 정보 가져오기
        df_cap = stock.get_market_cap_by_ticker(date_str)
        
        # 데이터가 비어있거나 모든 값이 0인 경우 건너뛰기
        # if df_cap.empty or (df_cap == 0).all().all():
        #     print(f"No data or all zeros on {date_str}. Skipping...")
        #     continue
        
        # 2. 종목명 추가
        df_cap['종목명'] = df_cap.index.map(lambda x: stock.get_market_ticker_name(x))
        
        # 3. 가격 정보 (시가, 고가, 저가, 종가, 거래량) 가져오기
        df_ohlcv = stock.get_market_ohlcv_by_ticker(date_str)
        
        # 중복 컬럼 제거 (종가, 거래량은 df_ohlcv에서 사용)
        df_cap = df_cap.drop(columns=['종가', '거래량'], errors='ignore')
        
        # 두 데이터프레임 병합
        df_cap = df_cap.join(df_ohlcv[['시가', '고가', '저가', '종가', '거래량']])
        
        # 4. PER, PBR, EPS, BPS, 배당률 가져오기
        df_fundamental = stock.get_market_fundamental_by_ticker(date_str)
        df_cap = df_cap.join(df_fundamental[['PER', 'PBR', 'EPS', 'BPS', 'DIV', 'DPS']])
        
        # 5. 외국인 보유 비율 가져오기
        df_foreign = stock.get_exhaustion_rates_of_foreign_investment_by_ticker(date_str)
        df_cap = df_cap.join(df_foreign[['한도소진률']])
        df_cap.rename(columns={'한도소진률': '외국인보유비율'}, inplace=True)
        
        # 6. 날짜 정보 추가
        df_cap['날짜'] = date_str
        
        # 전체 데이터프레임에 추가
        all_data = pd.concat([all_data, df_cap])
    except Exception as e:
        print(f"Error on {date_str}: {e}")

# 데이터 확인
print(all_data)

# 날짜 및 티커를 기준으로 정렬 (순서 유지)
all_data = all_data.sort_values(by=["티커", "날짜"])

# 시가총액 변화량 추가
all_data["시가총액변화"] = all_data.groupby("티커")["시가총액"].diff()
all_data["시가총액변화율(%)"] = (all_data["시가총액변화"] / all_data["시가총액"].shift(1)) * 100
all_data["시가총액변화(1주)"] = all_data.groupby("티커")["시가총액"].diff(periods=5)
all_data["시가총액변화율(1주)(%)"] = (all_data["시가총액변화(1주)"] / all_data["시가총액"].shift(5)) * 100
all_data["시가총액변화(1달)"] = all_data.groupby("티커")["시가총액"].diff(periods=20)
all_data["시가총액변화율(1달)(%)"] = (all_data["시가총액변화(1달)"] / all_data["시가총액"].shift(20)) * 100

# 거래량 변화량 추가
all_data["거래량변화"] = all_data.groupby("티커")["거래량"].diff()
all_data["거래율(%)"] = (all_data["거래량변화"] / all_data["상장주식수"]) * 100  # 거래량 변화율 (%)
all_data["거래량변화율(%)"] = (all_data["거래량변화"] / all_data["상장주식수"]) * 100  # 거래량 변화율 (%)
all_data["거래량변화(1주)"] = all_data.groupby("티커")["거래량"].diff(periods=5)
all_data["거래량변화율(1주)(%)"] = (all_data["거래량변화(1주)"] / all_data["상장주식수"]) * 100
all_data["거래량변화(1달)"] = all_data.groupby("티커")["거래량"].diff(periods=20)
all_data["거래량변화율(1달)(%)"] = (all_data["거래량변화(1달)"] / all_data["상장주식수"]) * 100

# 종가 변화량 추가
all_data["종가변화"] = all_data.groupby("티커")["종가"].diff()
all_data["종가변화율(%)"] = (all_data["종가변화"] / all_data["종가"].shift(1)) * 100  # 종가 변화율 (%)
all_data["종가변화(1주)"] = all_data.groupby("티커")["종가"].diff(periods=5)
all_data["종가변화율(1주)(%)"] = (all_data["종가변화(1주)"] / all_data["종가"].shift(5)) * 100
all_data["종가변화(1달)"] = all_data.groupby("티커")["종가"].diff(periods=20)
all_data["종가변화율(1달)(%)"] = (all_data["종가변화(1달)"] / all_data["종가"].shift(20)) * 100

# 외국인 보유 비율 변화량 추가
all_data["외국인보유비율변화"] = all_data.groupby("티커")["외국인보유비율"].diff()
all_data["외국인보유비율변화(1주)"] = all_data.groupby("티커")["외국인보유비율"].diff(periods=5)
all_data["외국인보유비율변화(1달)"] = all_data.groupby("티커")["외국인보유비율"].diff(periods=20)


# 파일로 저장
file_name = f"krx_data_{start_date}_to_{end_date}.xlsx"
all_data.to_excel(file_name, index=True)  # 티커 코드를 인덱스로 저장
print(f"KOSPI & KOSDAQ Data from {start_date} to {end_date} saved to {file_name}")