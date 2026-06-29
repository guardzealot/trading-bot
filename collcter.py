import yfinance as yf
import pandas as pd 

def fetch_stock_data(ticker_symbol):
    print(f"[{ticker_symbol}] 데이터 수집을 시작합니다 . . .")

    stock = yf.Ticker(ticker_symbol)
    df = stock.history(period = "5d", interval = "1d")

    if df.empty:
        print(f"오류 : [{ticker_symbol}] 데이터를 가져오지 못했습니다. 티커를 확인하세요. ")
        return None

    return df

if __name__ == "__main__":
    target_ticker = input(f"티커를 입력하세요.")
    data = fetch_stock_data(target_ticker)

    if data is not None:
        print("\n--- 수집 완료! 최근 데이터 샘플 ---")
        print(data[['Open', 'High', 'Low', 'Close', 'Volume']])    