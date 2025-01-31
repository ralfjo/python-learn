import requests
import pandas as pd
import glob
from datetime import datetime

def get_stock_data(market, page=1):
    url = f"https://finance.naver.com/sise/sise_market_sum.nhn?sosok={market}&page={page}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.encoding = "euc-kr"
    tables = pd.read_html(response.text)
    df = tables[1].dropna(how='all')
    
    # 전일비 컬럼을 '변동 방향'과 '변동 금액'으로 분리
    if "전일비" in df.columns:
        df[["전일대비", "전일대비변화"]] = df["전일비"].astype(str).str.split(" ", n=1, expand=True)
        df["전일대비변화"] = df["전일대비변화"].str.replace(",", "").astype(float)
        
        # '보합0'일 경우 Change Direction = '보합', Change Amount = 0으로 설정
        df.loc[df["전일대비"] == "보합0", "전일대비"] = "보합"
        df.loc[df["전일대비"] == "보합", "전일대비변화"] = 0.0
        
        df = df.drop(columns=["전일비"])
    
    return df

def get_all_stock_data(market):
    all_data = pd.DataFrame()
    for page in range(1, 40):  # 40페이지까지 순회 (코스피/코스닥 전체 종목 수 고려)
        try:
            df = get_stock_data(market, page)
            all_data = pd.concat([all_data, df], ignore_index=True)
        except Exception as e:
            print(f"Error on page {page} for market {market}: {e}")
            break
    return all_data

def merge_excel_files(output_filename="merged_stock_data.xlsx"):
    files = glob.glob("kospi_kosdaq_data_*.xlsx")
    all_data = pd.DataFrame()
    
    for file in files:
        df = pd.read_excel(file)
        df["Date"] = file.split("_")[-1].replace(".xlsx", "")
        all_data = pd.concat([all_data, df], ignore_index=True)
    
    all_data.to_excel(output_filename, index=False)
    print(f"Merged data saved to {output_filename}")

if __name__ == "__main__":
    date_input = datetime.today().strftime("%Y-%m-%d")
    
    kospi_data = get_all_stock_data(0)  # 코스피
    kosdaq_data = get_all_stock_data(1)  # 코스닥
    
    all_data = pd.concat([kospi_data, kosdaq_data], ignore_index=True)
    file_name = f"kospi_kosdaq_data_{date_input}.xlsx"
    all_data.to_excel(file_name, index=False)
    print(f"KOSPI & KOSDAQ Closing Data saved to {file_name}")
    
    # 기존 데이터를 하나의 엑셀 파일로 병합
    merge_excel_files()
