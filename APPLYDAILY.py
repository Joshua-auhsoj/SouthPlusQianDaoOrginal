import requests
import os
import xml.etree.ElementTree as ET

cookies = os.getenv('COOKIE')


headers = {
    'authority': 'www.south-plus.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
    'dnt': '1',
    'referer': 'https://www.south-plus.net/plugin.php?H_name-tasks.html.html',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

params = {
    'H_name': 'tasks',
    'action': 'ajax',
    'actions': 'job',
    'cid': '15',
    'nowtime': '1702877397639',
    'verify': '9d5c5785',
}

response = requests.get('https://www.south-plus.net/plugin.php', params=params, cookies=cookies, headers=headers)

data = response.text

# 解析XML数据
root = ET.fromstring(data)
cdata = root.text

# 提取变量值
values = cdata.split('\t')
if len(values) == 2:
    action = values[0]
    message = values[1]

    print('日常-' + message)
else:
    print("XML格式不正确，请检查COOKIE设置")
