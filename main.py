import os
import urllib.parse
import urllib.request
import subprocess
import re

def sc_send(text, desp='', key=os.getenv('SCKEY')):
    postdata = urllib.parse.urlencode({'text': text, 'desp': desp}).encode('utf-8')
    url = f'https://sctapi.ftqq.com/{key}.send'
    req = urllib.request.Request(url, data=postdata, method='POST')
    with urllib.request.urlopen(req) as response:
        result = response.read().decode('utf-8')
    return result

process_1 = subprocess.Popen(['python', 'APPLYDAILY.py'], stdout=subprocess.PIPE)
output_1, _ = process_1.communicate()

process_2 = subprocess.Popen(['python', 'COLLECTDAILY.py'], stdout=subprocess.PIPE)
output_2, _ = process_2.communicate()

process_3 = subprocess.Popen(['python', 'APPLYWEEKLY.py'], stdout=subprocess.PIPE)
output_3, _ = process_3.communicate()

process_4 = subprocess.Popen(['python', 'COLLECTWEEKLY.py'], stdout=subprocess.PIPE)
output_4, _ = process_4.communicate()

response_text1 = output_2.decode()

if re.search(r"成功", response_text1):
    title1 = "南+日常成功，"
else:
    title1 = "南+日常失败，"

response_text2 = output_4.decode()

if re.search(r"成功", response_text1):
    title2 = "周常成功，"
else:
    title2 = "周常失败，"


# 合并输出为一个变量
merged_content = output_1.decode() + output_2.decode() + output_3.decode() + output_4.decode()
merged_title = title1 + title2

print(merged_title)
print(merged_content)

ret = sc_send(merged_title, merged_content)
print(ret)