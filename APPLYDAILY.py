import requests
import os
import xml.etree.ElementTree as ET
cookie_value = os.getenv('COOKIE')

cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookie_value.split('; ')}

headers = {
    'authority': 'www.north-plus.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://www.north-plus.net/plugin.php?H_name-tasks.html.html',
    'sec-ch-ua': '"Chromium";v="109", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36',
}

params = {
    'H_name': 'tasks',
    'action': 'ajax',
    'actions': 'job',
    'cid': '15',
    'nowtime': '1702456871219',
    'verify': 'ca81e905',
}

response = requests.get('https://www.north-plus.net/plugin.php', params=params, cookies=cookies, headers=headers)


data = response.text

# 解析XML数据
root = ET.fromstring(data)
cdata = root.text

# 提取变量值
values = cdata.split('\t')
if len(values) == 2:
    action = values[0]
    message = values[1]


    print('日常-'+message)
else:
    print("Invalid XML format")
