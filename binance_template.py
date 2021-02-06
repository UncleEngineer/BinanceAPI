from binance.client import Client

from pprint import pprint

api_key = 'VN4aWcnxQzBqRhcMJ7SwKWavIs1goZDcLQ8oSx9s2WnA7ztpYgqosJkymEc1xogF'
api_secret = 'fNYc0CWm9CYPhBo7rTcX5RfV7MNsMIivcrdYHYycdQCFmrQ0U67vwgKHnuW2zcNO'

client = Client(api_key, api_secret)

# info = client.get_account()
# pprint(info)

doge = client.get_asset_balance(asset='DOGE')
usdt = client.get_asset_balance(asset='USDT')

print('DOGE:', doge)
print('USDT:', usdt)
