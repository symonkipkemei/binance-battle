

from binance.spot import Spot as Client
import os
from pprint import pprint
import datetime
import math


binance_testnet_api_key=os.environ["BINANCE_API_KEY"]
binance_testnet_secret_key=os.environ["BINANCE_SECRET_KEY"]
base_url="https://api.binance.com" 

client = Client(key=binance_testnet_api_key,secret=binance_testnet_secret_key,base_url=base_url)


def ticker_24hr():
    pprint(client.ticker_24hr("BNBUSDT"))


def ticker_8hr():
    pprint(client.ticker_price("BNBUSDT"))


def rolling_ticker():
    pprint(client.rolling_window_ticker("BNBUSDT", windowSize="7d", type="MINI"))



def trades():
    pprint(client.trades("BNBUSDT", limit=10))



def historical_trades():
    pprint(client.historical_trades("BNBUSDT", limit=10))


def book_ticker():
    pprint(client.book_ticker("BTCUSDT"))


def time():
    pprint(client.time())


def datetime_to_timestamp(year:int,month:int,day:int,hour:int,minute:int,second:int)-> int:
    now = datetime.datetime(year=year,month=month,day=day,hour=hour,minute=minute,second=second)
    timestamp = int((datetime.datetime.timestamp(now)) * 1000)

    return timestamp

def klines(symbols):
    data_change = {}

    for symbol_index, symbol in enumerate(symbols,1):
        kline = client.klines(symbol, "8h", limit=1, startTime = datetime_to_timestamp(2022,11,18,0,00,00))
        for data in kline: #kline - 2d list, data -list
            open_time = datetime.datetime.fromtimestamp(int(data[0]/1000))
            open = float(data[1])
            high = float(data[2])
            low = float(data[3])
            close = float(data[4])
            close_time = datetime.datetime.fromtimestamp(int(data[6]/1000))
            
            momentum  = close - open
            volatility = high - low

            momentum_change = round(((momentum/open) * 100),4)
            volatility_change = round(((volatility/low) * 100),4)

            print (symbol_index,symbol, open_time, close_time,f"mom % :{momentum_change}", f"vol % :{volatility_change}")

            
            data_change[symbol] = (momentum_change,volatility_change)

    return data_change
    

def exchange_info_pairs():
    exchange_info = client.exchange_info()

    pair_info = exchange_info["symbols"] #array/list

    symbols = []

    for pair in pair_info: # pair is a dictionary
        if pair["quoteAsset"] == "USDT":
            pass
            # print(pair["symbol"]) #trading pair

    symbols = ( pair["symbol"] for pair in pair_info if pair["quoteAsset"] == "USDT" )


    return symbols


def main():
    symbols = exchange_info_pairs()

    data_change = klines(symbols)
    #data_change = {"symon": (13,100),"kip": (94,25) ,"nancy":(10,108) ,"lelgo":(60,34)}

    #sort dictionary by value and print the top 10
    top10_dict = {}
    top_10 = sorted(data_change.items(),key=lambda x:x[1],reverse=True)
    for index,i in enumerate(top_10,1):
        if index <= 10:
            top10_dict[i[0]] = i[1]

    
    for k,v in enumerate(top10_dict.items(),1):
        print(k,v)


if __name__ == main():
    main()

