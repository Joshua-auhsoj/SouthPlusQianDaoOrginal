from bs4 import BeautifulSoup
import os
import requests

cookie_value = os.getenv('COOKIE')
cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookie_value.split('; ')}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
    'dnt': '1',
    'priority': 'u=0, i',
    'referer': 'https://www.south-plus.net/plugin.php?H_name-tasks-actions-newtasks.html.html',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"125.0.6422.142"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="125.0.6422.142", "Chromium";v="125.0.6422.142", "Not.A/Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}
response = requests.get('https://www.south-plus.net/', cookies=cookies, headers=headers)
# 定义HTML代码
html_code = response.text
# 假设html_code是包含HTML代码的变量
# 使用BeautifulSoup解析HTML代码
soup = BeautifulSoup(html_code, 'html.parser')
# 找到包含SP币值的<span>标签
sp_coin_span = soup.find('span', class_='s3 f10')
# 提取SP币值
sp_coin_value = sp_coin_span.text
# 输出SP币值
print("SP币:", sp_coin_value)
