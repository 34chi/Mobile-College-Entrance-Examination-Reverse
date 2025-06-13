import hashlib
import hmac
import base64
import random
from urllib.parse import unquote
import requests
import re
import time


def w(params):
    sign = params['SIGN']
    s = params['str']
    
    decoded_str = unquote(s)
    
    hmac_sha1 = hmac.new(sign.encode('utf-8'), decoded_str.encode('utf-8'), hashlib.sha1)
    
    base64_str = base64.b64encode(hmac_sha1.digest()).decode('utf-8')

    return s_hash(base64_str)

def s_hash(t):
    return hashlib.md5(t.encode('utf-8')).hexdigest()


for page in range(1, 10):

    with open('掌上高考逆向\\高校.txt','a') as f:

        result = w({
            'SIGN': "D23ABC@#56",
            'str': f'api.zjzw.cn/web/api/?keyword=&page={page}&province_id=&ranktype=&request_type=1&size=20&top_school_id=[57,3238,1569,3269]&type=&uri=apidata/api/gkv3/school/lists'
        })



        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://www.gaokao.cn',
            'Referer': 'https://www.gaokao.cn/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0',
            'sec-ch-ua': '"Microsoft Edge";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        json_data = {
            'keyword': '',
            'page': page,
            'province_id': '',
            'ranktype': '',
            'request_type': 1,
            'signsafe': result,
            'size': 20,
            'top_school_id': '[57,3238,1569,3269]',
            'type': '',
            'uri': 'apidata/api/gkv3/school/lists',
        }

        response = requests.post(
            f'https://api.zjzw.cn/web/api/?keyword=&page={page}&province_id=&ranktype=&request_type=1&size=20&top_school_id=[57,3238,1569,3269]&type=&uri=apidata/api/gkv3/school/lists&signsafe={result}',
            headers=headers,
            json=json_data,
        )

        obj = re.findall(r'"answerurl":"(?P<url>.*?)".*?"city_name":"(?P<city_name>.*?)".*?"hightitle":"(?P<hightitle>.*?)",',response.text)

        for match in obj:
            url, city_name, hightitle = match
            print(f"URL: {url}")
            print(f"City: {city_name}")
            print(f"Title: {hightitle}")
            print("------")
            f.write(f"URL: {url}\nCity: {city_name}\nTitle: {hightitle}\n------\n")

        time.sleep(random.uniform(3,5))
        
