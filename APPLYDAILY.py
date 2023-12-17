import requests
import os
import xml.etree.ElementTree as ET

cookie_value = os.getenv('COOKIE')

cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookie_value.split('; ')}

headers = {
    'DNT': '1',
    'Referer': 'https://www.south-plus.net/plugin.php?H_name-tasks.html',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'H_name': 'tasks',
    'action': 'ajax',
    'actions': 'job',
    'cid': '15',
    'nowtime': '1702806835359',
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
    print("XML格式不正确，请检查代码")
