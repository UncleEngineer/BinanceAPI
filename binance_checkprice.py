from binance.client import Client
import time
from pprint import pprint

api_key = 'VN4aWcnxQzBqRhcMJ7SwKWavIs1goZDcLQ8oSx9s2WnA7ztpYgqosJkymEc1xogF'
api_secret = 'fNYc0CWm9CYPhBo7rTcX5RfV7MNsMIivcrdYHYycdQCFmrQ0U67vwgKHnuW2zcNO'

client = Client(api_key, api_secret)



while True:
    prices = client.get_all_tickers()
    current_price = ''
    coin_name = 'DOGEUSDT'
    for p in prices:
        if p['symbol'] == coin_name:
            current_price = p
        
    print(current_price)
    time.sleep(0.2)
    # {'symbol': 'DOGEUSDT', 'price': '0.05024810'}
