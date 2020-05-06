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
    print(html)
    fo = open("html.txt","w")
    fo.write(str(html))
    bsObj = BeautifulSoup(html,"html.parser")
    info = bsObj.find("meta",  property="og:description")

    arr = str(info).split(' ')
    post_count , following, follows = arr[1].replace('content="','') ,arr[3] ,arr[5]
    print(name,post_count , following, follows)


if __name__ == "__main__":
    
    for i in ['r.t.321']:
        get_data(i)
        time.sleep(1)
   