import requests

def get_market_cap(symbol):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[symbol]['usd_market_cap']

def calculate_market_cap_ratio(symbol1, symbol2):
    market_cap1 = get_market_cap(symbol1)
    market_cap2 = get_market_cap(symbol2)
    ratio = (market_cap1 / (market_cap1 + market_cap2)) * 100
    return ratio

if __name__ == "__main__":
    symbol1 = 'bitcoin'
    symbol2 = 'ethereum'
    ratio = calculate_market_cap_ratio(symbol1, symbol2)
    print(f"{symbol1.upper()}市值占比：{ratio:.2f}%")
    print(f"{symbol2.upper()}市值占比：{100 - ratio:.2f}%")
