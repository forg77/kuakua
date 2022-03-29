import random
import re
import time

import requests
from lxml import etree

cookie = [{'cookie':'bid=YNFImMpeG1Y; douban-fav-remind=1; __yadk_uid=QB5KHPQw8n9Lqf9fKmkLBzhKsWYHeLNU; gr_user_id=97dedbb0-2533-41b0-b770-7321bd78d798; __gads=ID=7a72ccf2777a5a07-22cf779227cf00fa:T=1637320207:RT=1637320207:S=ALNI_MaYh3KIGNTxSB7SY7RpkNYoJa3KdQ; viewed="30391722_35044046"; _ga=GA1.2.1990689400.1636790620; ll="118172"; push_doumail_num=0; push_noty_num=0; __utmc=30149280; __utmz=30149280.1648348643.15.14.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ct=y; apiKey=; __utmv=30149280.20218; _pk_ses.100001.8cb4=*; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1648365668%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DhSvfkdi3OEv6zPSo39JPgMqsX1eToWMEE8ENPgCdVzARoPieudFj6H1l3GKPohVoYIbKKYAzJAVKCZ8wFW790q%26wd%3D%26eqid%3D91deb15c003b5d9a00000005623fcdc4%22%5D; __utma=30149280.1990689400.1636790620.1648355104.1648365669.18; __utmt=1; _pk_id.100001.8cb4=ac3a635777ad4e76.1632644786.12.1648367042.1648360190.; __utmb=30149280.14.9.1648367042621; dbcl2="254006760:ijbZuGvz0TA"'},
          {'cookie':'bid=YNFImMpeG1Y; douban-fav-remind=1; __yadk_uid=QB5KHPQw8n9Lqf9fKmkLBzhKsWYHeLNU; gr_user_id=97dedbb0-2533-41b0-b770-7321bd78d798; __gads=ID=7a72ccf2777a5a07-22cf779227cf00fa:T=1637320207:RT=1637320207:S=ALNI_MaYh3KIGNTxSB7SY7RpkNYoJa3KdQ; viewed="30391722_35044046"; _ga=GA1.2.1990689400.1636790620; ll="118172"; push_doumail_num=0; push_noty_num=0; __utmc=30149280; __utmz=30149280.1648348643.15.14.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ct=y; apiKey=; dbcl2="202189002:wQEnUCyKcpk"; ck=TZM2; __utmv=30149280.20218; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1648365668%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DhSvfkdi3OEv6zPSo39JPgMqsX1eToWMEE8ENPgCdVzARoPieudFj6H1l3GKPohVoYIbKKYAzJAVKCZ8wFW790q%26wd%3D%26eqid%3D91deb15c003b5d9a00000005623fcdc4%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1990689400.1636790620.1648355104.1648365669.18; _pk_id.100001.8cb4=ac3a635777ad4e76.1632644786.12.1648366911.1648360190.; __utmt=1; __utmb=30149280.9.9.1648366911038'}]
class spider:
    def __init__(self):
        self.contenturl = 'https://www.douban.com/group/kuakua/discussion?start='
        self.url_list = []
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.115'}

    def run(self,pages):
        #url_collector
        for i in range(135,pages):
            writeurl = open('url_path.txt', 'a', encoding='utf-16')
            writecontent = open('content.txt', 'a', encoding='utf-16')
            page_url = self.contenturl + str(i*30)
            cookie_random = random.randint(0,1)
            sleep_time = random.randint(1,4)
            get_page = requests.get(page_url,headers=self.headers,cookies=cookie[0])
            get_page = get_page.content.decode()
            toTree = etree.HTML(get_page)
            first_step = toTree.xpath('//td[@class="title"]/a//text()')
            urls = toTree.xpath('//td[@class="title"]/a//@href')

            #print(urls)
            lenf = len(first_step)
            print(lenf)
            for i in range(0,lenf):
                writeurl.write(urls[i])
                writeurl.write('\n')
                solution = first_step[i]
                solution = solution.replace('\n','')
                solution = solution.split()
                writecontent.writelines(solution)
                writecontent.write('\n')

            writecontent.close()
            writeurl.close()
            time.sleep(sleep_time)
            #print(first_step)

newspd = spider()
newspd.run(2000)