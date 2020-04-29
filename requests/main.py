import requests



def get_local_api():

    url = "http://127.0.0.1:8000/"
    r = requests.get(url)
    print(r.json())

def get_remote_api(coin):
    url = "http://api.hbdm.com/market/history/kline?period=1day&size=1&symbol="+coin
    r = requests.get(url)
    print(r.json())
    print(r.json()["data"][0]["close"])

if __name__ == "__main__":
    # get_local_api()
    get_remote_api("BTC_CQ")

