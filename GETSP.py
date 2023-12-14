import requests
from bs4 import BeautifulSoup
import os
import requests
cookie_value = os.getenv('COOKIE')

cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookie_value.split('; ')}



headers = {
    'authority': 'north-plus.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="109", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36',
}

response = requests.get('https://north-plus.net/', cookies=cookies, headers=headers, verify=False)

# 定义HTML代码
html_code = response.text


# 假设html_code是包含HTML代码的变量
html_code = response.text

# 使用BeautifulSoup解析HTML代码
soup = BeautifulSoup(html_code, 'html.parser')

# 找到包含SP币值的<span>标签
sp_coin_span = soup.find('span', class_='s3 f10')

# 提取SP币值
sp_coin_value = sp_coin_span.text

# 输出SP币值
print("SP币值:", sp_coin_value)