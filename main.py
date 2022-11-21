

from binance.spot import Spot as Client
import os
from pprint import pprint
import datetime
import math


binance_testnet_api_key=os.environ["BINANCE_API_KEY"]
binance_testnet_secret_key=os.environ["BINANCE_SECRET_KEY"]
base_url="https://api.binance.com" 

client = Client(key=binance_testnet_api_key,secret=binance_testnet_secret_key,base_url=base_url)



def datetime_to_timestamp(year:int,month:int,day:int,hour:int,minute:int,second:int)-> int:
    """convert date to time stamp

    Args:
        year (int): year
        month (int): month
        day (int): day
        hour (int): hour
        minute (int): minute
        second (int): second

    Returns:
        int: timestamp in microseconds
    """
    now = datetime.datetime(year=year,month=month,day=day,hour=hour,minute=minute,second=second)
    timestamp = int((datetime.datetime.timestamp(now)) * 1000)

    return timestamp

def exchange_info_pairs():
    """Abstract all symbol pairs from binance

    Returns:
        Generator: symbol pairs
    """
    exchange_info = client.exchange_info()

    pair_info = exchange_info["symbols"] #array/list

    symbols = []

    for pair in pair_info: # pair is a dictionary
        if pair["quoteAsset"] == "USDT":
            pass
            # print(pair["symbol"]) #trading pair

    symbols = ( pair["symbol"] for pair in pair_info if pair["quoteAsset"] == "USDT" )


    return symbols

def top_10(symbols,starttime)-> dict :
    """Establish the top 10 coins after 8hrs of opening"""

    data_change = {}

    for symbol_index, symbol in enumerate(symbols,1):
        kline = client.klines(symbol, "8h", limit=1, startTime = starttime)
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


    #sort dictionary by value and print the top 10
    top10_dict = {}
    top_10 = sorted(data_change.items(),key=lambda x:x[1],reverse=True)
    for index,i in enumerate(top_10,1):
        if index <= 10:
            top10_dict[i[0]] = i[1]

    print()
    print("TOP 10 COINS")
    print("_________________________________________________________")
    for k,v in enumerate(top10_dict.items(),1):
        print(k,v)
    print("_________________________________________________________")
    print()
    top_10_symbols = [ x for x in top10_dict.keys()]

    return top_10_symbols
    

def trade_8hr(top_10,starttime):

    """Abstract OHCL data after opening trade

    Returns:
        data_change(dict): the symbol and close price after the first 8 hrs
    """
    data_change = {}
    for symbol_index, symbol in enumerate(top_10,1):
        kline = client.klines(symbol, "8h", limit=1, startTime = starttime)
        for data in kline: #kline - 2d list, data -list
            #open_time = datetime.datetime.fromtimestamp(int(data[0]/1000))
            open_time = data[6]/1000
            open = float(data[1])
            high = float(data[2])
            low = float(data[3])
            close = float(data[4])
            #close_time = datetime.datetime.fromtimestamp(int(data[6]/1000))
            close_time = data[6]/1000

            data_change[symbol] = (close)
    
    return data_change
        
def trade_24hr(top_10,starttime):
    data_change = {}
    for symbol_index, symbol in enumerate(top_10,1):
        kline = client.klines(symbol, "1d", limit=1, startTime = starttime)
        for data in kline: #kline - 2d list, data -list
            open_time = datetime.datetime.fromtimestamp(int(data[0]/1000))
            open = float(data[1])
            high = float(data[2])
            low = float(data[3])
            close = float(data[4])
            close_time = datetime.datetime.fromtimestamp(int(data[6]/1000))
            
            data_change[symbol] = (high,low,close)
    
    return data_change

def main(date:int,month:int,year:int):
    # establish top 10 symbols
    
    symbols = exchange_info_pairs()
    starttime = datetime_to_timestamp(year,month,date,3,0,0)
    print("SEARCHING FOR TOP 10 COINS")
    print("_________________________________________________________")
    top_10_symbols = top_10(symbols,starttime)

    # data after selection
    data_8hr = trade_8hr(top_10_symbols,starttime)

    print()
    print("TRACKING THE TOP 10 COINS 24HRS LATER")
    print("_________________________________________________________")

    for x in data_8hr.keys():
        # adjust time to 8hrs after opening
        starttime = datetime_to_timestamp(year,month,date,11,0,0)
        data_24hr = trade_24hr(top_10_symbols,starttime)

        close_8 = data_8hr[x]

        if x in data_24hr.keys():
            high_24,low_24,close_24 = data_24hr[x]
        
        
        print(f"{x}:Entry price :{close_8} <>possible drawdown: {round(((low_24 - close_8)/close_8) * 100,2)} % <> possible profit: {round(((high_24 - close_8)/close_8) * 100,2)} %")


if __name__ == "__main__":
    main(18,11,2021)
