import os
import time
import threading
import datetime
import crawling.Crawling as Crawling
from models.Article import Article

loop = False
url = 'https://cafe.naver.com/ArticleList.nhn?search.clubid=19480246&search.menuid=24'
interval = 60 #second
datas = {}
users = {}

def workThread():
    while loop:
        now = datetime.datetime.now().date()
        now = datetime.datetime(now.year, now.month, now.day)

        result = Crawling.collect(url)

        for item in result:
            if item.number not in datas and item.date >= now:
                datas[item.number] = item

                if item.name not in users:
                    users[item.name] = 1
                else:
                    users[item.name] += 1


        time.sleep(interval)

def printThread():
    t = datetime.datetime.now().date()
    t = datetime.datetime(t.year, t.month, t.day)
    t = t + datetime.timedelta(0, 3600 * 24)

    while loop:
        now = datetime.datetime.now()
        
        if now >= t:
            file = open(now.strftime("%Y%m%d_%H%M%S") + ".txt", "w")

            for item in datas.values():
                file.write(item.toString() + "\n")

            for user in users.keys():
                file.write("{0}\t{1}\n".format(user, users[user]))

            file.close()

            t = now

        time.sleep(interval)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

wt = threading.Thread(name = "workThread", target = workThread)
pt = threading.Thread(name = "printThread", target = printThread)

loop = True

wt.start()
pt.start()
