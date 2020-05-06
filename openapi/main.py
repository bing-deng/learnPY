from fastapi import FastAPI

from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import time
from datetime import datetime

def get_data(name):

    url = "https://www.instagram.com/" + name
    # print(url)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = Request(url=url, headers=headers)
    html = urlopen(req).read()
    bsObj = BeautifulSoup(html,"html.parser")
    info = bsObj.find("meta",  property="og:description")

    arr = str(info).split(' ')
    post_count , following, follows = arr[1].replace('content="','') ,arr[3] ,arr[5]
    print(name,post_count , following, follows)
    return {"post_count":post_count, "following":following, "follows":follows}

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ins/{item_id}")
def read_item(item_id: str):
    info = get_data(item_id)
    print(info)
    return info
