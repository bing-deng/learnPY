import requests
import time

class Exam():

    def __init__(self, filename):
        self.filename = filename

    def post(self, answer):
        lines = open(self.filename,'r')
        self.tel("3s后开始测试")
        time.sleep(3)
        for index,i in enumerate(lines):
            if answer or index % 2 == 0:
                self.tel(i)
            time.sleep(5)
        self.tel("考试结束")


    def tel(self, msg):

        url = "https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s" % (
            "939159598:AAGGZscNysWO_bPOud5CiQKrBFjYnZSDaXQ",'-1001306413068',msg)
        param = {"chat_id": "-1001306413068", "text": msg }
        print(url)
        try:
            result = requests.get(url, param, timeout=20)
        except Exception as e:
            print(str(e))



if __name__ == "__main__":
    e = Exam('question.txt')
    e.post(answer=True)

