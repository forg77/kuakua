'''
urlread = open('url_path.txt','r',encoding='utf-16')
titleread = open('content.txt','r',encoding='utf-16')
url_list = str(urlread).split('\n')
title_list = str(titleread).split('\n')
for items in title_list:
'''
import logging
import random

import requests
from lxml import etree
import time

cookie = [{'cookie':'bid=YNFImMpeG1Y; douban-fav-remind=1; __yadk_uid=QB5KHPQw8n9Lqf9fKmkLBzhKsWYHeLNU; gr_user_id=97dedbb0-2533-41b0-b770-7321bd78d798; __gads=ID=7a72ccf2777a5a07-22cf779227cf00fa:T=1637320207:RT=1637320207:S=ALNI_MaYh3KIGNTxSB7SY7RpkNYoJa3KdQ; viewed="30391722_35044046"; _ga=GA1.2.1990689400.1636790620; ll="118172"; push_doumail_num=0; push_noty_num=0; __utmc=30149280; __utmz=30149280.1648348643.15.14.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ct=y; apiKey=; __utmv=30149280.20218; _pk_ses.100001.8cb4=*; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1648365668%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DhSvfkdi3OEv6zPSo39JPgMqsX1eToWMEE8ENPgCdVzARoPieudFj6H1l3GKPohVoYIbKKYAzJAVKCZ8wFW790q%26wd%3D%26eqid%3D91deb15c003b5d9a00000005623fcdc4%22%5D; __utma=30149280.1990689400.1636790620.1648355104.1648365669.18; __utmt=1; _pk_id.100001.8cb4=ac3a635777ad4e76.1632644786.12.1648367042.1648360190.; __utmb=30149280.14.9.1648367042621; dbcl2="254006760:ijbZuGvz0TA"'},
          {'cookie':'bid=IXZRzfLtfGM; dbcl2="202189002:IpKbvtBsLUs"; ck=D7Xn; douban-fav-remind=1; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1648379593%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; __utma=30149280.1656006039.1648379593.1648379593.1648379593.1; __utmc=30149280; __utmz=30149280.1648379593.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmv=30149280.20218; __yadk_uid=H1RXpl3U37jpZtJE2aqKiO181SdCc1hS; _pk_id.100001.8cb4=7b35a56e657f284a.1648379593.1.1648379865.1648379593.; __utmb=30149280.25.7.1648379853330'},
          {'cookie':'bid=YNFImMpeG1Y; douban-fav-remind=1; __yadk_uid=QB5KHPQw8n9Lqf9fKmkLBzhKsWYHeLNU; gr_user_id=97dedbb0-2533-41b0-b770-7321bd78d798; __gads=ID=7a72ccf2777a5a07-22cf779227cf00fa:T=1637320207:RT=1637320207:S=ALNI_MaYh3KIGNTxSB7SY7RpkNYoJa3KdQ; viewed="30391722_35044046"; _ga=GA1.2.1990689400.1636790620; ll="118172"; push_doumail_num=0; push_noty_num=0; __utmc=30149280; __utmz=30149280.1648348643.15.14.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ct=y; apiKey=; dbcl2="202189002:wQEnUCyKcpk"; ck=TZM2; __utmv=30149280.20218; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1648365668%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DhSvfkdi3OEv6zPSo39JPgMqsX1eToWMEE8ENPgCdVzARoPieudFj6H1l3GKPohVoYIbKKYAzJAVKCZ8wFW790q%26wd%3D%26eqid%3D91deb15c003b5d9a00000005623fcdc4%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1990689400.1636790620.1648355104.1648365669.18; _pk_id.100001.8cb4=ac3a635777ad4e76.1632644786.12.1648366911.1648360190.; __utmt=1; __utmb=30149280.9.9.1648366911038'}]
urlread = open('url_path.txt','r',encoding='utf-16')

class solver:
    def __init__(self):

        self.url_list = []
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52'}
    def run(self):
        while True:
            weburl = urlread.readline()[:-1]
            #print(weburl)
            if not weburl:
                break
            contentwrite = open('ans_content.txt', 'a', encoding='utf-16')
            get_page = requests.get(weburl, headers=self.headers, cookies=cookie[1])
            print(get_page)
            get_page = get_page.content.decode()
            toTree = etree.HTML(get_page)
            first_step = toTree.xpath('//div[@class="reply-doc content"]/p/text()')
            lenf = len(first_step)

            ans_list = []
            if lenf > 3:
                ans_list = first_step[:3]
            else:
                ans_list = first_step
            writestr = ''

            for items in ans_list:
                items.replace('\n','')
                writestr += items + '##'
            writestr += '*&\n'
            contentwrite.write(writestr)
            sleeptime = random.randint(1,4)
            time.sleep(sleeptime)
            contentwrite.close()


solver = solver()
solver.run()