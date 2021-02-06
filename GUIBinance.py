from tkinter import *

#########################
from binance.client import Client
from pprint import pprint
import time

api_key = 'VN4aWcnxQzBqRhcMJ7SwKWavIs1goZDcLQ8oSx9s2WnA7ztpYgqosJkymEc1xogF'
api_secret = 'fNYc0CWm9CYPhBo7rTcX5RfV7MNsMIivcrdYHYycdQCFmrQ0U67vwgKHnuW2zcNO'

client = Client(api_key, api_secret)

# info = client.get_account()
# pprint(info)

doge = client.get_asset_balance(asset='DOGE')
usdt = client.get_asset_balance(asset='USDT')

#print('DOGE:', doge)
#print('USDT:', usdt)

text_doge = '{} : {} (In order: {}) '.format(doge['asset'],doge['free'],doge['locked'])
text_usdt = '{} : {} (In order: {}) '.format(usdt['asset'],usdt['free'],usdt['locked'])
alltext = text_doge + '\n' + text_usdt


def UpdatePrice():
    prices = client.get_all_tickers()
    current_price = ''
    coin_name = 'DOGEUSDT'
    for p in prices:
        if p['symbol'] == coin_name:
            current_price = p
        
    #print(current_price)
    time.sleep(0.2)
    #{'symbol': 'DOGEUSDT', 'price': '0.05024810'}
    v_current.set('{} : {}'.format(current_price['symbol'],current_price['price']))
    R1.after(100,UpdatePrice)
    


#########################
GUI = Tk()
GUI.geometry('700x300')
GUI.title('โปรแกรมจัดการเหรียญ Crypto by Uncle Engineer')

FONT1 = ('Angsana New',30)
FONT2 = ('Impact',40)

L = Label(GUI,text='ยอดเงินของฉัน',font=FONT1)
L.pack()

v_balance = StringVar()
v_balance.set(alltext)

BL = Label(GUI,textvariable= v_balance, font=FONT1,fg='green')
BL.pack()

v_current = StringVar()

R1 = Label(GUI,textvariable= v_current, font=FONT2)
R1.pack()

UpdatePrice()

GUI.mainloop()
