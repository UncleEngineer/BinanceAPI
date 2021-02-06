from binance.client import Client
import time
from pprint import pprint
import configapi2

#import configapi2
#print(configapi2.API_KEY)

api_key = configapi2.API_KEY
api_secret = configapi2.SECRET_KEY
client = Client(api_key, api_secret)

'''
order = client.order_limit_buy(
    symbol='DOGEUSDT',
    quantity=450,
    price='0.03')

pprint(order)
'''


# 215750186
'''
result = client.cancel_order(
    symbol='DOGEUSDT',
    orderId=215750186)

print(result)
'''

orders = client.get_all_orders(symbol='DOGEUSDT')
#orders = client.get_open_orders(symbol='DOGEUSDT')
print('ALL ORDER:',orders)
